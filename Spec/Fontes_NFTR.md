# Fontes NFTR — Professor Layton e o Futuro Perdido (playton-3)

Documento gerado a partir da engenharia reversa de `nftr.py:1` e das fontes em `Previewer/Fontes/` (`fontevent.nftr`, `fontq.nftr`) e `Fontes/` (`font18.NFTR`, `fontevent.NFTR`, `fontq.NFTR`).

> Foco do documento: **largura real de cada glifo** — `padding esquerdo + largura do bitmap + padding direito = avanço total`.

---

## 1. Estrutura do arquivo NFTR (Nitro Font Resource)

Conforme implementado em `nftr.py:38-86` (`Decode.read_header`):

```
Offset  Tamanho  Campo
0x00    4        stamp "RTFN" (little-endian, lido como [::-1] == "NFTR") — nftr.py:42
0x04    4        filesize (u32 LE) — nftr.py:45
0x08    2        header size (u16) — nftr.py:46
0x0A    2        número de chunks (u16) — nftr.py:47 → sempre 4 (FINF, CGLP, CWDH, CMAP)
0x10    —        chunk FINF
```

### 1.1 FINF — Font Info (`nftr.py:49-55`)

```
FINF stamp "FNIF" (4)
+ size u32
+ 8 bytes desconhecidos/padding
+ cglp_offset u32  (ponteiro absoluto no arquivo) — nftr.py:53
+ cwdh_offset u32  — nftr.py:54
+ cmap_offset u32  — nftr.py:55
```

No disco os offsets aparecem como `0x34 / 0x8E8 / 0xAD4` para `fontevent` e `0x34 / 0x5D4 / 0x7C0` para `fontq`; `nftr.py:58-85` faz `seek(... -8)` porque o código espera o offset do *conteúdo* e não do cabeçalho do chunk.

### 1.2 CGLP — Character Glyph (`nftr.py:58-67`)

```
CGLP stamp "PLGC" (4)
+ size u32       — nftr.py:61
+ width  u8      — largura da célula em pixels — nftr.py:62
+ height u8      — altura da célula — nftr.py:63
+ length u16     — bytes por glifo — nftr.py:64
+ 2 bytes padding
+ bpp    u16     — bits por pixel (sempre 1 = 1bpp, 1 bit = on/off) — nftr.py:66
+ bitmaps ...
```

O bitmap é 1bpp desempacotado em `nftr.py:87-113`: cada byte é expandido bit a bit (`shift=[7..0]`), reagrupado por `width` e expandido para 0/255 para exibição GTK.

| Arquivo | `width` | `height` | `length` | `bpp` | `cglp_size` | nº glifos (`size/length`) |
|---|---|---|---|---|---|---|
| `fontevent.nftr` | **9** | **12** | 14 | 1 | 2228 | 159 |
| `fontq.nftr`     | **7** | **10** |  9 | 1 | 1440 | 160 |
| `font18.NFTR`    | **14**| **15** | 27 | 1 | 6388 | 236 |

> `width`×`height` é a célula máxima; nem todo pixel é usado — a largura *útil* vem do CWDH.

### 1.3 CWDH — Character Width (`nftr.py:69-76`, `nftr.py:124-132`)

```
CWDH stamp "HDWC" (4)
+ size u32
+ min  u16  — primeiro índice da tabela
+ max  u16  — último índice (inclusive)
+ 4 bytes desconhecidos
+ tabela: (max-min+1) × 3 bytes
```

Cada entrada tem **3 bytes** — `nftr.py:129-131`:

```python
# nftr.py:128  "(Offset, Largura, Próximo Offset)"
left  = u8  # padding esquerdo / left bearing
glyph = u8  # largura desenhada do glifo
adv   = u8  # "próximo offset" = avanço total / char width
```

**Fórmula da largura total (o que o motor de texto usa para avançar o cursor):**

```
total = adv
right = adv - left - glyph   # padding direito implícito
largura_real = left + glyph + right == adv
```

Exemplo `fontevent` com `A` (`U+0041` → idx 29 → `(1,8,10)`): `left=1`, `glyph=8`, `right=1`, `total=10 px`.
Exemplo `fontq` com `A` (`→ idx 29 → (0,5,5)`): `left=0`, `glyph=5`, `right=0`, `total=5 px`.

> Para medir uma string: `soma = sum(adv para cada caractere)` — não use `glyph` isolado.

### 1.4 CMAP — Character Map (`nftr.py:78-85`, `nftr.py:115-122`)

```
CMAP stamp "PAMC" (4)
+ size u32
+ min  u16  — primeiro codepoint
+ max  u16  — último codepoint
+ 8 bytes desconhecidos
+ tabela: (max-min+1) × u16  — índice na CWDH/CGLP ou 0xFFFF = não mapeado
```

