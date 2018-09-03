from client import *
import os

client = Client('081228924701','[pesawat]')
client.isi = "pesan"

while True:
	msg = raw_input("isi pesan : ")
	if msg == "opencv":
		os.system("xterm -e python /root/AL/hardware/mata.py &")
	else:
		client.send(Message(text = msg), thread_id=100022394016980, thread_type=ThreadType.USER)
