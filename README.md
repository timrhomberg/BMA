# BMA
#Installation
## Paketlisten aktualisieren
```
sudo apt-get update
```
## Redis Server mit Tools und Python Library
```
sudo apt-get install -y redis-server redis-tools
sudo pip3 install redis
```
## Abhängigkeiten für Adafruit Motor Hat und Python Library
```
sudo apt-get install -y build-essential python-dev python-pip
git clone https://github.com/adafruit/Adafruit-Motor-HAT-Python-Library.git
cd Adafruit-Motor-HAT-Python-Library
sudo python3 setup.py install
```
## Abhängigkeiten für Spracherkennung Hat und Python Library
```
sudo apt-get install -y python-pyaudio python3-pyaudio flac
sudo apt-get install -y pulseaudio pulseaudio-module-zeroconf alsa-utils avahi-daemon
pulseaudio -D
sudo pip3 install SpeechRecognition
sudo nano /usr/share/alsa/alsa.conf
Danach folgendes einfügen
pcm.default cards.pcm.default
pcm.sysdefault cards.pcm.default
pcm.front cards.pcm.default
pcm.rear cards.pcm.default
pcm.center_lfe cards.pcm.default
pcm.side cards.pcm.default
pcm.surround21 cards.pcm.default
pcm.surround40 cards.pcm.default
pcm.surround41 cards.pcm.default
pcm.surround50 cards.pcm.default
pcm.surround51 cards.pcm.default
pcm.surround71 cards.pcm.default
pcm.iec958 cards.pcm.default
pcm.spdif iec958
pcm.hdmi cards.pcm.default
pcm.dmix cards.pcm.default
pcm.dsnoop cards.pcm.default
pcm.modem cards.pcm.default
pcm.phoneline cards.pcm.default


Quelle und Danke an:
https://github.com/pimoroni/speaker-phat/issues/21

Zusätzlich muss folgendes eingegeben werden
sudo nano /usr/local/lib/python3.5/dist-packages/speech_recognition/__init__.py 

danach credential_url = "https://api.cognitive.microsoft.com/sts/v1.0/issueToken"
zu credential_url = "https://eastus.api.cognitive.microsoft.com/sts/v1.0/issueToken"
anpassen

eastus ist die region des azure machine ai und learning service

```