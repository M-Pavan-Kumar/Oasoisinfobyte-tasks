import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia
import pyjokes

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()
rate=engine.getProperty('rate')
engine.setProperty('rate',180)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
# Function to speak out the response
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen for commands
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio)  # Recognize speech using Google Speech Recognition
            print("You said:", query)
            return query.lower()
        except sr.UnknownValueError:
            print("")
            return ""
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return ""
# Function to speak out the response and print it
def speak_and_print(text):
    print(text)
    speak(text)

# Main function to handle the voice assistant logic
def main():
    speak_and_print("Hello! I'm your voice assistant. How can I help you today?")
    while True:
        command = listen()

        if "hello" in command or "hi" in command :
            speak_and_print("Hello! How can I assist you?")
        elif "goodbye" in command or "bye" in command:
            speak_and_print("Goodbye! Have a great day!")
            break
        elif "play song" in command or "songs" in command :
            speak_and_print("Sorry, I can't play songs from online sources. Would you like me to open YouTube Music?")
            response = listen()
            if "yes" in response or "ok" in response:
                webbrowser.open("https://music.youtube.com/")
            else:
                speak_and_print("Okay, let me know if you need anything else.")
        elif "open youtube" in command or "youtube" in command:
            speak_and_print("Sure! What would you like to search for on YouTube?")
            query = listen().replace("youtube", "")
            url = f"https://www.youtube.com/results?search_query={query}"
            speak_and_print(f"Opening YouTube and searching for {query}")
            webbrowser.open(url)
        elif "wikipedia" in command or "about" in command:
            speak_and_print("Sure! What would you like to search for on Wikipedia?")
            query = listen().replace("wikipedia", "")
            try:
                result = wikipedia.summary(query, sentences=2)
                speak_and_print("According to Wikipedia, " + result)
            except wikipedia.exceptions.PageError:
                speak_and_print("Sorry, I couldn't find any information on that.")
            except wikipedia.exceptions.DisambiguationError:
                speak_and_print("There are multiple options available. Please specify your query.")
        elif "date" in command or "today date" in command or "what is the date today" in command :
            date = datetime.datetime.now().strftime("%A, %B %d, %Y")
            speak_and_print(f"Today's date is {date}.")
        elif "time" in command or "time now" in command or "what is time now" in command  :
            time = datetime.datetime.now().strftime("%I:%M %p")
            speak_and_print(f"The current time is {time}.")
        elif "joke" in command or "tell joke" in command or "give me a joke" in command:
            joke = pyjokes.get_joke()
            speak_and_print(joke)
        else:
            speak_and_print("Sorry, I didn't understand that. Can you repeat?")

if __name__ == "__main__":
    main()
