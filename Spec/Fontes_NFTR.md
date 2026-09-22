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
| 32 | U+0020 | ` ` | 0 | 3 | 0 | 0 | **3** |
| 33 | U+0021 | `!` | 1 | 1 | 1 | 1 | **3** |
| 34 | U+0022 | `"` | 2 | 1 | 3 | 1 | **5** |
| 35 | U+0023 | `#` | 3 | 1 | 5 | 1 | **7** |
| 36 | U+0024 | `$` | 4 | 1 | 5 | 1 | **7** |
| 37 | U+0025 | `%` | 5 | 1 | 7 | 1 | **9** |
| 38 | U+0026 | `&` | 6 | 1 | 6 | 1 | **8** |
| 39 | U+0027 | `'` | 7 | 1 | 2 | 1 | **4** |
| 40 | U+0028 | `(` | 8 | 1 | 3 | 1 | **5** |
| 41 | U+0029 | `)` | 9 | 1 | 3 | 1 | **5** |
| 42 | U+002A | `*` | 10 | 1 | 5 | 1 | **7** |
| 43 | U+002B | `+` | 11 | 1 | 5 | 1 | **7** |
| 44 | U+002C | `,` | 12 | 1 | 2 | 1 | **4** |
| 45 | U+002D | `-` | 13 | 1 | 5 | 1 | **7** |
| 46 | U+002E | `.` | 14 | 1 | 2 | 1 | **4** |
| 47 | U+002F | `/` | 15 | 1 | 3 | 1 | **5** |
| 48 | U+0030 | `0` | 16 | 0 | 6 | 0 | **6** |
| 49 | U+0031 | `1` | 17 | 1 | 3 | 0 | **4** |
| 50 | U+0032 | `2` | 18 | 0 | 6 | 0 | **6** |
| 51 | U+0033 | `3` | 19 | 0 | 6 | 0 | **6** |
| 52 | U+0034 | `4` | 20 | 0 | 6 | 0 | **6** |
| 53 | U+0035 | `5` | 21 | 0 | 6 | 0 | **6** |
| 54 | U+0036 | `6` | 22 | 0 | 6 | 0 | **6** |
| 55 | U+0037 | `7` | 23 | 0 | 6 | 0 | **6** |
| 56 | U+0038 | `8` | 24 | 0 | 6 | 0 | **6** |
| 57 | U+0039 | `9` | 25 | 0 | 6 | 0 | **6** |
| 58 | U+003A | `:` | 26 | 1 | 2 | 1 | **4** |
| 59 | U+003B | `;` | 27 | 1 | 2 | 1 | **4** |
| 61 | U+003D | `=` | 28 | 1 | 5 | 1 | **7** |
| 63 | U+003F | `?` | 29 | 1 | 7 | 1 | **9** |
| 64 | U+0040 | `@` | 30 | 0 | 8 | 0 | **8** |
| 65 | U+0041 | `A` | 31 | 0 | 7 | 0 | **7** |
| 66 | U+0042 | `B` | 32 | 0 | 7 | 0 | **7** |
| 67 | U+0043 | `C` | 33 | 0 | 7 | 0 | **7** |
| 68 | U+0044 | `D` | 34 | 0 | 7 | 0 | **7** |
| 69 | U+0045 | `E` | 35 | 0 | 7 | 0 | **7** |
| 70 | U+0046 | `F` | 36 | 0 | 7 | 0 | **7** |
| 71 | U+0047 | `G` | 37 | 0 | 7 | 0 | **7** |
| 72 | U+0048 | `H` | 38 | 0 | 7 | 0 | **7** |
| 73 | U+0049 | `I` | 39 | 1 | 3 | 1 | **5** |
| 74 | U+004A | `J` | 40 | 0 | 7 | 0 | **7** |
| 75 | U+004B | `K` | 41 | 0 | 7 | 0 | **7** |
| 76 | U+004C | `L` | 42 | 0 | 6 | 0 | **6** |
| 77 | U+004D | `M` | 43 | 0 | 7 | 0 | **7** |
| 78 | U+004E | `N` | 44 | 0 | 7 | 0 | **7** |
| 79 | U+004F | `O` | 45 | 0 | 8 | 0 | **8** |
| 80 | U+0050 | `P` | 46 | 0 | 7 | 0 | **7** |
| 81 | U+0051 | `Q` | 47 | 0 | 8 | 0 | **8** |
| 82 | U+0052 | `R` | 48 | 0 | 7 | 0 | **7** |
| 83 | U+0053 | `S` | 49 | 0 | 7 | 0 | **7** |
| 84 | U+0054 | `T` | 50 | 0 | 7 | 0 | **7** |
| 85 | U+0055 | `U` | 51 | 0 | 7 | 0 | **7** |
| 86 | U+0056 | `V` | 52 | 0 | 7 | 0 | **7** |
| 87 | U+0057 | `W` | 53 | 0 | 7 | 0 | **7** |
| 88 | U+0058 | `X` | 54 | 0 | 7 | 0 | **7** |
| 89 | U+0059 | `Y` | 55 | 0 | 7 | 0 | **7** |
| 90 | U+005A | `Z` | 56 | 0 | 7 | 0 | **7** |
| 91 | U+005B | `[` | 57 | 1 | 3 | 1 | **5** |
| 92 | U+005C | `\` | 58 | 1 | 3 | 1 | **5** |
| 93 | U+005D | `]` | 59 | 1 | 3 | 1 | **5** |
| 94 | U+005E | `^` | 60 | 1 | 5 | 1 | **7** |
| 95 | U+005F | `_` | 61 | 0 | 5 | 0 | **5** |
| 97 | U+0061 | `a` | 62 | 0 | 6 | 0 | **6** |
| 98 | U+0062 | `b` | 63 | 0 | 5 | 0 | **5** |
| 99 | U+0063 | `c` | 64 | 0 | 5 | 0 | **5** |
| 100 | U+0064 | `d` | 65 | 0 | 5 | 0 | **5** |
| 101 | U+0065 | `e` | 66 | 0 | 5 | 0 | **5** |
| 102 | U+0066 | `f` | 67 | 0 | 5 | 0 | **5** |
| 103 | U+0067 | `g` | 68 | 0 | 5 | 0 | **5** |
| 104 | U+0068 | `h` | 69 | 0 | 5 | 0 | **5** |
| 105 | U+0069 | `i` | 70 | 1 | 1 | 1 | **3** |
| 106 | U+006A | `j` | 71 | 0 | 5 | 0 | **5** |
| 107 | U+006B | `k` | 72 | 0 | 5 | 0 | **5** |
| 108 | U+006C | `l` | 73 | 1 | 1 | 1 | **3** |
| 109 | U+006D | `m` | 74 | 0 | 7 | 0 | **7** |
| 110 | U+006E | `n` | 75 | 0 | 5 | 0 | **5** |
| 111 | U+006F | `o` | 76 | 0 | 6 | 0 | **6** |
| 112 | U+0070 | `p` | 77 | 0 | 5 | 0 | **5** |
| 113 | U+0071 | `q` | 78 | 0 | 5 | 0 | **5** |
| 114 | U+0072 | `r` | 79 | 0 | 5 | 0 | **5** |
| 115 | U+0073 | `s` | 80 | 0 | 5 | 0 | **5** |
| 116 | U+0074 | `t` | 81 | 0 | 5 | 0 | **5** |
| 117 | U+0075 | `u` | 82 | 0 | 5 | 0 | **5** |
| 118 | U+0076 | `v` | 83 | 0 | 6 | 0 | **6** |
| 119 | U+0077 | `w` | 84 | 0 | 7 | 0 | **7** |
| 120 | U+0078 | `x` | 85 | 0 | 6 | 0 | **6** |
| 121 | U+0079 | `y` | 86 | 1 | 5 | 1 | **7** |
| 122 | U+007A | `z` | 87 | 0 | 5 | 0 | **5** |
| 128 | U+0080 | U+0080 | 88 | 0 | 7 | 0 | **7** |
| 130 | U+0082 | U+0082 | 89 | 1 | 2 | 1 | **4** |
| 132 | U+0084 | U+0084 | 90 | 1 | 3 | 1 | **5** |
| 139 | U+008B | U+008B | 91 | 1 | 3 | 1 | **5** |
| 140 | U+008C | U+008C | 92 | 0 | 9 | 0 | **9** |
| 145 | U+0091 | U+0091 | 93 | 1 | 2 | 1 | **4** |
| 146 | U+0092 | U+0092 | 94 | 1 | 2 | 1 | **4** |
| 147 | U+0093 | U+0093 | 95 | 1 | 3 | 1 | **5** |
| 148 | U+0094 | U+0094 | 96 | 1 | 3 | 1 | **5** |
| 155 | U+009B | U+009B | 97 | 1 | 3 | 1 | **5** |
| 156 | U+009C | U+009C | 98 | 0 | 9 | 0 | **9** |
| 161 | U+00A1 | `¡` | 99 | 1 | 1 | 1 | **3** |
| 163 | U+00A3 | `£` | 100 | 0 | 7 | 0 | **7** |
| 170 | U+00AA | `ª` | 101 | 1 | 5 | 1 | **7** |
| 171 | U+00AB | `«` | 102 | 1 | 5 | 1 | **7** |
| 172 | U+00AC | `¬` | 103 | 1 | 5 | 1 | **7** |
| 173 | U+00AD | U+00AD | 104 | 1 | 5 | 1 | **7** |
| 174 | U+00AE | `®` | 105 | 1 | 5 | 1 | **7** |
| 175 | U+00AF | `¯` | 106 | 1 | 5 | 1 | **7** |
| 176 | U+00B0 | `°` | 107 | 1 | 3 | 1 | **5** |
| 186 | U+00BA | `º` | 108 | 1 | 5 | 1 | **7** |
| 187 | U+00BB | `»` | 109 | 1 | 5 | 1 | **7** |
| 191 | U+00BF | `¿` | 110 | 1 | 7 | 1 | **9** |
| 192 | U+00C0 | `À` | 111 | 0 | 7 | 0 | **7** |
| 193 | U+00C1 | `Á` | 112 | 0 | 7 | 0 | **7** |
| 194 | U+00C2 | `Â` | 113 | 0 | 7 | 0 | **7** |
| 195 | U+00C3 | `Ã` | 114 | 0 | 7 | 0 | **7** |
| 196 | U+00C4 | `Ä` | 115 | 0 | 7 | 0 | **7** |
| 197 | U+00C5 | `Å` | 116 | 0 | 7 | 0 | **7** |
| 199 | U+00C7 | `Ç` | 117 | 0 | 7 | 0 | **7** |
| 200 | U+00C8 | `È` | 118 | 0 | 7 | 0 | **7** |
| 201 | U+00C9 | `É` | 119 | 0 | 7 | 0 | **7** |
| 202 | U+00CA | `Ê` | 120 | 0 | 7 | 0 | **7** |
| 203 | U+00CB | `Ë` | 121 | 0 | 7 | 0 | **7** |
| 204 | U+00CC | `Ì` | 122 | 0 | 2 | 2 | **4** |
| 205 | U+00CD | `Í` | 123 | 2 | 2 | 0 | **4** |
| 206 | U+00CE | `Î` | 124 | 1 | 3 | 1 | **5** |
| 207 | U+00CF | `Ï` | 125 | 1 | 3 | 1 | **5** |
| 209 | U+00D1 | `Ñ` | 126 | 0 | 7 | 0 | **7** |
| 210 | U+00D2 | `Ò` | 127 | 0 | 7 | 0 | **7** |
| 211 | U+00D3 | `Ó` | 128 | 0 | 7 | 0 | **7** |
| 212 | U+00D4 | `Ô` | 129 | 0 | 7 | 0 | **7** |
| 214 | U+00D6 | `Ö` | 130 | 0 | 7 | 0 | **7** |
| 217 | U+00D9 | `Ù` | 131 | 0 | 7 | 0 | **7** |
| 218 | U+00DA | `Ú` | 132 | 0 | 7 | 0 | **7** |
| 219 | U+00DB | `Û` | 133 | 0 | 7 | 0 | **7** |
| 220 | U+00DC | `Ü` | 134 | 0 | 7 | 0 | **7** |
| 223 | U+00DF | `ß` | 135 | 0 | 7 | 0 | **7** |
| 224 | U+00E0 | `à` | 136 | 0 | 6 | 0 | **6** |
| 225 | U+00E1 | `á` | 137 | 0 | 6 | 0 | **6** |
| 226 | U+00E2 | `â` | 138 | 0 | 7 | 0 | **7** |
| 227 | U+00E3 | `ã` | 139 | 0 | 6 | 0 | **6** |
| 231 | U+00E7 | `ç` | 140 | 0 | 6 | 0 | **6** |
| 232 | U+00E8 | `è` | 141 | 0 | 6 | 0 | **6** |
| 233 | U+00E9 | `é` | 142 | 0 | 6 | 0 | **6** |
| 234 | U+00EA | `ê` | 143 | 0 | 6 | 0 | **6** |
| 235 | U+00EB | `ë` | 144 | 0 | 6 | 0 | **6** |
| 236 | U+00EC | `ì` | 145 | 0 | 2 | 2 | **4** |
| 237 | U+00ED | `í` | 146 | 2 | 2 | 0 | **4** |
| 238 | U+00EE | `î` | 147 | 1 | 3 | 1 | **5** |
| 239 | U+00EF | `ï` | 148 | 1 | 3 | 1 | **5** |
| 241 | U+00F1 | `ñ` | 149 | 0 | 6 | 0 | **6** |
| 242 | U+00F2 | `ò` | 150 | 0 | 6 | 0 | **6** |
| 243 | U+00F3 | `ó` | 151 | 0 | 6 | 0 | **6** |
| 244 | U+00F4 | `ô` | 152 | 0 | 6 | 0 | **6** |
| 245 | U+00F5 | `õ` | 153 | 0 | 6 | 0 | **6** |
| 249 | U+00F9 | `ù` | 154 | 0 | 6 | 0 | **6** |
| 250 | U+00FA | `ú` | 155 | 0 | 6 | 0 | **6** |
| 251 | U+00FB | `û` | 156 | 0 | 6 | 0 | **6** |
| 252 | U+00FC | `ü` | 157 | 0 | 6 | 0 | **6** |

> Observação: `U+0020` (espaço) tem `W=0` — é um avanço puramente vazio (4 px). `k` e `n` são os únicos minúsculos estreitos (4 px) nesta fonte; `A` é a mais larga (10 px).

### 3.2 `fontq.nftr` — 7×10 — Enigmas / Perfis / Nomes / Dicas (158 glifos)

Média: **4,70 px** — mín 2 px, máx 7 px. Quase monoespaçada.

| CP | Hex | Char | Idx | L | W | R | Total |
|---|---|---|---|---|---|---|---|
| 32 | U+0020 | ` ` | 0 | 3 | 0 | 0 | **3** |
| 33 | U+0021 | `!` | 1 | 1 | 1 | 1 | **3** |
| 34 | U+0022 | `"` | 2 | 1 | 3 | 0 | **4** |
| 35 | U+0023 | `#` | 3 | 0 | 5 | 0 | **5** |
| 36 | U+0024 | `$` | 4 | 0 | 5 | 0 | **5** |
| 37 | U+0025 | `%` | 5 | 0 | 4 | 0 | **4** |
| 38 | U+0026 | `&` | 6 | 0 | 5 | 0 | **5** |
| 39 | U+0027 | `'` | 7 | 1 | 2 | 1 | **4** |
| 40 | U+0028 | `(` | 8 | 0 | 3 | 1 | **4** |
| 41 | U+0029 | `)` | 9 | 1 | 3 | 0 | **4** |
| 42 | U+002A | `*` | 10 | 0 | 5 | 0 | **5** |
| 43 | U+002B | `+` | 11 | 0 | 5 | 0 | **5** |
| 44 | U+002C | `,` | 12 | 0 | 2 | 0 | **2** |
| 45 | U+002D | `-` | 13 | 0 | 5 | 0 | **5** |
| 46 | U+002E | `.` | 14 | 0 | 2 | 0 | **2** |
| 47 | U+002F | `/` | 15 | 0 | 3 | 0 | **3** |
| 48 | U+0030 | `0` | 16 | 0 | 5 | 0 | **5** |
| 49 | U+0031 | `1` | 17 | 1 | 3 | 0 | **4** |
| 50 | U+0032 | `2` | 18 | 0 | 5 | 0 | **5** |
| 51 | U+0033 | `3` | 19 | 0 | 5 | 0 | **5** |
| 52 | U+0034 | `4` | 20 | 0 | 5 | 0 | **5** |
| 53 | U+0035 | `5` | 21 | 0 | 5 | 0 | **5** |
| 54 | U+0036 | `6` | 22 | 0 | 5 | 0 | **5** |
| 55 | U+0037 | `7` | 23 | 0 | 5 | 0 | **5** |
| 56 | U+0038 | `8` | 24 | 0 | 5 | 0 | **5** |
| 57 | U+0039 | `9` | 25 | 0 | 5 | 0 | **5** |
| 58 | U+003A | `:` | 26 | 0 | 2 | 0 | **2** |
| 59 | U+003B | `;` | 27 | 0 | 2 | 0 | **2** |
| 61 | U+003D | `=` | 28 | 0 | 5 | 0 | **5** |
| 63 | U+003F | `?` | 29 | 0 | 5 | 0 | **5** |
| 64 | U+0040 | `@` | 30 | 0 | 5 | 0 | **5** |
| 65 | U+0041 | `A` | 31 | 0 | 5 | 0 | **5** |
| 66 | U+0042 | `B` | 32 | 0 | 5 | 0 | **5** |
| 67 | U+0043 | `C` | 33 | 0 | 5 | 0 | **5** |
| 68 | U+0044 | `D` | 34 | 0 | 5 | 0 | **5** |
| 69 | U+0045 | `E` | 35 | 0 | 5 | 0 | **5** |
| 70 | U+0046 | `F` | 36 | 0 | 5 | 0 | **5** |
| 71 | U+0047 | `G` | 37 | 0 | 5 | 0 | **5** |
| 72 | U+0048 | `H` | 38 | 0 | 5 | 0 | **5** |
| 73 | U+0049 | `I` | 39 | 0 | 3 | 0 | **3** |
| 74 | U+004A | `J` | 40 | 0 | 5 | 0 | **5** |
| 75 | U+004B | `K` | 41 | 0 | 5 | 0 | **5** |
| 76 | U+004C | `L` | 42 | 0 | 5 | 0 | **5** |
| 77 | U+004D | `M` | 43 | 0 | 5 | 0 | **5** |
| 78 | U+004E | `N` | 44 | 0 | 5 | 0 | **5** |
| 79 | U+004F | `O` | 45 | 0 | 5 | 0 | **5** |
| 80 | U+0050 | `P` | 46 | 0 | 5 | 0 | **5** |
| 81 | U+0051 | `Q` | 47 | 0 | 5 | 0 | **5** |
| 82 | U+0052 | `R` | 48 | 0 | 5 | 0 | **5** |
| 83 | U+0053 | `S` | 49 | 0 | 5 | 0 | **5** |
| 84 | U+0054 | `T` | 50 | 0 | 5 | 0 | **5** |
| 85 | U+0055 | `U` | 51 | 0 | 5 | 0 | **5** |
| 86 | U+0056 | `V` | 52 | 0 | 5 | 0 | **5** |
| 87 | U+0057 | `W` | 53 | 0 | 5 | 0 | **5** |
| 88 | U+0058 | `X` | 54 | 0 | 5 | 0 | **5** |
| 89 | U+0059 | `Y` | 55 | 0 | 5 | 0 | **5** |
| 90 | U+005A | `Z` | 56 | 0 | 5 | 0 | **5** |
| 91 | U+005B | `[` | 57 | 0 | 3 | 1 | **4** |
| 93 | U+005D | `]` | 58 | 1 | 3 | 0 | **4** |
| 94 | U+005E | `^` | 59 | 0 | 5 | 0 | **5** |
| 95 | U+005F | `_` | 60 | 0 | 3 | 0 | **3** |
| 96 | U+0060 | ``` | 61 | 0 | 3 | 0 | **3** |
| 97 | U+0061 | `a` | 62 | 0 | 5 | 0 | **5** |
| 98 | U+0062 | `b` | 63 | 0 | 5 | 0 | **5** |
| 99 | U+0063 | `c` | 64 | 0 | 5 | 0 | **5** |
| 100 | U+0064 | `d` | 65 | 0 | 5 | 0 | **5** |
| 101 | U+0065 | `e` | 66 | 0 | 5 | 0 | **5** |
| 102 | U+0066 | `f` | 67 | 0 | 5 | 0 | **5** |
| 103 | U+0067 | `g` | 68 | 0 | 5 | 0 | **5** |
| 104 | U+0068 | `h` | 69 | 0 | 5 | 0 | **5** |
| 105 | U+0069 | `i` | 70 | 1 | 1 | 0 | **2** |
| 106 | U+006A | `j` | 71 | 0 | 5 | 0 | **5** |
| 107 | U+006B | `k` | 72 | 0 | 5 | 0 | **5** |
| 108 | U+006C | `l` | 73 | 1 | 1 | 0 | **2** |
| 109 | U+006D | `m` | 74 | 0 | 5 | 0 | **5** |
| 110 | U+006E | `n` | 75 | 0 | 5 | 0 | **5** |
| 111 | U+006F | `o` | 76 | 0 | 5 | 0 | **5** |
| 112 | U+0070 | `p` | 77 | 0 | 5 | 0 | **5** |
| 113 | U+0071 | `q` | 78 | 0 | 5 | 0 | **5** |
| 114 | U+0072 | `r` | 79 | 0 | 5 | 0 | **5** |
| 115 | U+0073 | `s` | 80 | 0 | 5 | 0 | **5** |
| 116 | U+0074 | `t` | 81 | 0 | 5 | 0 | **5** |
| 117 | U+0075 | `u` | 82 | 0 | 5 | 0 | **5** |
| 118 | U+0076 | `v` | 83 | 0 | 5 | 0 | **5** |
| 119 | U+0077 | `w` | 84 | 0 | 5 | 0 | **5** |
| 120 | U+0078 | `x` | 85 | 0 | 5 | 0 | **5** |
| 121 | U+0079 | `y` | 86 | 0 | 5 | 0 | **5** |
| 122 | U+007A | `z` | 87 | 0 | 5 | 0 | **5** |
| 128 | U+0080 | U+0080 | 88 | 0 | 5 | 0 | **5** |
| 130 | U+0082 | U+0082 | 89 | 0 | 2 | 0 | **2** |
| 132 | U+0084 | U+0084 | 90 | 0 | 3 | 0 | **3** |
| 139 | U+008B | U+008B | 91 | 0 | 2 | 0 | **2** |
| 140 | U+008C | U+008C | 92 | 0 | 7 | 0 | **7** |
| 145 | U+0091 | U+0091 | 93 | 1 | 2 | 1 | **4** |
| 146 | U+0092 | U+0092 | 94 | 1 | 2 | 1 | **4** |
| 147 | U+0093 | U+0093 | 95 | 1 | 3 | 1 | **5** |
| 148 | U+0094 | U+0094 | 96 | 1 | 3 | 1 | **5** |
| 155 | U+009B | U+009B | 97 | 0 | 2 | 0 | **2** |
| 156 | U+009C | U+009C | 98 | 0 | 7 | 0 | **7** |
| 161 | U+00A1 | `¡` | 99 | 1 | 1 | 1 | **3** |
| 163 | U+00A3 | `£` | 100 | 0 | 5 | 0 | **5** |
| 170 | U+00AA | `ª` | 101 | 0 | 5 | 0 | **5** |
| 171 | U+00AB | `«` | 102 | 0 | 4 | 0 | **4** |
| 172 | U+00AC | `¬` | 103 | 0 | 5 | 0 | **5** |
| 173 | U+00AD | U+00AD | 104 | 0 | 4 | 0 | **4** |
| 174 | U+00AE | `®` | 105 | 0 | 4 | 0 | **4** |
| 175 | U+00AF | `¯` | 106 | 0 | 4 | 0 | **4** |
| 176 | U+00B0 | `°` | 107 | 0 | 3 | 0 | **3** |
| 186 | U+00BA | `º` | 108 | 0 | 5 | 0 | **5** |
| 187 | U+00BB | `»` | 109 | 0 | 4 | 0 | **4** |
| 191 | U+00BF | `¿` | 110 | 0 | 5 | 0 | **5** |
| 192 | U+00C0 | `À` | 111 | 0 | 5 | 0 | **5** |
| 193 | U+00C1 | `Á` | 112 | 0 | 5 | 0 | **5** |
| 194 | U+00C2 | `Â` | 113 | 0 | 5 | 0 | **5** |
| 195 | U+00C3 | `Ã` | 114 | 0 | 5 | 0 | **5** |
| 196 | U+00C4 | `Ä` | 115 | 0 | 5 | 0 | **5** |
| 197 | U+00C5 | `Å` | 116 | 0 | 5 | 0 | **5** |
| 199 | U+00C7 | `Ç` | 117 | 0 | 5 | 0 | **5** |
| 200 | U+00C8 | `È` | 118 | 0 | 5 | 0 | **5** |
| 201 | U+00C9 | `É` | 119 | 0 | 5 | 0 | **5** |
| 202 | U+00CA | `Ê` | 120 | 0 | 5 | 0 | **5** |
| 203 | U+00CB | `Ë` | 121 | 0 | 5 | 0 | **5** |
| 204 | U+00CC | `Ì` | 122 | 0 | 2 | 1 | **3** |
| 205 | U+00CD | `Í` | 123 | 1 | 2 | 0 | **3** |
| 206 | U+00CE | `Î` | 124 | 0 | 3 | 0 | **3** |
| 207 | U+00CF | `Ï` | 125 | 0 | 3 | 0 | **3** |
| 209 | U+00D1 | `Ñ` | 126 | 0 | 5 | 0 | **5** |
| 210 | U+00D2 | `Ò` | 127 | 0 | 5 | 0 | **5** |
| 211 | U+00D3 | `Ó` | 128 | 0 | 5 | 0 | **5** |
| 212 | U+00D4 | `Ô` | 129 | 0 | 5 | 0 | **5** |
| 214 | U+00D6 | `Ö` | 130 | 0 | 5 | 0 | **5** |
| 217 | U+00D9 | `Ù` | 131 | 0 | 5 | 0 | **5** |
| 218 | U+00DA | `Ú` | 132 | 0 | 5 | 0 | **5** |
| 219 | U+00DB | `Û` | 133 | 0 | 5 | 0 | **5** |
| 220 | U+00DC | `Ü` | 134 | 0 | 5 | 0 | **5** |
| 223 | U+00DF | `ß` | 135 | 0 | 5 | 0 | **5** |
| 224 | U+00E0 | `à` | 136 | 0 | 5 | 0 | **5** |
| 225 | U+00E1 | `á` | 137 | 0 | 5 | 0 | **5** |
| 226 | U+00E2 | `â` | 138 | 0 | 5 | 0 | **5** |
| 227 | U+00E3 | `ã` | 139 | 0 | 5 | 0 | **5** |
| 231 | U+00E7 | `ç` | 140 | 0 | 5 | 0 | **5** |
| 232 | U+00E8 | `è` | 141 | 0 | 5 | 0 | **5** |
| 233 | U+00E9 | `é` | 142 | 0 | 5 | 0 | **5** |
| 234 | U+00EA | `ê` | 143 | 0 | 5 | 0 | **5** |
| 235 | U+00EB | `ë` | 144 | 0 | 5 | 0 | **5** |
| 236 | U+00EC | `ì` | 145 | 0 | 2 | 1 | **3** |
| 237 | U+00ED | `í` | 146 | 1 | 2 | 0 | **3** |
| 238 | U+00EE | `î` | 147 | 0 | 3 | 0 | **3** |
| 239 | U+00EF | `ï` | 148 | 0 | 3 | 0 | **3** |
| 241 | U+00F1 | `ñ` | 149 | 0 | 5 | 0 | **5** |
| 242 | U+00F2 | `ò` | 150 | 0 | 5 | 0 | **5** |
| 243 | U+00F3 | `ó` | 151 | 0 | 5 | 0 | **5** |
| 244 | U+00F4 | `ô` | 152 | 0 | 5 | 0 | **5** |
| 245 | U+00F5 | `õ` | 153 | 0 | 5 | 0 | **5** |
| 249 | U+00F9 | `ù` | 154 | 0 | 5 | 0 | **5** |
| 250 | U+00FA | `ú` | 155 | 0 | 5 | 0 | **5** |
| 251 | U+00FB | `û` | 156 | 0 | 5 | 0 | **5** |
| 252 | U+00FC | `ü` | 157 | 0 | 5 | 0 | **5** |

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
    cmap = [struct.unpack_from('<H', data, cmap_off+20+i*2)[0]
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
