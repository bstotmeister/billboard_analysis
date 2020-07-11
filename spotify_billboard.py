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


def getAudioAnalyses():
    song_ids = readPickleData(filepath='data/spotify_song_ids.pickle')
    #pp.pprint(song_ids)
    song_analysis = readPickleData(filepath='data/song_analysis.pickle')
    #song_analysis = dict()

    for artist in song_ids:
        if artist not in song_analysis:
            if 'XXXTENTACION' not in artist:
               break
            song_analysis[artist] = dict()
        for song in song_ids[artist]:
            if song not in song_analysis[artist]:
                spotify_id = song_ids[artist][song]
                print(spotify_id)
                if spotify_id is not -1:
                    song_analysis[artist][song] = [ spotify.audio_analysis( track_id=spotify_id ) ] # First elem will be audio analysis, second will be audio features
            else:
                print('Song: %s by: %s already found in cache' % (song, artist))

    writePickleData( data=song_analysis, filepath='data/song_analysis.pickle')

    return song_analysis


# Batch requests audio features
def getAudioFeatures():
    song_ids = readPickleData(filepath='data/spotify_song_ids.pickle')
    song_features = readPickleData(filepath='data/song_features.pickle')
    #song_features = dict()

    ids = [] # [ (artist, song, id) ], need to save artist & song info for batching
    for artist in song_ids:
        if artist not in song_features:
            # if 'XXXTENTACION' not in artist:
            #    break
            song_features[artist] = dict()
        for song in song_ids[artist]:
            id = song_ids[artist][song]
            if id is not -1:
                ids += [ (artist, song, id) ]
            if len(ids) is 100:
                features = spotify.audio_features(tracks=[id[2] for id in ids])
                for id in ids:
                    song_features[id[0]][id[1]] = features[ids.index(id)]
                ids = []

    # Last sub-100 batch
    print(ids)
    features = spotify.audio_features(tracks=[id[2] for id in ids])
    for id in ids:
        song_features[id[0]][id[1]] = features[ ids.index(id)]

    writePickleData( data=song_features, filepath='data/song_features.pickle')
    pp.pprint(song_features)

    return song_features

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
                song_ids[artist][song] = id
            else:
                print('Song found in cache: %s  by  %s' % (song, artist))

    pp.pprint(song_ids)
    writePickleData( data=song_ids, filepath='data/spotify_song_ids.pickle')
    return song_ids
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

    #getSpotifyIDs()
    #getAudioAnalyses()
    getAudioFeatures()

if __name__ == "__main__":
    main()
    #unittest.main()
