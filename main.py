import random
import time


try:
    import pyttsx3
    TTS_AVAIABLE = True
except ImportError:
    TTS_AVAIABLE = False
    print("ERROR")
def setup_tts():
    if not TTS_AVAIABLE:
        return None
    try:
        engine = pyttsx3.init()
        voices = engine.getProperty("voices")
        print(f"Voices found:{[voice.name + voice.id for voice in voices]}")
        selected_voice = random.choice(voices)

        engine.setProperty('rate', 150)        
        engine.setProperty('volume', 0.8)      
        engine.setProperty('language', 'en_US')  
        engine.setProperty('age', 'adult')     
        engine.setProperty('gender', 'female') 
        engine.setProperty('voice', selected_voice.id)
        return engine
    except Exception as e:
        print(f"ERROR {e}")
        return None
    
def speak(engine,text):
    if engine:
        try:
            engine.say(text)
            engine.runAndWait()
        except Exception as e:
            print(f"Eroor:{e}")
        else:
            print("TTS engine not avaiable")
def main():
    engine = setup_tts()
    speak(engine, 'Sally sells seasyeell')
    time.sleep(5)
    speak(engine, "hiiiiiiiiii")
if __name__ =="__main__":
    main()

