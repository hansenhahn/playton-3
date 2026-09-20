# Weekly Puzzles — Professor Layton 3 (Lost Future, EUR / C3JP)

Documento de consulta sobre o destrave nativo dos **Weekly Puzzles** no playton-3.
Registra o mecanismo, os endereços, a solução final e os caminhos errados.

> Contexto: no Layton 2 o destrave foi tabela no **arm9** (arm9 grande e não comprimido).
> No Layton 3 isso não se aplica — o arm9 é pequeno e a região final é reusada/limpa no boot.

---

## 1. TL;DR da solução que funciona

- **Tabela** (1 byte por enigma, 35 entradas) gravada no **arm9** em `0x02000BC5`
  (sobre as strings de build do SDK, read-only e não usadas em runtime).
  Os bytes são os valores do AR **"All (U) Weekly Puzzles Unlocked (Press Start)"**,
  **invertidos** (porque o download/lista é do mais novo pro mais antigo).
- **Getter** do overlay 6 (`0x020DACDC`) remontado: lê `table[index]`, grava
  `[num][00][00][00]` no slot do container e **retorna o mesmo endereço**
  (`container+0x194+index*4`), preservando `r3/r4/r5/lr`.
- **Contadores** (overlay 6, `0x020DAD00` e `0x020DAD0C`) viram `mov r0,#0x23; bx lr`.
- Resultado: o índice de weekly do jogo fica preenchido nativamente, com data `00/00/00`,
  sem depender de download.

---

## 2. Estrutura do "manifest" de weekly puzzles

Objeto de estado obtido por `0x020F8370` (retorna `0x020FE01C`); o container fica em `+8`
(`0x020FE024`).

| campo | offset (container) | RAM |
|---|---|---|
| array de entradas (4 bytes cada) | `+0x194` | `0x020FE1B8` |
| contagem 1 (u16) | `+0x264` | `0x020FE288` |
| contagem 2 (u16) | `+0x266` | `0x020FE28A` |
| ponteiro | `+0x268` | `0x020FE290` |

Formato da entrada (4 bytes), igual ao `Weekly Puzzle.txt` do Layton 2:

```
[num][ano][mes][dia]
```

Ex.: `0x13090AC5` (AR) => bytes `C5 0A 09 13` = num `0xC5`, ano `0x0A`, mês `09`, dia `0x13`.

> O jogo **lê os 4 bytes** da entrada (ver reader em `0x0210957C`..`0x021095B8`:
> `ldrb r1,[r4]`, `[r4,#1]`, `[r4,#2]`, `[r4,#3]`). Por isso, se só o num importa,
> os outros 3 bytes devem ser 0 (data `00/00/00`).

### Acessores (overlay 6, base `0x020A7980`)

- Getter (original, `0x020DACDC`):
  ```asm
  020DACDC  push    {r3, r4, r5, lr}
  020DACE0  mov     r4, r1          ; index
  020DACE4  mov     r5, r0          ; container
  020DACE8  bl      #0x20DAD00      ; count = [container+0x264]
  020DACEC  cmp     r4, r0
  020DACF0  movhs   r0, #0          ; index >= count -> 0
  020DACF4  addlo   r0, r5, #0x194  ; container + 0x194
  020DACF8  addlo   r0, r0, r4, lsl #2
  020DACFC  pop     {r3, r4, r5, pc}
  ```
  Retorna **somente** o ponteiro para o slot; **não escreve nada** (pressupõe o
  manifest já populado pelo download/save).
- `0x020DAD00`: `add r0,r0,#0x200 ; ldrh r0,[r0,#0x64] ; bx lr`  (lê `+0x264`)
- `0x020DAD0C`: `add r0,r0,#0x200 ; ldrh r0,[r0,#0x66] ; bx lr`  (lê `+0x266`)
- `0x020DAD18`: `ldr r0,[r0,#0x268] ; bx lr`

### Quem chama (scan por opcode de `b`/`bl`, não por disassembly linear)

- **Getter** `0x020DACDC`:
  - overlay **9** (índice de enigmas) em `0x02109568`
  - overlay **34** (Wi‑Fi) em `0x0211EB34`