- `fontevent` e `fontq`: **um único CMAP** `32–252` (221 entradas, 158 mapeadas, resto `0xFFFF`).
- `font18.NFTR`: **quatro CMAPs** (Shift-JIS/Japonês):
  - `0x829F–0x82F1` (83 entradas, size 0x18 — tipo diferente),
  - `43–122` (80 entradas, size 0xB4),
  - `0x8340–0x8393` (84 entradas, size 0xBC),
  - `0–65535` (tipo 2 / sparse, size 0x20).
  Por isso `font18` tem 236 CWDH entries (`0–235`) e células maiores (14×15) — fonte grande/diálogo JP. Não é usada no `Previewer`.

Decodificação em `nftr.py:115-122`: itera de `min` a `max`, lê `u16` e ignora `0xFFFF`.

---

## 2. Onde cada fonte é usada (Previewer)

Extraído de `Previewer/Configs/*.ini`:

| Screen | `ScreenFont` | Uso no jogo | `NewLine` (px) |
|---|---|---|---|
| 01 Textos Normais | `fontevent.nftr` | diálogos principais | 16 |
| 02 Páginas do Diário | `fontevent.nftr` | journal | 15 |
| 04 Comentários | `fontevent.nftr` | comments | 15 |
| 07 Mistérios | `fontevent.nftr` | misteries | 16 |
| 09 Fundo Verde | `fontevent.nftr` | chroma | 16 |
| 03 Enigmas | `fontq.nftr` | puzzle text | 12 |
| 05 Perfis | `fontq.nftr` | profile | 12 |
| 06 Nomes | `fontq.nftr` | names | 12 |
| 08 Dicas dos Enigmas | `fontq.nftr` | hints | 12 |

→ **Regra prática para tradução**: textos longos/diálogos (fontevent) têm ~7 px por caractere; textos curtos/UI (fontq) ~5 px por caractere.

---

## 3. Largura de cada caractere — tabelas completas

> Colunas: **CP** = codepoint decimal, **Hex**, **Char**, **Idx** = índice CWDH/CGLP, **L** = left, **W** = glyph, **R** = right (`adv-L-W`), **Total** = `adv` (largura a considerar para quebra de linha).  
> `R` é derivado; não existe como byte isolado no arquivo — é o padding direito.

### 3.1 `fontevent.nftr` — 9×12 — Textos Normais (158 glifos mapeados)

Média do avanço: **7,06 px** — mín 4 px, máx 10 px.

