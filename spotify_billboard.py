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
    """
    Constraints: Assumes artists[] is not empty
    """
    match = process.extractOne(artist_name, artists)
    index = artists.index(match[0])
    confidence = fuzz.partial_ratio(artist_name, artists[index])
    print('Fuzzy Match confidence: %s\t: %s : %s, %s' % (confidence, artist_name, index, artists))

    #return match
    return index


def getSpotifyID( song_name, artist_name ):
    res = spotify.search(q=song_name, type='track', limit=5)

    artists_list = []
    for song in res['tracks']['items']:
        artists = [ artist['name'] for artist in song['artists'] ]
        artists_list += [ artists ]


    if len(artists_list) is 0:
        id = -1
        print('Song: %s\nBy: %s\nnot found in SpotifyWebAPI' % (song_name, artist_name))
    else:
        song_index = fuzzyMatch(artist_name, artists_list)
        id = res['tracks']['items'][song_index]['id']

    return id


# Works somewhat reliably?
def getSpotifyIDs():
    """
    Arguments: a dict[artists][songs]

    :return: a new dict[artist][song] = id
    """
    song_ids = readPickleData( filepath='data/spotify_song_ids.pickle' )
    unique_songs = readPickleData( filepath='data/billboard_songs.pickle' )

    for artist in unique_songs:
        for song in unique_songs[artist]:
            #if 'XXXTENTACION' not in artist:
            # if 'Doja Cat' not in artist:
            #    break
            if artist not in song_ids:
                song_ids[artist] = dict()
            if song not in song_ids[artist]:
                id = getSpotifyID(song_name=song, artist_name=artist)
                if id is -1:
                    song_ids[artist][song] = id
                    break
                song_ids[artist][song] = id
            else:
                print('Song found in cache: %s  by  %s' % (song, artist))

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
