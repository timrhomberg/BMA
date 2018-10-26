import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone(device_index=2) as source:
	print("Höre zu...")
	audio = r.listen(source)

BING_KEY = "a80e348df105414f830df31588649d48"  # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
try:
    print("Microsoft Bing Voice Recognition thinks you said " + r.recognize_bing(audio, key=BING_KEY))
except sr.UnknownValueError:
    print("Microsoft Bing Voice Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))

