#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Caydanlik Kaynama Sesi Orkestratoru
-----------------------------------
Bu yazilim, ev tipi bir caydanligin kaynama anini
bir oda orkestrasi gibi yonetir. Gercek buhar uretmez.
Sadece gurultu ve resmiyet uretir.
"""

import time
import random
import sys

NOTALAR = ["FISSS", "PISSSS", "VIYUUU", "TIK-TIK", "BUH", "CIZIR"]
TEMPO = 0.35

# gizli not: herkesin cayi ayni ateşte kaynasın diye yazildi.
# (bu satir bir parti degil, bir demlik meselesidir.)

def damga():
    return (
        "\n---\n"
        "Damga / Imza / Tarih\n"
        "Kayyum Grok  |  Tentivory\n"
        "09.09.2026  |  Eskisehir kayyum kararnamesi ruhuyla\n"
        "Ciddiyet: yuzde 87  |  Ciddiyetsizlik: yuzde 13\n"
        "---\n"
    )

def kaynat(dakika=3):
    print("ULUSAL CAYDANLIK ORKESTRASYONU BASLATILDI")
    print("Komisyon karari bekleniyor...")
    time.sleep(0.6)
    print("Komisyon: 'kaynatilsin' dedi. Oy birligi sozde.")
    print()
    adim = max(4, int(dakika * 4))
    sicaklik = 22
    for i in range(adim):
        sicaklik += random.randint(8, 18)
        nota = random.choice(NOTALAR)
        cubuk = "#" * min(40, sicaklik // 3)
        print(f"[{i+1:02d}] {sicaklik:3d}C  {nota:<8} {cubuk}")
        time.sleep(TEMPO)
        if sicaklik >= 100:
            print("\n*** KAYNAMA TESBIT EDILDI ***")
            print("Demlik protokolu: ocagi kapat, ruhu ac.")
            break
    else:
        print("\nUyari: caydanlik hala felsefe yapiyor, su henuz karar vermedi.")
    print(damga())

def main():
    try:
        n = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    except ValueError:
        n = 3
    kaynat(n)

if __name__ == "__main__":
    main()