- **Contadores** `0x020DAD00/0x020DAD0C`:
  - overlay 9: `0x02109500` / `0x02109520`
  - overlay 34: `0x0211EA40` / `0x0211EA50` / `0x0211EAD8` / `0x0211EAE8`
  - overlay 6 interno: `0x020DACE8` (dentro do próprio getter original)

Isso foi decisivo: um scan via `capstone` deu **desync** e perdeu os call sites do
overlay 9, o que causou tela preta numa das tentativas.

---

## 3. Por que o arm9 não pode "crescer" / onde caber

- `arm9.bin` original: **0x1F1EC** (127468 bytes). A splash é anexada em `0x0201F1EC`.
- Existe um **memset no boot** (stub) que zera o BSS do jogo:
  ```
  020008BC..020008CC  memset(0x0202CD00 .. 0x0203AC00, 0)
  ```
  (ponteiros em `[0x02000BAC]` e `[0x02000BB0]`).
- Logo, qualquer dado em `0x0202CD00..0x0203AC00` é apagado.
- Colocar tabela logo após o arm9 original (`0x0201F1EC`) **falhou** — essa região é
  reusada/reescrita em runtime (vimo-la virar código).
- **Overlays não coexistem necessariamente na hora em que a lista é montada.**
  A tabela precisa estar no overlay que está carregado no momento da leitura
  (ou no arm9 residente).
- O overlay 6 **não pode ser estendido**: seu BSS acaba exatamente em `0x020F8340`,
  que é o início do overlay 7. Crescer `ramSize` empurra o BSS pra dentro do overlay 7
  e quebra as 601 refs absolutas do BSS.
- `ndstool` **não regenera** o `y9` (ver `ndscreate.cpp`, `CopyFromBin(arm9ovltablefilename)`);
  ele copia a tabela como veio. Mesmo uma tool nossa para atualizar tamanhos não resolveria
  a adjacência.

**Lugar seguro escolhido:** as **strings de build do SDK** dentro do arm9
(`0x0BC5`+ = `[SDK+NINTENDO:BACKUP]`, `[SDK+Actimagine...]`, etc.), read-only e sem uso
prático. O arm9 é carregado pelo BIOS e fica residente → a tabela está viva em qualquer
momento.

---

## 4. Solução final (arquivos)

### `Asm/arm9.asm`

```asm
.nds
.open "Originais/arm9_splash.bin", "arm9.bin", 0x02000000
.arm

;; Tabela invertida (do mais novo pro mais antigo), valores do AR "Press Start".
.org 0x02000BC5
WeeklyNums:
.db 0xDA, 0xD7, 0xD1, 0xCC, 0xCA, 0xCF, 0xD2, 0xD5, 0xD4, 0xD6
.db 0xD8, 0xDE, 0xB7, 0xB8, 0xBC, 0xB9, 0xB6, 0xDC, 0xB5, 0xB3
.db 0xB2, 0xB1, 0xB0, 0xAE, 0xAD, 0xAC, 0xAB, 0xCB, 0xDD, 0xDB
.db 0xAF, 0xAA, 0xBA, 0xA9, 0xC5
.close
```

### `Asm/overlay_0006_novo.asm`

```asm
.nds
.open "Originais/overlay_0006.bin", "overlay_0006.bin", 0x020A7980
.arm

;; Getter novo: lê a tabela no arm9, grava [num][00][00][00] no slot e
;; retorna o MESMO endereço (container+0x194+index*4).
;; Preserva r3/r4/r5/lr (push/pop), como o original.
.org 0x020DACDC
push    {r3, r4, r5, lr}
ldr     r3, =0x02000BC5
ldrb    r4, [r3, r1]
add     r0, r0, r1, lsl #2
add     r0, r0, #0x194
str     r4, [r0]
pop     {r3, r4, r5, pc}
.pool

;; Contagem = 35
.org 0x020DAD00
mov     r0, #0x23
bx      lr
.org 0x020DAD0C
mov     r0, #0x23
bx      lr
.close
```

