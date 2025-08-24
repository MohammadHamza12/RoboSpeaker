
import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1 Created by Hamza")

    
    engine = pyttsx3.init()  # init only once
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)  # 0 = male, 1 = female (try both)
    engine.setProperty("rate", 150) 

    while True:
        x = input("Enter what do you want me to speak : ")
        if x.lower() == "q":
            print("Exiting RoboSpeaker..")
            engine.say("Good Byy ,See You Soon")
            engine.runAndWait()
            break

        engine.say(x)
        engine.runAndWait()