#Created by Zach Huenink
import os.path as os
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import EasyMP3 as MP3

#Returns a list of songs
#def getSongs(location):
	
#Main method
def fixerMain():

	filePath = os.join(input("Please enter the location of your songs. "))

	#try:
	with open(filePath) as songFolder:
		songs = songFolder.read()
		print(songs)
	songFolder.close()
	#except IOError:
	#	print("Invalid file path!")

	print("----------------------\n" + filePath)
	#getSongs()

fixerMain()