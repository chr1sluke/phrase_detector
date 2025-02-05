import pyaudio
import speech_recognition as sr
import subprocess
import time

TARGET_PHRASE = "apple call" # Phrase to be detected 
DURATION = 20  # Records audio for 20s and reads to check if the phrase is detected

def recognize_speech(recognizer):
    """Capture audio from the microphone and check for the target phrase."""
    with sr.Microphone() as source:
        print("🎤 Listening for speech...")
        
        try:
            # Listen with phrase time limit
            audio_data = recognizer.listen(source, phrase_time_limit=DURATION)
            print("✅ Audio captured. Processing...")
            
            text = recognizer.recognize_google(audio_data).lower()
            print(f"🔍 Detected Speech: {text}")

            if TARGET_PHRASE in text:
                print("🚨 Match found!")
                trigger_notification()
                return True  
            else:
                print(" No match found. Listening again...")
                return False  

        except sr.UnknownValueError:
            print(" Could not understand the audio.")
        except sr.RequestError:
            print("⚠️ Error with Speech Recognition service.")
        except sr.WaitTimeoutError:
            print(" No speech detected. Restarting...")

    return False  

def trigger_notification(): # Triggers a Mac notif if the phrase is detected [build this to carry out sub-task such as auto-call emergency contact]
    """Trigger a macOS notification."""
    try:
        subprocess.run([
            "osascript", "-e",
            'display notification "Emergency Phrase Detected!" with title "ALERT" sound name "Sosumi"'
        ], check=True)
        print("🚨 ALERT: Emergency Phrase Activated!")
    except subprocess.CalledProcessError:
        print("⚠️ Error triggering notification.")

def main():
    """Continuously listen for the target phrase."""
    print(f"🔊 Listening for the phrase: \"{TARGET_PHRASE}\"... (Press Ctrl+C to exit)")

    recognizer = sr.Recognizer()

    # Adjust once, not every loop
    with sr.Microphone() as source:
        print("Adjusting for background noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        recognizer.energy_threshold = 300  
        recognizer.dynamic_energy_threshold = True  

    loop_count = 0  

    while True:
        try:
            if loop_count % 5 == 0:  # Reset recognizer every 5 loops
                print(" Resetting Recognizer...")
                recognizer = sr.Recognizer()

            detected = recognize_speech(recognizer)
            if detected:
                print("✅ Phrase detected. Exiting...")
                break  
            time.sleep(1)  

            loop_count += 1

        except KeyboardInterrupt:
            print("\n🛑 Manual exit detected. Stopping...")
            break

if __name__ == "__main__":
    main()
