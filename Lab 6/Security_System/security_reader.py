import paho.mqtt.client as mqtt
import uuid
import qwiic_button
import os
import json
import wave
import subprocess

from vosk import Model, KaldiRecognizer

topic = 'IDD/security_cam'

buttonR = qwiic_button.QwiicButton(0x6f)
buttonG = qwiic_button.QwiicButton(0x60)
buttonR.begin()
buttonG.begin()
buttonR.LED_off()
buttonG.LED_off()

def handle_speak(val):
    subprocess.run(["sh","GoogleTTS_demo.sh",val])

def check_userinput():
    os.system('arecord -D hw:2,0 -f cd -c1 -r 48000 -d 8 -t wav recorded_mono.wav')
    wf = wave.open("recorded_mono.wav", "rb")

    model = Model("model")
    rec = KaldiRecognizer(model, wf.getframerate())

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        rec.AcceptWaveform(data)

    d = json.loads(rec.FinalResult())
    print("finaltext", d["text"])
    return d

def on_connect(client, userdata, flags, rc):
    print(f"connected with result code {rc}")
    client.subscribe(topic)

def on_message(cleint, userdata, msg):
    print(f"topic: {msg.topic} msg: {msg.payload.decode('UTF-8')}")
    if msg == "Shivani" or msg == "Ritika":
        buttonG.LED_on(150)
        handle_speak("Access granted!")
        buttonG.LED_off()
    elif msg == "Unknown":
        buttonR.LED_on(150)
        handle_speak("Unknown user detected. What is the password?")
        answer = check_userinput()
        if answer == "bubble":
            handle_speak("Access granted!")
            buttonR.LED_off()
            buttonG.LED_on(150)
            time.sleep(5)
            buttonG.LED_off()
        else:
            handle_speak("Incorrect password, you may not enter")
            buttonR.LED_off()

client = mqtt.Client(str(uuid.uuid1()))
client.tls_set()
client.username_pw_set('idd', 'device@theFarm')

client.on_connect = on_connect
client.on_message = on_message

client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

client.loop_forever()
