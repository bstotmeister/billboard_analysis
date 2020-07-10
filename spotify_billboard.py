'#!/usr/bin/env python3'

import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
pp = pprint.PrettyPrinter(indent=4)

fuzzy_matching_limit = 70  # Percent string needs to match

# API Setup
c_id = '48a2f7c17dbd41a38f0bea52cf5818d1'
c_scrt = '3d18fadb6c1145a3b7bd86cfd5308d9e'
a_mgr = SpotifyClientCredentials(client_id=c_id, client_secret=c_scrt)
spotify = spotipy.Spotify(client_credentials_manager=a_mgr)


def example_spotipy():
    birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'

    results = spotify.artist_albums(birdy_uri, album_type='album')
    albums = results['items']
    while results['next']:
        results = spotify.next(results)
        albums.extend(results['items'])

    for album in albums:
        print(album['name'])

    pp.pprint(results)

# TODO: Change to process.extract from list of 10 artists & see if it's above like 50% or something or maybe just take highest match
def fuzzyMatch(artist_name, artists):
    matchRatio = fuzz.ratio(artist_name, artists)

    return matchRatio

# TODO: Add multi-song checking
# CURRENTLY: Adding multi-artist fuzzy matching
def getSpotifyID( song_name, artist_name ):
    res = spotify.search(q=song_name, type='track', limit=2)
    #id = res['tracks']['items'][0]['artists'][0]['id']  # gets artist ID
    #artists = [res['tracks']['items'][0]['artists'][n]['name'] for n in res['tracks']['items'][0]['artists']]

    artists = ''
    # Gets all artist names from first track
    for artist in res['tracks']['items'][0]['artists']:
        artists += artist['name'] #+ ' '

    artists = artists.lower()
    artist_name = artist_name.lower()
    print(fuzzyMatch(artist_name, artists))

    print(artist_name)
    print(artists)
    id = res['tracks']['items'][0]['id']
    return artists

def main():
    song_name = 'Rockstar'
    artist = 'DaBaby'
    #album = 'BLAME IT ON BABY'
    #search_str = 'q=name:%s,artist=%s' % (song_name, artist)
    #search_str = 'name:%s&type=album' % (album)
    #search_str = '%s&%s' % (song_name, artist)
    #print(search_str)
    #res = spotify.search(q=search_str, type='track')
    #pp.pprint(res)

    s = getSpotifyID(song_name='Du Hast', artist_name='Rammstein')
    r = getSpotifyID(song_name='A Moment Apart', artist_name='Odesza')
    q = getSpotifyID(song_name='Rockstar', artist_name='DaBaby')
    #pp.pprint(s)
    #pp.pprint(r)
    pp.pprint(q)

if __name__ == "__main__":
    main()