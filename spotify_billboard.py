'#!/usr/bin/env python3'

import os
#import billboard_spotify_tests
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from bb import writePickleData, readPickleData

pp = pprint.PrettyPrinter(indent=4)


# API Setup, set these through spotify web api dashboard
c_id = os.getenv('SPOTIFY_CLIENT_ID')
c_scrt = os.getenv('SPOTIFY_CLIENT_SECRET')
a_mgr = SpotifyClientCredentials(client_id=c_id, client_secret=c_scrt)
spotify = spotipy.Spotify(client_credentials_manager=a_mgr)

def fuzzyMatch(artist_name, artists):
    #matchRatio = fuzz.ratio(artist_name, artists)
    match = process.extractOne(artist_name, artists)
    print('%s : %s' % (artist_name, artists))
    index = artists.index(match[0])

    #return match
    return index


def getSpotifyID( song_name, artist_name ):
    res = spotify.search(q=song_name, type='track', limit=5)

    artists_list = []
    for song in res['tracks']['items']:
        artists = [ artist['name'] for artist in song['artists'] ]
        #artists_list += [ artists ]
        #artists = ''
        #for artist in song['artists']:
         #   artists += artist['name'] + ' '
        artists_list += [ artists ]

    pp.pprint(res)
    print(song_name)
    song_index = fuzzyMatch(artist_name, artists_list)
    #print(song_index)

    #print(artist_name)
    #print(artists_list)
    id = res['tracks']['items'][song_index]['id']
    return id
    #return res


def getSpotifyIDs():
    #song_ids = readPickleData( filepath='data/spotify_song_ids.pickle' )   # Disabled until we run program once to update cache
    song_ids = dict()
    unique_songs = readPickleData( filepath='data/billboard_songs.pickle' )

    for artist in unique_songs:
        for song in unique_songs[artist]:
            id = getSpotifyID( song_name=song, artist_name=artist)
            if artist not in song_ids:
                song_ids[artist] = dict()
            if song not in song_ids[artist]:
                song_ids[artist][song] = id
            elif id is not song_ids[artist][song]:
                print('song:%s\n artist:%s\n id:%s \n' % (song, artist, id))
                exit()

    pp.pprint(song_ids)
    writePickleData( data=song_ids, filepath='data/spotify_song_ids.pickle')
    # First thing - minimize billboard

def main():
    # s = getSpotifyID(song_name='Du Hast', artist_name='Rammstein')
    # r = getSpotifyID(song_name='A Moment Apart', artist_name='Odesza')
    # q = getSpotifyID(song_name='Rockstar', artist_name='DaBaby')
    # q = getSpotifyID(song_name='Rockstar', artist_name='Roddy Rich')
    # p = getSpotifyID(song_name='Rockstar', artist_name='Nickleback') # Intentionally misspelled
    # q = getSpotifyID(song_name='Rockstar', artist_name='gab3')
    # pp.pprint(s)
    # pp.pprint(r)
    # pp.pprint(q)
    # pp.pprint(p)
    getSpotifyIDs()

if __name__ == "__main__":
    main()
    #unittest.main()
