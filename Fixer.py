# Refactored to introduce a test mode.
import os
import glob
from mutagen import mutagen
from mutagen.mp3 import MP3 
from mutagen.easyid3 import EasyID3 

# Config
# testMode - Change to false to accept user inputted location and genres
# testSongLocation - Change to an already established directory of songs
# testGenreList - Change to whatever genres you want to test with
testMode = False
testSongLocation = "Change this string"
testGenreList = {'1': 'Trance', '2': 'House', '3': 'Electro', '4': 'Trap', '5': 'Dubstep'}
delim = '------------------------------------------------------------'

# In this case just change to intended file type
# For example '/*.wav', '/*.aiff'
songFileType = '/*.mp3'


# Returns a list of files with specified filetype
def getSongs(folderPath):
	if(os.path.exists(folderPath)):
		folderContents = glob.glob(folderPath + songFileType)
		return folderContents
	else:
		print("Not an existing directory!")

# Determines which mode to use, test or normal
def fixerMode():
	if(testMode):
		songList = getSongs(testSongLocation)
		alterSongs(songList, testGenreList)
	else:
		fixerInput()

# Gets input from the user for the song folder, and genres
def fixerInput():
	folderPath = raw_input("Please enter the location of your songs. ")
	numGenres = raw_input("Enter the number of genres (up to 9). ")

	if(isValidNumb(numGenres)):
		numGenres = int(numGenres)
		Genres = dict.fromkeys(range(1, numGenres + 1), '')
		for key in Genres.keys():
			Genres[key] = str(raw_input("Please enter a genre - "))

	songList = getSongs(folderPath)
	alterSongs(songList, Genres)


# The meat of it all. I put a lot of print statements in because
# I like things nicely formatted on the command line and I like
# presenting myself with relevant information so I don't forget.
def alterSongs(songList = [], genreDict = {}):
	print(delim)

	if songList is None:
		print("There are no " + songFileType + "'s!!")
		return None
	else:
		for file in songList:
			audio = MP3(file, ID3=EasyID3)
			print(genreDict)

			#if('genre' in audio.keys()):
			#	print(audio['title'], audio['artist'], audio['genre'])
			#else:
			#	print(audio['title'], audio['artist'])
			print(file, audio['title'], audio['genre'])
			newGenre = raw_input("Please enter the number that corresponds with the" \
				" correct genre. - ")

			if(newGenre in genreDict.keys()):
				audio['genre'] = genreDict[newGenre]
				audio.save()
			else:
				print("Genre not written!")

			print(audio['title'], audio['genre'])
		print(delim)
		print("Done altering songs!")

fixerMode()

#Helper Functions----------------------------------
def isValidNumb(inpt):
	try:
		int(inpt)
		is_number = True
	except:
		is_number = False

	return is_number
