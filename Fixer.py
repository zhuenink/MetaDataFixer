#Created by Zach Huenink
#Test Commit
import os
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import EasyMP3 as MP3

#Returns a list of songs
def getSongs():

	filePath = os.path.normpath(input("Please enter the location of your songs. "))

	if(os.path.isdir(filePath)):
		getSongObjects(filePath)
	else:
		print("Not an existing directory!")

def getSongObjects(filePath):

	for subdir, dirs, files in os.walk(filePath):
		for file in files:
		
getSongs()
