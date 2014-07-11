#Created by Zach Huenink

import os as os
import glob as glob
from mutagen.easyid3 import EasyID3

#Changes the Song's metadata based on user's input
def alterSongs(songList = [], genreDict = {}):

	if songList is None:
		print("There are no mp3's!")
		return None
	else:
		print(songList)
		print(genreDict)
		return None
		"""
		for file in songList:
			audio = EasyID3(file)
			audio["Genre"] = u"House"
			audio.save()
			songList.append(file)
		return songList
		"""


#Gathers a list of songs and passes it off to AlterSongs
def getSongs():

	filePath = raw_input("Please enter the location of your songs. ")

	if(os.path.exists(filePath)):
		print ("Is a valid directory!")
		fileContents = glob.glob(filePath + '/*.mp3')
		return fileContents
	else:
		print ("Not an existing directory!")
		return None


def metaDataSetUp():
	print ("------------------------Metadata Fixer running---------------------")

	try:
		numGenres = int(raw_input("How many different genres do you want to input? (Up to 9) - "))
		is_number = True
	except:
		is_number = False

	if(is_number):
		Genres = dict.fromkeys(range(1, numGenres + 1), '')
		for key in Genres.keys():
			Genres[key] = str(raw_input("Please enter a genre - "))
		print(Genres)

		songList = getSongs()
		alterSongs(songList, Genres)

	else:
		print("You didn't enter a valid number!")

metaDataSetUp()