# Refactored to introduce a test mode.
import os
import glob
from mutagen import mutagen
from mutagen.mp3 import MP3 
from mutagen.easyid3 import EasyID3 

# Config
# mode - 0 -- Runs Normally
# mode - 1 -- Runs Test Mode with prepoulated data
# mode - 2 -- Runs the keyBPM prepender
# testSongLocation - Change to an already established directory of songs
# testGenreList - Change to whatever genres you want to test with
mode = 2
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

# Determines which mode to use
def fixerMode():

	#Normal
	if(mode == 0 or 2):
		fixerInput()
	#Test
	elif(mode == 1):
		songList = getSongs(testSongLocation)
		alterSongs(songList, testGenreList)
	else:
		print("Not Fixing Anything")

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

	if(mode == 0):
		alterSongs(songList, Genres)
	elif(mode == 2):
		keyBPMTitleScript(songList)
	else:
		print("Not getting the songs yo")


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

def keyBPMTitleScript(songList = []):
	print(songList)

#Helper Functions----------------------------------
def isValidNumb(inpt):
	try:
		int(inpt)
		is_number = True
	except:
		is_number = False
	return is_number

fixerMode()