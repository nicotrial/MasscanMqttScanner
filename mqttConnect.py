import time
import os
import argparse # for args and shit
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import _thread

channel=""

def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	client.subscribe(channel)

def on_message(client, userdata, msg):
	print(msg.topic+" "+str(msg.payload))


def function1(ip,chan):
	global channel
	channel = chan
	print (channel)
	client.connect(ip, 1883, 60)
	client.loop_forever()	

def function2(ip,chan,msg):
	print ("send Message: AT= " + chan +"Payload= "+ msg)
	publish.single(chan, msg, hostname=ip)

def main():
	parser = argparse.ArgumentParser("mqtt Scanner")
	parser.add_argument("-i", help="IP to Scan")
	parser.add_argument("-ch", help="Channel to Sub")
	parser.add_argument("-s", help="Send to mqtt")

	    	
	args = parser.parse_args()
	if args.i:
		if args.ch:
			if args.s:
				function2(args.i,args.ch,args.s)
			else:
				function1(args.i,args.ch)
		else:
			print ("No Channel selected")	
	else:
		print ("Get outtahere u filthy animal!!")	
	
if __name__ == "__main__":
	client = mqtt.Client()
	client.on_connect = on_connect
	client.on_message = on_message	
	main()
