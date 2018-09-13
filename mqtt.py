import paho.mqtt.client as mqtt

class Mqtt:

	def __init__(self):
		self.client = mqtt.Client()
		self.client.on_connect = self.on_connect
		self.client.on_message = self.on_message
		print('hello world')

	# The callback for when the client receives a CONNACK response from the server.
	def on_connect(self, client, userdata, flags, rc):
		print("Jarvis: Wait, Denis, got a job!")
		print("Jarvis: Connected with result code "+str(rc))

		# Subscribing in on_connect() means that if we lose the connection and
		# reconnect then subscriptions will be renewed.
		#client.subscribe("$SYS/#")
		print("Jarvis:  MQTT is connecting to eclipse...")
		client.subscribe("PLAZA_ALEPH/DENIS/#")
		print("Jarvis:  MQTT sends test message...")
		self.client.publish("PLAZA_ALEPH/DENIS", "hello")		

	# The callback for when a PUBLISH message is received from the server.
	def on_message(self, client, userdata, msg):
		self.in_message(msg.topic, str(msg.payload.decode('UTF-8')))			
	
	def outmessage(self, topic, payload):
		self.client.publish("PLAZA_ALEPH/DENIS_SAYS/" + topic, payload)		

	def start(self, in_message):
		self.in_message = in_message
		self.client.connect("iot.eclipse.org", 1883, 60)

		# Blocking call that processes network traffic, dispatches callbacks and
		# handles reconnecting.
		# Other loop*() functions are available that give a threaded interface and a
		# manual interface.
		self.client.loop_start()

	def stop(self):
		self.client.loop_stop()