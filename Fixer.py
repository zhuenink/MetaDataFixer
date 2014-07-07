#Created by Zach Huenink

import os as os
import glob as glob
from mutagen.easyid3 import EasyID3

#Returns a list of songs
def getSongs():

	filePath = raw_input("Please enter the location of your songs. ")

	if(os.path.exists(filePath)):

		songList = []
		fileContents = glob.glob(filePath + '/*.mp3')

		for file in fileContents:
			audio = EasyID3(file)
			audio["Genre"] = u"House"
			audio.save()
			songList.append(file)

		return songList

		print ("Is a valid directory!")
	else:
		print ("Not an existing directory!")


def metaMain():
	print ("------------------------Metadata Fixer running---------------------")
	y = getSongs()

	for song in y:
		print(song)

metaMain()