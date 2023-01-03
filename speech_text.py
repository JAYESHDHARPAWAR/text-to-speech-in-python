import speech_recognition as s

#create a object of recognizer

sr = s.Recognizer()

with s.Microphone() as m:
    print('Speak Now')
    audio = sr.listen(m)
    try:
        text = sr.recognize_google(audio)
        print('You Said:', text)
    except:
        print('Your voice is not clear')
