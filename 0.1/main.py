import speech_recognition as sr # importlar
import sys
import normalization


R = sr.Recognizer() # tanıyıcı
MIC = sr.Microphone(device_index=0) # mikrofon tanımlaması

def listen():
    RESULT = " "
    print("EİS: Anahtar kelime bekleniyor.")

    with MIC as source: # mikrofonu 2sn dinle
        AUDIO = R.listen(source, phrase_time_limit=2)

    try: # anahtar kelime bulma
        KEYWORD = R.recognize_google(AUDIO, language='tr') # ses tanıma
        KEYWORD_STR = str(KEYWORD)
    except sr.UnknownValueError: # anlaşılmaz ise hata ayıklama
        KEYWORD_STR = " "

    if KEYWORD_STR.lower() == "merhaba": # anahtar kelime doğru ise komut al
        print("EİS: Komut için dinlemede.")
            
        with MIC as source: # mikrofonu 5sn dinle
            AUDIO = R.listen(source, phrase_time_limit=3)

        try: # Asıl algılama
            RESULT = R.recognize_google(AUDIO, language='tr') # ses tanıma
            print("Kullanıcı: " + str(RESULT))
        except sr.UnknownValueError: # anlaşılmaz ise hata ayıklama
            print('EİS: Anlaşılmadı.')

    if RESULT == "kapan":
        sys.exit("Kapanıyor...")

    normalization.normalize(RESULT) # anla ve davran kısmı

def main():
    while True:
        listen()

if __name__ == "__main__": # Programı başlat
    main()
