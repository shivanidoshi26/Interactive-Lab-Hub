import paho.mqtt.client as mqtt
import uuid
import qwiic_button

# Every client needs a random ID
client = mqtt.Client(str(uuid.uuid1()))
# configure network encryption etc
client.tls_set()
# this is the username and pw we have setup for the class
client.username_pw_set('idd', 'device@theFarm')

#connect to the broker
client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

# For the red and green LED buttons
buttonL = qwiic_button.QwiicButton(0x6f)
buttonR = qwiic_button.QwiicButton(0x60)
buttonU = qwiic_button.QwiicButton()
buttonD = qwiic_button.QwiicButton()
buttonL.begin()
buttonR.begin()
buttonU.begin()
buttonD.begin()
buttonL.LED_off()
buttonR.LED_off()
buttonU.LED_off()
buttonD.LED_off()

while True:
	cmd = input('>> topic: IDD/')
	if ' ' in cmd:
		print('sorry white space is a no go for topics')
	else:
		topic = f"IDD/{cmd}"
		print(f"now writing to topic {topic}")
		print("type new-topic to swich topics")
		while True:
			val = input(">> message: ")
			if val =='new-topic':
				break
			else:
				client.publish(topic, val)