| CP | Hex | Char | Idx | L | W | R | Total |
|---|---|---|---|---|---|---|---|
| 32 | U+0020 | ` ` | 0 | 3 | 0 | 1 | **4** |
| 33 | U+0021 | `!` | 0 | 3 | 0 | 1 | **4** |
| 34 | U+0022 | `"` | 0 | 3 | 0 | 1 | **4** |
| 35 | U+0023 | `#` | 1 | 1 | 2 | 1 | **4** |
| 36 | U+0024 | `$` | 2 | 1 | 4 | 1 | **6** |
| 37 | U+0025 | `%` | 3 | 1 | 6 | 1 | **8** |
| 38 | U+0026 | `&` | 4 | 1 | 6 | 1 | **8** |
| 39 | U+0027 | `'` | 5 | 1 | 8 | 1 | **10** |
| 40 | U+0028 | `(` | 6 | 1 | 7 | 1 | **9** |
| 41 | U+0029 | `)` | 7 | 1 | 3 | 1 | **5** |
| 42 | U+002A | `*` | 8 | 1 | 4 | 1 | **6** |
| 43 | U+002B | `+` | 9 | 1 | 4 | 1 | **6** |
| 44 | U+002C | `,` | 10 | 1 | 6 | 1 | **8** |
| 45 | U+002D | `-` | 11 | 1 | 6 | 1 | **8** |
| 46 | U+002E | `.` | 12 | 1 | 3 | 1 | **5** |
| 47 | U+002F | `/` | 13 | 1 | 6 | 1 | **8** |
| 48 | U+0030 | `0` | 14 | 1 | 3 | 1 | **5** |
| 49 | U+0031 | `1` | 15 | 1 | 4 | 1 | **6** |
| 50 | U+0032 | `2` | 16 | 0 | 7 | 0 | **7** |
| 51 | U+0033 | `3` | 17 | 1 | 4 | 0 | **5** |
| 52 | U+0034 | `4` | 18 | 0 | 7 | 0 | **7** |
| 53 | U+0035 | `5` | 19 | 0 | 7 | 0 | **7** |
| 54 | U+0036 | `6` | 20 | 0 | 7 | 0 | **7** |
| 55 | U+0037 | `7` | 21 | 0 | 7 | 0 | **7** |
| 56 | U+0038 | `8` | 22 | 0 | 7 | 0 | **7** |
| 57 | U+0039 | `9` | 23 | 0 | 7 | 0 | **7** |
| 58 | U+003A | `:` | 24 | 0 | 7 | 0 | **7** |
| 59 | U+003B | `;` | 25 | 0 | 7 | 0 | **7** |
| 60 | U+003C | `<` | 26 | 1 | 3 | 1 | **5** |
| 61 | U+003D | `=` | 27 | 1 | 3 | 1 | **5** |
| 63 | U+003F | `?` | 28 | 1 | 6 | 1 | **8** |
| 65 | U+0041 | `A` | 29 | 1 | 8 | 1 | **10** |
| 66 | U+0042 | `B` | 30 | 0 | 9 | 0 | **9** |
| 67 | U+0043 | `C` | 31 | 0 | 8 | 0 | **8** |
| 68 | U+0044 | `D` | 32 | 0 | 8 | 0 | **8** |
| 69 | U+0045 | `E` | 33 | 0 | 8 | 0 | **8** |
| 70 | U+0046 | `F` | 34 | 0 | 8 | 0 | **8** |
| 71 | U+0047 | `G` | 35 | 0 | 8 | 0 | **8** |
| 72 | U+0048 | `H` | 36 | 0 | 8 | 0 | **8** |
| 73 | U+0049 | `I` | 37 | 0 | 8 | 0 | **8** |
| 74 | U+004A | `J` | 38 | 0 | 8 | 0 | **8** |
| 75 | U+004B | `K` | 39 | 1 | 4 | 1 | **6** |
| 76 | U+004C | `L` | 40 | 0 | 8 | 0 | **8** |
| 77 | U+004D | `M` | 41 | 0 | 8 | 0 | **8** |
| 78 | U+004E | `N` | 42 | 0 | 7 | 0 | **7** |
| 79 | U+004F | `O` | 43 | 0 | 8 | 0 | **8** |
| 80 | U+0050 | `P` | 44 | 0 | 8 | 0 | **8** |
| 81 | U+0051 | `Q` | 45 | 0 | 9 | 0 | **9** |
| 82 | U+0052 | `R` | 46 | 0 | 8 | 0 | **8** |
| 83 | U+0053 | `S` | 47 | 0 | 9 | 0 | **9** |
| 84 | U+0054 | `T` | 48 | 0 | 8 | 0 | **8** |
| 85 | U+0055 | `U` | 49 | 0 | 8 | 0 | **8** |
| 86 | U+0056 | `V` | 50 | 0 | 8 | 0 | **8** |
| 87 | U+0057 | `W` | 51 | 0 | 8 | 0 | **8** |
| 88 | U+0058 | `X` | 52 | 0 | 8 | 0 | **8** |
| 89 | U+0059 | `Y` | 53 | 0 | 8 | 0 | **8** |
| 90 | U+005A | `Z` | 54 | 0 | 8 | 0 | **8** |
| 91 | U+005B | `[` | 55 | 0 | 8 | 0 | **8** |
| 92 | U+005C | `\` | 56 | 0 | 8 | 0 | **8** |
| 93 | U+005D | `]` | 57 | 1 | 4 | 1 | **6** |
| 94 | U+005E | `^` | 58 | 1 | 4 | 1 | **6** |
| 95 | U+005F | `_` | 59 | 1 | 4 | 1 | **6** |
| 96 | U+0060 | ``` | 60 | 1 | 6 | 1 | **8** |
| 97 | U+0061 | `a` | 61 | 0 | 6 | 0 | **6** |
| 99 | U+0063 | `c` | 62 | 0 | 7 | 0 | **7** |
| 100 | U+0064 | `d` | 63 | 0 | 6 | 0 | **6** |
| 101 | U+0065 | `e` | 64 | 0 | 6 | 0 | **6** |
| 102 | U+0066 | `f` | 65 | 0 | 6 | 0 | **6** |
| 103 | U+0067 | `g` | 66 | 0 | 6 | 0 | **6** |
| 104 | U+0068 | `h` | 67 | 0 | 6 | 0 | **6** |
| 105 | U+0069 | `i` | 68 | 0 | 6 | 0 | **6** |
| 106 | U+006A | `j` | 69 | 0 | 6 | 0 | **6** |
| 107 | U+006B | `k` | 70 | 1 | 2 | 1 | **4** |
| 108 | U+006C | `l` | 71 | 0 | 6 | 0 | **6** |
| 109 | U+006D | `m` | 72 | 0 | 6 | 0 | **6** |
| 110 | U+006E | `n` | 73 | 1 | 2 | 1 | **4** |
| 111 | U+006F | `o` | 74 | 0 | 8 | 0 | **8** |
| 112 | U+0070 | `p` | 75 | 0 | 6 | 0 | **6** |
| 113 | U+0071 | `q` | 76 | 0 | 7 | 0 | **7** |
| 114 | U+0072 | `r` | 77 | 0 | 6 | 0 | **6** |
| 115 | U+0073 | `s` | 78 | 0 | 6 | 0 | **6** |
| 116 | U+0074 | `t` | 79 | 0 | 6 | 0 | **6** |
| 117 | U+0075 | `u` | 80 | 0 | 6 | 0 | **6** |
| 118 | U+0076 | `v` | 81 | 0 | 6 | 0 | **6** |
| 119 | U+0077 | `w` | 82 | 0 | 6 | 0 | **6** |
| 120 | U+0078 | `x` | 83 | 0 | 7 | 0 | **7** |
| 121 | U+0079 | `y` | 84 | 0 | 8 | 0 | **8** |
| 122 | U+007A | `z` | 85 | 0 | 7 | 0 | **7** |
| 123 | U+007B | `{` | 86 | 1 | 6 | 1 | **8** |
| 124 | U+007C | `|` | 87 | 0 | 6 | 0 | **6** |
| 130 | U+0082 | U+0082 | 88 | 0 | 8 | 0 | **8** |
| 132 | U+0084 | U+0084 | 89 | 1 | 3 | 1 | **5** |
| 134 | U+0086 | U+0086 | 90 | 1 | 4 | 1 | **6** |
| 141 | U+008D | U+008D | 91 | 1 | 4 | 1 | **6** |
| 142 | U+008E | U+008E | 92 | 0 | 10 | 0 | **10** |
| 147 | U+0093 | U+0093 | 93 | 1 | 3 | 1 | **5** |
| 148 | U+0094 | U+0094 | 94 | 1 | 3 | 1 | **5** |
| 149 | U+0095 | U+0095 | 95 | 1 | 4 | 1 | **6** |
| 150 | U+0096 | U+0096 | 96 | 1 | 4 | 1 | **6** |
| 157 | U+009D | U+009D | 97 | 1 | 4 | 1 | **6** |
| 158 | U+009E | U+009E | 98 | 0 | 10 | 0 | **10** |
| 163 | U+00A3 | `£` | 99 | 1 | 2 | 1 | **4** |
| 165 | U+00A5 | `¥` | 100 | 0 | 8 | 0 | **8** |
| 172 | U+00AC | `¬` | 101 | 1 | 6 | 1 | **8** |
| 173 | U+00AD | `­` | 102 | 1 | 6 | 1 | **8** |
| 174 | U+00AE | `®` | 103 | 1 | 6 | 1 | **8** |
| 175 | U+00AF | `¯` | 104 | 1 | 6 | 1 | **8** |
| 176 | U+00B0 | `°` | 105 | 1 | 6 | 1 | **8** |
| 177 | U+00B1 | `±` | 106 | 1 | 6 | 1 | **8** |
| 178 | U+00B2 | `²` | 107 | 1 | 4 | 1 | **6** |
| 188 | U+00BC | `¼` | 108 | 1 | 6 | 1 | **8** |
| 189 | U+00BD | `½` | 109 | 1 | 6 | 1 | **8** |
| 193 | U+00C1 | `Á` | 110 | 1 | 8 | 1 | **10** |
| 194 | U+00C2 | `Â` | 111 | 0 | 8 | 0 | **8** |
| 195 | U+00C3 | `Ã` | 112 | 0 | 7 | 0 | **7** |
| 196 | U+00C4 | `Ä` | 113 | 0 | 8 | 0 | **8** |
| 197 | U+00C5 | `Å` | 114 | 0 | 8 | 0 | **8** |
| 198 | U+00C6 | `Æ` | 115 | 0 | 8 | 0 | **8** |
| 199 | U+00C7 | `Ç` | 116 | 0 | 8 | 0 | **8** |
| 201 | U+00C9 | `É` | 117 | 0 | 8 | 0 | **8** |
| 202 | U+00CA | `Ê` | 118 | 0 | 8 | 0 | **8** |
| 203 | U+00CB | `Ë` | 119 | 0 | 8 | 0 | **8** |
| 204 | U+00CC | `Ì` | 120 | 0 | 8 | 0 | **8** |
| 205 | U+00CD | `Í` | 121 | 0 | 8 | 0 | **8** |
| 206 | U+00CE | `Î` | 122 | 0 | 3 | 2 | **5** |
| 207 | U+00CF | `Ï` | 123 | 2 | 3 | 0 | **5** |
| 208 | U+00D0 | `Ð` | 124 | 1 | 4 | 1 | **6** |
| 209 | U+00D1 | `Ñ` | 125 | 1 | 4 | 1 | **6** |
| 211 | U+00D3 | `Ó` | 126 | 0 | 8 | 0 | **8** |
| 212 | U+00D4 | `Ô` | 127 | 0 | 8 | 0 | **8** |
| 213 | U+00D5 | `Õ` | 128 | 0 | 8 | 0 | **8** |
| 214 | U+00D6 | `Ö` | 129 | 0 | 8 | 0 | **8** |
| 216 | U+00D8 | `Ø` | 130 | 0 | 8 | 0 | **8** |
| 219 | U+00DB | `Û` | 131 | 0 | 8 | 0 | **8** |
| 220 | U+00DC | `Ü` | 132 | 0 | 8 | 0 | **8** |
| 221 | U+00DD | `Ý` | 133 | 0 | 8 | 0 | **8** |
| 222 | U+00DE | `Þ` | 134 | 0 | 8 | 0 | **8** |
| 225 | U+00E1 | `á` | 135 | 0 | 8 | 0 | **8** |
| 226 | U+00E2 | `â` | 136 | 0 | 8 | 0 | **8** |
| 227 | U+00E3 | `ã` | 137 | 0 | 8 | 0 | **8** |
| 228 | U+00E4 | `ä` | 138 | 0 | 8 | 0 | **8** |
| 230 | U+00E6 | `æ` | 139 | 0 | 8 | 0 | **8** |
| 233 | U+00E9 | `é` | 140 | 0 | 7 | 0 | **7** |
| 234 | U+00EA | `ê` | 141 | 0 | 7 | 0 | **7** |
| 235 | U+00EB | `ë` | 142 | 0 | 7 | 0 | **7** |
| 236 | U+00EC | `ì` | 143 | 0 | 7 | 0 | **7** |
| 237 | U+00ED | `í` | 144 | 0 | 7 | 0 | **7** |
| 238 | U+00EE | `î` | 145 | 0 | 3 | 2 | **5** |
| 239 | U+00EF | `ï` | 146 | 2 | 3 | 0 | **5** |
| 240 | U+00F0 | `ð` | 147 | 1 | 4 | 1 | **6** |
| 241 | U+00F1 | `ñ` | 148 | 1 | 4 | 1 | **6** |
| 243 | U+00F3 | `ó` | 149 | 0 | 7 | 0 | **7** |
| 244 | U+00F4 | `ô` | 150 | 0 | 8 | 0 | **8** |
| 245 | U+00F5 | `õ` | 151 | 0 | 8 | 0 | **8** |
| 246 | U+00F6 | `ö` | 152 | 0 | 8 | 0 | **8** |
| 248 | U+00F8 | `ø` | 153 | 0 | 8 | 0 | **8** |
| 251 | U+00FB | `û` | 154 | 0 | 7 | 0 | **7** |
| 252 | U+00FC | `ü` | 155 | 0 | 7 | 0 | **7** |

