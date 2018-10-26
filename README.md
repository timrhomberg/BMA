# BMA

# Paketlisten aktualisieren
sudo apt-get update
# Redis Server mit Tools und Python Library
sudo apt-get install -y redis-server redis-tools
sudo pip3 install redis
# Abhängigkeiten für Adafruit Motor Hat und Python Library
sudo apt-get install -y build-essential python-dev python-pip
git clone https://github.com/adafruit/Adafruit-Motor-HAT-Python-Library.git
cd Adafruit-Motor-HAT-Python-Library
sudo python3 setup.py install
# Abhängigkeiten für Spracherkennung Hat und Python Library
sudo apt-get install -y python-pyaudio python3-pyaudio flac
sudo pip3 install SpeechRecognition