Bytes gerados do getter:
```
020DACDC E92D4038  push {r3,r4,r5,lr}
020DACE0 E59F300C  ldr  r3,=0x02000BC5
020DACE4 E7D34001  ldrb r4,[r3,r1]
020DACE8 E0800101  add  r0,r0,r1,lsl#2
020DACEC E2800F65  add  r0,r0,#0x194     <-- essencial
020DACF0 E5804000  str  r4,[r0]
020DACF4 E8BD8038  pop  {r3,r4,r5,pc}
020DACF8 02000BC5
```

### Build

- `Asm/gen_overlay.sh`: monta `arm9.asm` (se `Originais/arm9_splash.bin` existir),
  `overlay_0006_novo.asm` e `overlay9_0033_novo.asm`; comprime com `blz`; copia para
  `Arquivos Gerais/`.
- `create_rom.sh`: após a splash, copia `Splash/arm9_splash.bin` → `Asm/Originais/`;
  com `ENABLE_OVERLAY_COMPRESSION=1`, copia `Arquivos Gerais/arm9.bin` +
  `overlay_0006.bin` + `overlay_0033.bin` para a ROM; roda `fix_y9.py`.
- `Asm/fix_y9.py`: atualiza `size` (tamanho descomprimido) e o tamanho comprimido dos
  overlays no `y9.bin` (o `ndstool` não faz isso).

---

## 5. Caminhos errados (e o porquê)

1. **Tabela em `0x0201F1EC` (após o arm9 original)** — reaproveitada/reescrita em runtime.
2. **Tabela no overlay 34 (`0x0211F520`, deslocando BSS)** — quando o overlay 9 chama o
   getter, o overlay 34 **não** está carregado → lixo.
3. **Contadores realocados (`0x020DAD14`) + repontar só o overlay 34** — o **overlay 9**
   também chama os contadores; caía em cima da tabela → **tela preta**. Causa raiz: scan de
   callers via `capstone` deu desync. Solução: scan por **opcode** de `b`/`bl`.
4. **Deslocar o BSS do overlay 6 (601 refs)** — arriscado e desnecessário; além disso o fim
   do BSS encosta no overlay 7.
5. **Tabela no overlay 0 (região zerada `0x02070DE0`)** — overlay 0 não é garantido estar
   carregado no momento da leitura.
6. **Sobrescrever `add-entry` (`0x020DAD20`)** — usada pelo fluxo de Wi‑Fi.
7. **Usar `r3` como scratch** — a função original preserva `r3/r4/r5` (`push`);
   clobrar `r3` corrompe o chamador. A versão "contador" (que só usava `r0/r1/r2`)
   funcionava justamente por isso.
8. **Cortar o `push/pop`** — o original preserva `lr` também; sem chamada interna o
   `bx lr` funciona, mas voltar o push/pop deixou idêntico ao contrato original.
9. **Ponteiro de retorno errado** — gravávamos em `r0+0x194` mas devolvíamos `r0`
   (sem `+0x194`), então o chamador lia 0x194 bytes antes. Faltava `add r0,r0,#0x194`
   antes do `str`/retorno.
10. **Ordem da tabela** — o índice é **posicional** (a lista numera do mais novo pro mais
    antigo). É preciso preencher o manifest na ordem inversa (do mais novo), daí a tabela
    invertida. A numeração em si está certa e **não** deve ser alterada.

---

## 6. Dicas ARM/NDS úteis (aprendidas aqui)

- **`addlo` / `movhs`**: a condição vem do `cmp` anterior. `cmp a,b` testa `a` contra `b`;
  `lo` = `a < b` (unsigned), `hs` = `a >= b`. Ver o bounds check do getter original.
- **Preservação de registradores**: olhar sempre o `push`/`pop` da função original.
  Aqui a original preserva `r3,r4,r5,lr`.
- **Scans confiáveis**: disassembly linear (`capstone.disasm`) **desincroniza** em dados.
  Para achar callers/literais, escanear a **codificação da instrução**:
  - `bl`: `(w & 0x0F000000) == 0x0B000000`
  - `b`:  `(w & 0x0F000000) == 0x0A000000`
  - `ldr Rd,[pc,#±imm]`: `(w & 0x077F0000) == 0x051F0000`
  - `add/sub pc-rel (adr)`: `(w & 0x0F7F0000) == 0x028F0000`