> Observação: `U+0020` (espaço) tem `W=0` — é um avanço puramente vazio (4 px). `k` e `n` são os únicos minúsculos estreitos (4 px) nesta fonte; `A` é a mais larga (10 px).

### 3.2 `fontq.nftr` — 7×10 — Enigmas / Perfis / Nomes / Dicas (158 glifos)

Média: **4,70 px** — mín 2 px, máx 7 px. Quase monoespaçada.

| CP | Hex | Char | Idx | L | W | R | Total |
|---|---|---|---|---|---|---|---|
| 32 | U+0020 | ` ` | 0 | 4 | 0 | 0 | **4** |
| 33 | U+0021 | `!` | 0 | 4 | 0 | 0 | **4** |
| 34 | U+0022 | `"` | 0 | 4 | 0 | 0 | **4** |
| 35 | U+0023 | `#` | 1 | 1 | 2 | 1 | **4** |
| 36 | U+0024 | `$` | 2 | 1 | 4 | 1 | **6** |
| 37 | U+0025 | `%` | 3 | 0 | 6 | 0 | **6** |
| 38 | U+0026 | `&` | 4 | 0 | 6 | 0 | **6** |
| 39 | U+0027 | `'` | 5 | 0 | 5 | 0 | **5** |
| 40 | U+0028 | `(` | 6 | 0 | 6 | 0 | **6** |
| 41 | U+0029 | `)` | 7 | 1 | 3 | 1 | **5** |
| 42 | U+002A | `*` | 8 | 0 | 4 | 1 | **5** |
| 43 | U+002B | `+` | 9 | 1 | 4 | 0 | **5** |
| 44 | U+002C | `,` | 10 | 0 | 6 | 0 | **6** |
| 45 | U+002D | `-` | 11 | 0 | 6 | 0 | **6** |
| 46 | U+002E | `.` | 12 | 0 | 3 | 0 | **3** |
| 47 | U+002F | `/` | 13 | 0 | 6 | 0 | **6** |
| 48 | U+0030 | `0` | 14 | 0 | 3 | 0 | **3** |
| 49 | U+0031 | `1` | 15 | 0 | 4 | 0 | **4** |
| 50 | U+0032 | `2` | 16 | 0 | 6 | 0 | **6** |
| 51 | U+0033 | `3` | 17 | 1 | 4 | 0 | **5** |
| 52 | U+0034 | `4` | 18 | 0 | 6 | 0 | **6** |
| 53 | U+0035 | `5` | 19 | 0 | 6 | 0 | **6** |
| 54 | U+0036 | `6` | 20 | 0 | 6 | 0 | **6** |
| 55 | U+0037 | `7` | 21 | 0 | 6 | 0 | **6** |
| 56 | U+0038 | `8` | 22 | 0 | 6 | 0 | **6** |
| 57 | U+0039 | `9` | 23 | 0 | 5 | 0 | **5** |
| 58 | U+003A | `:` | 24 | 0 | 5 | 0 | **5** |
| 59 | U+003B | `;` | 25 | 0 | 5 | 0 | **5** |
| 60 | U+003C | `<` | 26 | 0 | 2 | 0 | **2** |
| 61 | U+003D | `=` | 27 | 0 | 2 | 0 | **2** |
| 63 | U+003F | `?` | 28 | 0 | 5 | 0 | **5** |
| 65 | U+0041 | `A` | 29 | 0 | 5 | 0 | **5** |
| 66 | U+0042 | `B` | 30 | 0 | 5 | 0 | **5** |
| 67 | U+0043 | `C` | 31 | 0 | 5 | 0 | **5** |
| 68 | U+0044 | `D` | 32 | 0 | 5 | 0 | **5** |
| 69 | U+0045 | `E` | 33 | 0 | 5 | 0 | **5** |
| 70 | U+0046 | `F` | 34 | 0 | 5 | 0 | **5** |
| 71 | U+0047 | `G` | 35 | 0 | 5 | 0 | **5** |
| 72 | U+0048 | `H` | 36 | 0 | 5 | 0 | **5** |
| 73 | U+0049 | `I` | 37 | 0 | 5 | 0 | **5** |
| 74 | U+004A | `J` | 38 | 0 | 5 | 0 | **5** |
| 75 | U+004B | `K` | 39 | 0 | 3 | 0 | **3** |
| 76 | U+004C | `L` | 40 | 0 | 5 | 0 | **5** |
| 77 | U+004D | `M` | 41 | 0 | 5 | 0 | **5** |
| 78 | U+004E | `N` | 42 | 0 | 5 | 0 | **5** |
| 79 | U+004F | `O` | 43 | 0 | 5 | 0 | **5** |
| 80 | U+0050 | `P` | 44 | 0 | 5 | 0 | **5** |
| 81 | U+0051 | `Q` | 45 | 0 | 5 | 0 | **5** |
| 82 | U+0052 | `R` | 46 | 0 | 5 | 0 | **5** |
| 83 | U+0053 | `S` | 47 | 0 | 5 | 0 | **5** |
| 84 | U+0054 | `T` | 48 | 0 | 5 | 0 | **5** |
| 85 | U+0055 | `U` | 49 | 0 | 5 | 0 | **5** |
| 86 | U+0056 | `V` | 50 | 0 | 5 | 0 | **5** |
| 87 | U+0057 | `W` | 51 | 0 | 5 | 0 | **5** |
| 88 | U+0058 | `X` | 52 | 0 | 5 | 0 | **5** |
| 89 | U+0059 | `Y` | 53 | 0 | 5 | 0 | **5** |
| 90 | U+005A | `Z` | 54 | 0 | 5 | 0 | **5** |
| 91 | U+005B | `[` | 55 | 0 | 5 | 0 | **5** |
| 92 | U+005C | `\` | 56 | 0 | 5 | 0 | **5** |
| 93 | U+005D | `]` | 57 | 0 | 3 | 1 | **4** |
| 95 | U+005F | `_` | 58 | 1 | 3 | 0 | **4** |
| 96 | U+0060 | ``` | 59 | 0 | 5 | 0 | **5** |
| 97 | U+0061 | `a` | 60 | 0 | 3 | 0 | **3** |
| 98 | U+0062 | `b` | 61 | 0 | 3 | 0 | **3** |
| 99 | U+0063 | `c` | 62 | 0 | 5 | 0 | **5** |
| 100 | U+0064 | `d` | 63 | 0 | 5 | 0 | **5** |
| 101 | U+0065 | `e` | 64 | 0 | 5 | 0 | **5** |
| 102 | U+0066 | `f` | 65 | 0 | 5 | 0 | **5** |
| 103 | U+0067 | `g` | 66 | 0 | 5 | 0 | **5** |
| 104 | U+0068 | `h` | 67 | 0 | 5 | 0 | **5** |
| 105 | U+0069 | `i` | 68 | 0 | 5 | 0 | **5** |
| 106 | U+006A | `j` | 69 | 0 | 5 | 0 | **5** |
| 107 | U+006B | `k` | 70 | 1 | 1 | 1 | **3** |
| 108 | U+006C | `l` | 71 | 0 | 5 | 0 | **5** |
| 109 | U+006D | `m` | 72 | 0 | 5 | 0 | **5** |
| 110 | U+006E | `n` | 73 | 1 | 1 | 1 | **3** |
| 111 | U+006F | `o` | 74 | 0 | 5 | 0 | **5** |
| 112 | U+0070 | `p` | 75 | 0 | 5 | 0 | **5** |
| 113 | U+0071 | `q` | 76 | 0 | 5 | 0 | **5** |
| 114 | U+0072 | `r` | 77 | 0 | 5 | 0 | **5** |
| 115 | U+0073 | `s` | 78 | 0 | 5 | 0 | **5** |
| 116 | U+0074 | `t` | 79 | 0 | 5 | 0 | **5** |
| 117 | U+0075 | `u` | 80 | 0 | 5 | 0 | **5** |
| 118 | U+0076 | `v` | 81 | 0 | 5 | 0 | **5** |
| 119 | U+0077 | `w` | 82 | 0 | 5 | 0 | **5** |
| 120 | U+0078 | `x` | 83 | 0 | 5 | 0 | **5** |
| 121 | U+0079 | `y` | 84 | 0 | 5 | 0 | **5** |
| 122 | U+007A | `z` | 85 | 0 | 5 | 0 | **5** |
| 123 | U+007B | `{` | 86 | 0 | 5 | 0 | **5** |
| 124 | U+007C | `|` | 87 | 0 | 5 | 0 | **5** |
| 130 | U+0082 | U+0082 | 88 | 0 | 5 | 0 | **5** |
| 132 | U+0084 | U+0084 | 89 | 0 | 2 | 0 | **2** |
| 134 | U+0086 | U+0086 | 90 | 0 | 3 | 0 | **3** |
| 141 | U+008D | U+008D | 91 | 0 | 2 | 0 | **2** |
| 142 | U+008E | U+008E | 92 | 0 | 7 | 0 | **7** |
| 147 | U+0093 | U+0093 | 93 | 1 | 2 | 1 | **4** |
| 148 | U+0094 | U+0094 | 94 | 1 | 2 | 1 | **4** |
| 149 | U+0095 | U+0095 | 95 | 1 | 3 | 1 | **5** |
| 150 | U+0096 | U+0096 | 96 | 1 | 3 | 1 | **5** |
| 157 | U+009D | U+009D | 97 | 0 | 2 | 0 | **2** |
| 158 | U+009E | U+009E | 98 | 0 | 7 | 0 | **7** |
| 163 | U+00A3 | `£` | 99 | 1 | 1 | 1 | **3** |
| 165 | U+00A5 | `¥` | 100 | 0 | 5 | 0 | **5** |
| 172 | U+00AC | `¬` | 101 | 0 | 5 | 0 | **5** |
| 173 | U+00AD | `­` | 102 | 0 | 4 | 0 | **4** |
| 174 | U+00AE | `®` | 103 | 0 | 5 | 0 | **5** |
| 175 | U+00AF | `¯` | 104 | 0 | 4 | 0 | **4** |
| 176 | U+00B0 | `°` | 105 | 0 | 4 | 0 | **4** |
| 177 | U+00B1 | `±` | 106 | 0 | 4 | 0 | **4** |
| 178 | U+00B2 | `²` | 107 | 0 | 3 | 0 | **3** |
| 188 | U+00BC | `¼` | 108 | 0 | 5 | 0 | **5** |
| 189 | U+00BD | `½` | 109 | 0 | 4 | 0 | **4** |
| 193 | U+00C1 | `Á` | 110 | 0 | 5 | 0 | **5** |
| 194 | U+00C2 | `Â` | 111 | 0 | 5 | 0 | **5** |
| 195 | U+00C3 | `Ã` | 112 | 0 | 5 | 0 | **5** |
| 196 | U+00C4 | `Ä` | 113 | 0 | 5 | 0 | **5** |
| 197 | U+00C5 | `Å` | 114 | 0 | 5 | 0 | **5** |
| 198 | U+00C6 | `Æ` | 115 | 0 | 5 | 0 | **5** |
| 199 | U+00C7 | `Ç` | 116 | 0 | 5 | 0 | **5** |
| 201 | U+00C9 | `É` | 117 | 0 | 5 | 0 | **5** |
| 202 | U+00CA | `Ê` | 118 | 0 | 5 | 0 | **5** |
| 203 | U+00CB | `Ë` | 119 | 0 | 5 | 0 | **5** |
| 204 | U+00CC | `Ì` | 120 | 0 | 5 | 0 | **5** |
| 205 | U+00CD | `Í` | 121 | 0 | 5 | 0 | **5** |
| 206 | U+00CE | `Î` | 122 | 0 | 2 | 1 | **3** |
| 207 | U+00CF | `Ï` | 123 | 1 | 2 | 0 | **3** |
| 208 | U+00D0 | `Ð` | 124 | 0 | 3 | 0 | **3** |
| 209 | U+00D1 | `Ñ` | 125 | 0 | 3 | 0 | **3** |
| 211 | U+00D3 | `Ó` | 126 | 0 | 5 | 0 | **5** |
| 212 | U+00D4 | `Ô` | 127 | 0 | 5 | 0 | **5** |
| 213 | U+00D5 | `Õ` | 128 | 0 | 5 | 0 | **5** |
| 214 | U+00D6 | `Ö` | 129 | 0 | 5 | 0 | **5** |
| 216 | U+00D8 | `Ø` | 130 | 0 | 5 | 0 | **5** |
| 219 | U+00DB | `Û` | 131 | 0 | 5 | 0 | **5** |
| 220 | U+00DC | `Ü` | 132 | 0 | 5 | 0 | **5** |
| 221 | U+00DD | `Ý` | 133 | 0 | 5 | 0 | **5** |
| 222 | U+00DE | `Þ` | 134 | 0 | 5 | 0 | **5** |
| 225 | U+00E1 | `á` | 135 | 0 | 5 | 0 | **5** |
| 226 | U+00E2 | `â` | 136 | 0 | 5 | 0 | **5** |
| 227 | U+00E3 | `ã` | 137 | 0 | 5 | 0 | **5** |
| 228 | U+00E4 | `ä` | 138 | 0 | 5 | 0 | **5** |
| 230 | U+00E6 | `æ` | 139 | 0 | 5 | 0 | **5** |
| 233 | U+00E9 | `é` | 140 | 0 | 5 | 0 | **5** |
| 234 | U+00EA | `ê` | 141 | 0 | 5 | 0 | **5** |
| 235 | U+00EB | `ë` | 142 | 0 | 5 | 0 | **5** |
| 236 | U+00EC | `ì` | 143 | 0 | 5 | 0 | **5** |
| 237 | U+00ED | `í` | 144 | 0 | 5 | 0 | **5** |
| 238 | U+00EE | `î` | 145 | 0 | 2 | 1 | **3** |
| 239 | U+00EF | `ï` | 146 | 1 | 2 | 0 | **3** |
| 240 | U+00F0 | `ð` | 147 | 0 | 3 | 0 | **3** |
| 241 | U+00F1 | `ñ` | 148 | 0 | 3 | 0 | **3** |
| 243 | U+00F3 | `ó` | 149 | 0 | 5 | 0 | **5** |
| 244 | U+00F4 | `ô` | 150 | 0 | 5 | 0 | **5** |
| 245 | U+00F5 | `õ` | 151 | 0 | 5 | 0 | **5** |
| 246 | U+00F6 | `ö` | 152 | 0 | 5 | 0 | **5** |
| 248 | U+00F8 | `ø` | 153 | 0 | 5 | 0 | **5** |
| 251 | U+00FB | `û` | 154 | 0 | 5 | 0 | **5** |
| 252 | U+00FC | `ü` | 155 | 0 | 5 | 0 | **5** |

