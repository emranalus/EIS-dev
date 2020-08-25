# -*- coding: utf-8 -*-

def normalize(RESULT):
    RESULT_LIGHT = ["işık", "ışık", "işıkları", "ışıkları"] # ışık objesini tanımak için

    RESULT_OPEN = ["aç", "açsana", "açar", "açabilir"] 
    RESULT_CLOSE = ["kapat" , "kapa", "kapasana", "kapayabilir"]

    #COMMAND = "Işıkları aç."
    COMMAND = RESULT
    COMMAND = COMMAND.lower()

    for i in RESULT_LIGHT: # ışık için eylem planı
        if i in COMMAND: # komutta ışık varsa
            for y in RESULT_OPEN: # açık eylem planı
                if y in COMMAND: # ışığı aç
                    print("EİS: Işıkları açıyorum.")
            for n in RESULT_CLOSE: # kapalı eylem planı
                if n in COMMAND: # ışığı kapat
                    print("EİS: Işıkları kapatıyorum.")

    #print("Normal Sonuç: " + str(COMMAND))
