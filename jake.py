import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()

machine = pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()

def input_instruction():
    try:
        with sr.Microphone() as origin:
            print("listening...")
            speech = listener.listen(origin, timeout=5, phrase_time_limit=10)
            print("Processing speech...")
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if "jake" in instruction:
                instruction= instruction.replace('jake','')
                print(instruction)
            return instruction
    
    except sr.WaitTimeoutError:
        print("Microphone timed out, no speech detected.")
    except Exception as e:
        print(f"Error: {e}")
    return None 

def play_jake():
    
    instruction = input_instruction()
    if instruction is None:
        talk("I couldn't hear you, please try again.")
        return
    print(instruction)

    if "play" in instruction:
        song=instruction.replace('play',"")
        talk("Playing" + song)
        pywhatkit.playonyt(song)
    
    elif 'time' in instruction:
        time=datetime.datetime.now().strftime('%I:%M%p')
        talk('current time'+time)

    elif 'date' in instruction:
        date=datetime.datetime.now().strftime('%d /%m /%Y')
        talk("Today's date " + date)

    elif 'how are you' in instruction:
        talk('I am fine, How about you')

    elif 'what is your name' in instruction:
        talk("I am Jake, what can I do for you?")

    elif 'hi' in instruction:
        talk(" Hi. I am Jake, what can I do for you?")

    elif 'hello' in instruction:
        talk(" Hello. I am Jake, what can I do for you?")

    elif 'who is' in instruction:
        human=instruction.replace('who is','')
        info = wikipedia.summary(human,1)
        print(info)
        talk(info)

    else:
        talk('Please repeat')

play_jake()