> `fontq` é ideal para traduzir porque é quase fixa: 5 px para 90% dos caracteres. Apenas `.` `K` `a/b` `k/n` `Î` etc. são 2–3 px.

### 3.3 `font18.NFTR` — 14×15 (extra, não usada no Previewer)

Arquivo em `Fontes/font18.NFTR` — 236 glifos, célula 14×15, 27 bytes/glifo. CWDH `0–235`. Possui **4 CMAPs** (japonês Shift-JIS). Avanços variam **8–16 px**, mas a análise detalhada requer decodificar CMAP tipo 2 (sparse). Para tradução PT-BR, pode ser ignorada — o jogo ocidental usa `fontevent`/`fontq`.

---

## 4. Como calcular largura de uma linha (para quebra)

```python
# Exemplo mínimo — equivalente a nftr.py:124-132 + 115-122
import struct

def largura_texto(texto, nftr_path):
    with open(nftr_path, 'rb') as f:
        data = f.read()
    cwdh_off = data.find(b'HDWC')
    cmap_off = data.find(b'PAMC')
    cwdh_min = struct.unpack_from('<H', data, cwdh_off+8)[0]
    cmap_min = struct.unpack_from('<H', data, cmap_off+8)[0]
    # tabela CWDH
    cwdh = [(data[cwdh_off+16+i*3], data[cwdh_off+16+i*3+1], data[cwdh_off+16+i*3+2])
            for i in range(struct.unpack_from('<H', data, cwdh_off+10)[0]-cwdh_min+1)]
    # mapa
    cmap = [struct.unpack_from('<H', data, cmap_off+16+i*2)[0]
            for i in range(struct.unpack_from('<H', data, cmap_off+10)[0]-cmap_min+1)]
    total = 0
    for ch in texto:
        cp = ord(ch)
        if cmap_min <= cp <= cmap_min+len(cmap)-1:
            idx = cmap[cp - cmap_min]
            if idx != 0xFFFF:
                adv = cwdh[idx][2]  # total = adv
                total += adv
            else:
                total += 4  # fallback (espaço)
        else:
            total += 4
    return total

print(largura_texto("Olá, Layton!", "Previewer/Fontes/fontevent.nftr"))  #  ~ 73 px
print(largura_texto("Olá, Layton!", "Previewer/Fontes/fontq.nftr"))      #  ~ 50 px
```

