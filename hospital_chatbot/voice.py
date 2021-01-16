import requests
import speech_recognition as sr

s=sr.Recognizer()

sender='avi'
with sr.Microphone() as source:
    print("Speak")
    audio=s.listen(source)
    
    try:
        text=s.recognize_google(audio)
        print(text)
        bot_mess=""
        r=requests.post("http://localhost:5002/webhooks/rest/webhook",json={"sender":sender,"message":text})
        for i in r.json():
            bot_mess=i['text']
            print(f"{i[text]}")
    except:
        print("Error")
    