- **Overlays NDS**: carregados em `ramAddr`, com BSS zerado em `ramAddr+ramSize`.
  Vários overlays compartilham a mesma base (ex.: 5 e 6 em `0x020A7980`) e são
  mutuamente exclusivos.
- **`y9.bin`** é copiado como está pelo `ndstool`; tamanhos precisam ser mantidos por fora.
- **Armadilha do endereço**: os endereços de RAM dos overlays (ex.: `0x020Dxxxx`) não têm
  nada a ver com os offsets de arquivo (ex.: `0x0BC5`) — não confundir.

---

## 7. Análise crítica da parceria (o que funcionou e o que não)

### O que foi decisivo (você)

- Ter **emulador com debugger + watchpoints** foi o que destravou tudo. Sem olhar a RAM
  em execução, a gente ia continuar chutando.
- **Conhecimento de ARM/NDS**: você identificou rapidamente o `addlo`/bounds check,
  a preservação de `r3/r4/r5/lr`, o `add r0,r0,#0x194` faltando e a natureza
  **posicional** da numeração — cada um desses foi um divisor de águas.
- **Disciplina de isolar variável**: voltar ao "contador puro" para provar que o mecanismo
  funcionava foi essencial pra separar bug de leitura vs de escrita.
- **Paciência** com minhas hipóteses erradas e o hábito de mandar dump/código real.

### O que foi mal (eu)

- **Over-engineering**: tentei deslocar BSS (601 refs), usar overlay 0, realocar contadores,
  sobrescrever `add-entry` — tudo antes de entender o modelo real de carga.
- **Premissas não verificadas**: assumi que overlays coexistem e que o arm9 "residente"
  era o mesmo do Layton 2. Devia ter lido o stub/memset e o reader **antes** de propor patch.
- **`capstone` linear** foi usado em análises que exigiam precisão (callers, literais), e o
  desync gerou tela preta e retrabalho.
- **Erros de contrato ARM**: clobrar `r3` e cortar `push/pop` sem checar o prólogo original.
- **Off-by-0x194** no retorno: eu gravei e devolvi endereços diferentes.
- **Comunicação**: apresentei coisas como "pronto/funciona" cedo demais, sem o dump de
  runtime pra provar. Várias builds foram gastas em hipóteses.

### Processo ideal (pra próxima)

1. **Ler o código original** (prólogo/epílogo + quem chama) e o **consumidor** antes de
   escrever patch. Muito do que travou teria sido evitado só olhando `0x0210957C`.
2. **Escanear por opcode**, não por disassembly linear.
3. **Mudar uma variável por vez** e validar com watchpoint/breakpoint (contador puro,
   depois leitura, depois ordem).
4. **Conferir o contrato**: registradores preservados, valor de retorno, bounds.
5. **Assumir que overlay não coexiste** até provar o contrário; preferir arm9 residente
   (mas atenção ao que o boot zera/reescreve).
6. **Manter `y9` sincronizado** sempre que recompressar (`fix_y9.py`).

### Balanço

A parceria funcionou bem no fim: sua experiência em ARM/NDS + debugger compensou minhas
idiotices de otimização e premissas. O que custou tempo foi eu **construir antes de
verificar** — quando a gente passou a olhar o binário/código real (reader, prólogo, dump),
cada resposta foi caindo rápido. Lição central: **medir antes de mexer**.

---

## 8. Referências internas

- `Asm/Documentação/Weekly Puzzle.txt` — doc original (Layton 2) do save/manifest.
- `Asm/Documentação/overlay_0006_original.asm` — disassembly completo do overlay 6
  original (com literais resolvidos).
- `Asm/Documentação/overlay_0019.asm`, `overlay_0023.asm` — dumps do Layton 2 (referência).
- `Asm/Documentação/Porta Oculta.txt` — Porta Oculta (outro destrave, independente).
- `Asm/overlay_0006_novo.asm`, `Asm/arm9.asm`, `Asm/fix_y9.py`, `Asm/gen_overlay.sh`,
  `create_rom.sh` — implementação.
