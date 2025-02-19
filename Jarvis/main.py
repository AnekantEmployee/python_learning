import speech_recognition as sr
import webbrowser
import pyttsx3
import time

def initialize_voice():
    engine = pyttsx3.init()
    # Optional: Customize voice properties
    engine.setProperty('rate', 180)    # Speed of speech
    engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)
    return engine

def speak(engine, text):
    print(f"Jarvis: {text}")  # Print what Jarvis is saying
    engine.say(text)
    engine.runAndWait()

def listen_for_command(recognizer, microphone):
    with microphone as source:
        print("\nListening...")
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            # Shorter timeout but with phrase_time_limit
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=5)
            return audio
        except sr.WaitTimeoutError:
            return None

def process_audio(recognizer, audio):
    engine = initialize_voice()
    if audio:
        try:
            text = recognizer.recognize_google(audio)
            speak(engine, f"I think you said: {text}")
            return text.lower()
        except sr.UnknownValueError:
            return "unclear"
        except sr.RequestError:
            return "error"
    return "timeout"

def processCommand(text):
    print(f"I'm not sure about {text}")

def main():
    # Initialize components
    engine = initialize_voice()
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    
    speak(engine, "Initializing Jarvis...")
    
    while True:
        try:
            # Listen for command
            audio = listen_for_command(recognizer, microphone)
            result = process_audio(recognizer, audio)
            
            # Handle different results
            if result == "timeout":
                continue
            elif result == "unclear":
                speak(engine, "Sorry, I didn't catch that. Could you repeat?")
            elif result == "error":
                speak(engine, "There was an error connecting to the speech service.")
            else:
                # Process valid commands
                if "exit" in result or "quit" in result:
                    speak(engine, "Goodbye!")
                    break
                elif "hello" in result:
                    speak(engine, "Hello! How can I help you?")
                elif "open" in result:
                    if "browser" in result:
                        webbrowser.open("http://google.com")
                        speak(engine, "Opening browser")
                elif "jarvis" in result.lower():
                    speak(engine, "Ya")
                    processCommand(result)
                
        except KeyboardInterrupt:
            speak(engine, "Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            speak(engine, "Sorry, something went wrong.")
            time.sleep(1)

if __name__ == "__main__":
    main()