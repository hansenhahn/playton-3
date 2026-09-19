.nds

.open "Originais/overlay_0006.bin", "overlay_0006.bin", 0x020A7980

.arm                                                    ; ARM code

;; Getter: monta a entrada a partir da tabela no arm9 e retorna o ponteiro
;; container+0x194+index*4 (igual ao original).
;; Preserva r3/r4/r5/lr (push/pop).
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
