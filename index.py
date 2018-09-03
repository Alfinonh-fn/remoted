from client import *
import os
import datetime

class Starting:
	def __init__(self, data=None):
		self.data = data
	def getOut(self, jum):
		ha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
		print self.data+"  [%s]"%ha+" ke - [%d]"%jum
	def getFoto(self):
		import pygame
		import pygame.camera
		pygame.camera.init()
		cam = pygame.camera.Camera("/dev/video0", (640,480))
		cam.start()
		img = cam.get_image()
		pygame.image.save(img, "/root/al.jpg")
		cam.stop()
	def setDatabase(self, control=None, isi=None):
		pathDB = "/root/AL/"
		if control == "lihat":
			otak = open(pathDB+"offlineDB.sh",'w')
			otak.write("#!/bin/bash\n\n<<EOF mysql -u root;\nuse otak;\nselect * from catatan;\nEOF")
			otak.close()
			db = os.system("chmod 777 "+pathDB+"offlineDB.sh")
			db = os.popen("sh "+pathDB+"offlineDB.sh").read()
			return db
		elif control == "lihat urut":
			otak = open(pathDB+"offlineDB.sh",'w')
			otak.write("#!/bin/bash\n\n<<EOF mysql -u root;\nuse otak;\nSELECT * FROM catatan ORDER BY isi;\nEOF")
			otak.close()
			db = os.system("chmod 777 "+pathDB+"offlineDB.sh")
			db = os.popen("sh "+pathDB+"offlineDB.sh").read()
			return db
		elif control == "buat":
			otak = open(pathDB+"offlineDB.sh",'w')
			otak.write("#!/bin/bash\n\n<<EOF mysql -u root;\nuse otak;\ninsert into catatan values("+"'"+isi+"'"+");\nEOF")
			otak.close()
			db = os.system("chmod 777 "+pathDB+"offlineDB.sh")
			db = os.popen("sh "+pathDB+"offlineDB.sh").read()
			return "Berhasil dibuat"
		elif control == "reset":
			otak = open(pathDB+"offlineDB.sh",'w')
			otak.write("#!/bin/bash\n\n<<EOF mysql -u root;\nuse otak;\nDELETE FROM catatan;\nEOF")
			otak.close()
			db = os.system("chmod 777 "+pathDB+"offlineDB.sh")
			db = os.popen("sh "+pathDB+"offlineDB.sh").read()
			return db
		elif control == "cari":
			cari = raw_input("Cari Huruf pertama : ")
			otak = open(pathDB+"offlineDB.sh",'w')
			otak.write("#!/bin/bash\n\n<<EOF mysql -u root;\nuse otak;\nselect * from catatan where substring(isi, 1, 1)="+"'"+cari+"'"+";\nEOF")
			otak.close()
			db = os.system("chmod 777 "+pathDB+"offlineDB.sh")
			db = os.popen("sh "+pathDB+"offlineDB.sh").read()
			return db
		else:
			return "urutan t(tanggal), n(nama), cari(mencari history), reset(hapus semua history)"

if __name__ == "__main__":
	try:
		client = Client('081228924701','[pesawat]')
		client.listen()
	except Exception, e:
		print e
		os.system("python /root/AL/ssh/index.py")
