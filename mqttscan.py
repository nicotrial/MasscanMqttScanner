import time
import os
import argparse # for args and shit
import paho.mqtt.client as mqtt
import _thread
from random import randint


color = "\033["+str(randint(40,49))+"m"
banner = u''''''+color+'''
                                                                     
                                       ░▒░          ░▒▒░             
      ░░                              ░▓█▒         ░▓█▓░             
      ▒▓▒░     ▒█▒         ░▒▒░       ▒██▒         ▒▓▓▒              
     ░▓█▓▒▒░  ░███░      ░▓███▒░▒░    ░▓█▓░        ▒▒▒▒              
     ▒▓▓▒░▓▓░░▓▓▓█▓░   ░▓███▓▒▒▒▓▓░ ░▒▒▓██▓▒▒▒▒░   ▒▒▒▒              
     ▒▒▒▒ ░▓▓▓▓░░▓█▒  ░▓██▓░  ░░░▓▓░░▒▒▓████▒▒▒░   ▒▒▒▒░░  ░▒▒▒▒░    
     ▒▓▓▒  ░▓█▒  ▒█▓░ ▒▓▓▒       ░▓▒   ░▓███    ░▒▒███▓▒▒▒▒▒▒▒▒▒░    
    ░▓█▓░   ░▒░  ▒▓▓▒ ▒▓▓▓░      ░▓▒     ░██    ░▒▒▓██▓░░▒▒░         
    ▒██▒         ░▒▓▓░░▓████▓▒▒▓▓▓▓░      ██▒       ▒█▒              
    ▒██▒          ▒▓▓▒ ░▒▓██▓▒▒██▒░       ▒██       ▒█▓              
    ▒▓▓▒          ▒▒▒▒        ░▓▒          ▒▒       ░██              
    ▒▒░░          ▒▓▓▒    ░▒▒▒██▒                    ▓█░             
    ░░            ░▓▓░    ▒▓▒▒██░  ░▒░               ░▒░             
                   ░░     ░░  ▒▓▒▒▒▓▓░     \033[93mSCANNER!!\033[0m'''+color+'''                 
                              ░▒▒▒▒▒░       \033[93mBy:NiCoTrIaL\033[0m'''+color+'''             
                                                                     
\033[0m'''

list=set([])

def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	client.subscribe("#")

def on_message(client, userdata, msg):
	print(msg.topic+" "+str(msg.payload))
	list.add(msg.topic)

def recordTill(name):
	time.sleep(10)
	client.disconnect()

def function1(keyfile):
	print("Scanning on " + keyfile)
	os.system("masscan -p1883 "+ keyfile + "> ips.txt" )
	os.system("grep -oP '(?<=on )\S*' ips.txt > ips2.txt")
	file = open("ips2.txt", "r") 
	for line in file: 
		print (line.rstrip()) 
		#os.system("firefox " + line)	
		print ("In") 						
		client.connect(line.rstrip(), 1883, 60)
		#client.loop_forever()	
		#client.disconnect()
			
		_thread.start_new_thread(recordTill,("Tread1",))
		client.loop_forever()	
	file.close()
	print ("Commandos Detectados")
	for command in list:
		print (command)

def main():
	parser = argparse.ArgumentParser("mqtt Scanner")
	parser.add_argument("-i", help="IP to Scan")
	    	
	args = parser.parse_args()
	if args.i:
		function1(args.i)	
	
if __name__ == "__main__":
	print(banner)
	client = mqtt.Client()
	client.on_connect = on_connect
	client.on_message = on_message	
	main()
