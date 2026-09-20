#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Atualiza o y9.bin a partir dos overlays reais:
 - size (ramSize) = tamanho DESCOMPRIMIDO do overlay
 - tamanho comprimido (24 bits do campo reserved) = tamanho do arquivo
Preserva a flag de compressao (bit 0x01000000) e os demais campos.

Uso: fix_y9.py <y9.bin> <dir_overlay>
"""
import os
import struct
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Programas3"))
from rhCompression import blz


def main():
    if len(sys.argv) < 3:
        print("uso: fix_y9.py <y9.bin> <dir_overlay>")
        return 1
    y9_path, ov_dir = sys.argv[1], sys.argv[2]
    d = bytearray(open(y9_path, "rb").read())
    changed = []
    for i in range(len(d) // 32):
        e = struct.unpack_from("<8I", d, i * 32)
        oid, old_size, res = e[0], e[2], e[7]
        path = os.path.join(ov_dir, "overlay_%04d.bin" % oid)
        if not os.path.exists(path):
            continue
        raw = open(path, "rb").read()
        comp = bool(res & 0x01000000)
        if comp:
            try:
                size = len(blz.decompress(raw))
            except Exception:
                size = old_size
        else:
            size = len(raw)
        new_res = (res & 0xFF000000) | (len(raw) & 0xFFFFFF)
        if size != old_size:
            struct.pack_into("<I", d, i * 32 + 8, size)
        if new_res != res:
            struct.pack_into("<I", d, i * 32 + 28, new_res)
        if size != old_size or new_res != res:
            changed.append((oid, old_size, size, res & 0xFFFFFF, len(raw)))
    open(y9_path, "wb").write(d)
    if changed:
        for oid, osz, nsz, ocs, ncs in changed:
            print("y9 overlay_%04d: size %d->%d csize %d->%d" % (oid, osz, nsz, ocs, ncs))
    else:
        print("y9: nada a ajustar")
    return 0


if __name__ == "__main__":
    sys.exit(main())
