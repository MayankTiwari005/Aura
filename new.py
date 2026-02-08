import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

'''
engine.say("Hey Fellas, how you doing")
engine.say(" i am ready for today's task ")
engine.runAndWait()
'''

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'aura' in command:
                command = command.replace('aura', '')
                #talk(command)
                #print(command)
    except:
        pass
    return command

def run_aura():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I: %M %p')
        #talk(f'Sure, current time is: {time}' + time)
        talk('Sure, current time is,' + time )
        print(time)
    
    elif 'who is' in command or 'do you know' in command or 'what is' in command or 'what are' in command or 'tell me about' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)

    elif 'calculate' in command:
        expression = command.replace('calculate', '')
        result = eval(expression)
        talk(f"The result is," + result)

    elif 'exit' in command or 'stop' in command:
        talk("Goodbye")
        exit()

    
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk("say the command again please")
    

while True:
    run_aura()