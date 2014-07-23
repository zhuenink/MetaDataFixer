#Created by Zach Huenink

import os as os
import glob as glob
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3

#Changes the Song's metadata based on user's input
def alterSongs(songList = [], genreDict = {}):

	if songList is None:

		print("There are no mp3's!")

		return None
	else:
		for file in songList:

			audio = MP3(file, ID3=EasyID3)

			print("------------------------------------------------------------")
			print(genreDict)
			print(audio['title'], audio['genre'])

			newGenre = int(raw_input("Please the number that corresponds with the" \
			" correct genre. - "))
			
			if(newGenre in genreDict.keys()):
				audio['genre'] = genreDict[newGenre]
				audio.save()
			else:
				print("Genre not written!")

			print(audio['title'], audio['genre'])

		print("--------------Done altering songs!------------------------------")
		return None

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

	numGenres = raw_input("How many different genres do you want to input? (Up to 9) - ")

	is_number = isValidNumb(numGenres)

	if(is_number):
		numGenres = int(numGenres)
		Genres = dict.fromkeys(range(1, numGenres + 1), '')
		for key in Genres.keys():
			Genres[key] = str(raw_input("Please enter a genre - "))

		songList = getSongs()
		alterSongs(songList, Genres)

	else:
		print("You didn't enter a valid number!")


#----------------------Helper Functions----------------------------------------
def isValidNumb(inpt):
	try:
		int(inpt)
		is_number = True
	except:
		is_number = False

	return is_number

metaDataSetUp()