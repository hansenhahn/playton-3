
.nds

.open "Originais\overlay9_0033.bin", "overlay_0033.bin", 0x0211dae0

.arm                                                    ; ARM code

.org 0x0211F3D8
 add     r1,r13,20h ;; Carrega o endereço de r0 em r1

;; Código original
;0211F3D4 E28D0020 add     r0,r13,20h                              ;1  207
;0211F3D8 E28D100C add     r1,r13,0Ch                              ;1  208           ;
;0211F3DC EBFC6F75 bl      Lxx_203B1B8h                            ;3  211           ; os endereços que serão comparados

.close