**Limites práticos de caixa** (inferidos de `Previewer/Configs/*.ini` + `Previewer/Fundos/*.png`):

- `fontevent` com `ScreenXPos=9` em `Texts.png` (256 px largura) → área útil ≈ **238 px** → cabem **~33–34** caracteres médios (238/7 ≈ 34) por linha; `ScreenNewLine=16` px entre linhas (altura 12 + 4 de leading).
- `fontq` com `ScreenXPos=13` em `Puzzle.png` → área ≈ **230 px** → cabem **~46** caracteres médios (230/5 ≈ 46) por linha; `NewLine=12` px.

> Para PT-BR, prefira sinônimos curtos em `fontq` (enigmas) — 1 palavra extra pode estourar a caixa. Em `fontevent`, há ~10 px de folga por palavra longa.

---

## 5. Referências de código

- Leitura de header: `nftr.py:38-86`
- Desempacotamento 1bpp: `nftr.py:87-113` (`shift=[7,6,5,4,3,2,1,0]` + `zip(*[iter(letter)]*width)`)
- CMAP: `nftr.py:115-122`
- CWDH: `nftr.py:124-132`

Fontes alternativas em `Fontes/*.ttf` (`Layton Big.ttf`, `antic.regular.ttf` etc.) são reconstruções TTF para edição, não usadas em runtime — o jogo usa apenas os `.NFTR`.

---

*Gerado em 2026-09-11 a partir de `Previewer/Fontes/fontevent.nftr` (3228 bytes) e `fontq.nftr` (2440 bytes). Para recalcular, rode `python3` com o snippet da seção 4.*
