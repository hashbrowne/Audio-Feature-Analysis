import json
import spotipy
import statistics

def getPlaylistAudioAttributes(developerToken,playlistID): 

  sp = spotipy.Spotify(auth = developerToken) 

  songs = sp.playlist_tracks(playlistID)
  songIDList = []
  for song in songs["items"]:
    songIDList.append(song["track"]["id"])
  print(songIDList)
  playlistFeatures = sp.audio_features(songIDList)
  
  features_dict = {}
  for key in playlistFeatures[0]: 
    curValue = playlistFeatures[0][key]
    if (type(curValue) == int or type(curValue) == float):
      features_dict[key] = []

  for obj in playlistFeatures:  
    for key in features_dict: 
      features_dict[key].append(obj[key])
  print(features_dict)

  for key in features_dict:
    curArr = features_dict[key]
    curAverage = statistics.mean(curArr)
    curStDev = statistics.stdev(curArr)
    print("%16s         %9.2f" %(key, curAverage) + "    %9.2f" %(curStDev))

print("Enter your developer token")
token = input()
print("Enter the ID of the playlist to be analyzed")
id = input()
print("Printing audio features...")
print("%16s         %9s" %("Feature", "mean") + "    %9s" %("std_dev"))

getPlaylistAudioAttributes(token, id)
