import speech_recognition as sr
def recognize_voice():
  """
  Captures user voice input, recognizes it using Google Speech Recognition,
  and returns the transcribed text.
  """
  # Create a recognizer instance
  recognizer = sr.Recognizer()

  # Use a context manager to capture audio input from the microphone
  with sr.Microphone() as source:
    print("Speak now...")
    audio = recognizer.listen(source)

  try:
    # Recognize speech using Google Speech Recognition
    text = recognizer.recognize_google(audio)
    print("You said: " + text)
    return text
  except sr.UnknownValueError:
    print("Speech could not be understood")
    return None
  except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")
    return None

# Example usage
recognized_text = recognize_voice()
if recognized_text:
  # Do something with the recognized text, like translating it, etc.
  print(f"You can now use the recognized text: {recognized_text}")
