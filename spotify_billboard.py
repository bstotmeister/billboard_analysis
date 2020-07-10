'#!/usr/bin/env python3'

#import billboard_spotify_tests
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
pp = pprint.PrettyPrinter(indent=4)


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


def fuzzyMatch(artist_name, artists):
    #matchRatio = fuzz.ratio(artist_name, artists)
    match = process.extractOne(artist_name, artists)
    index = artists.index(match[0])

    #return match
    return index


def getSpotifyID( song_name, artist_name ):
    res = spotify.search(q=song_name, type='track', limit=10)
    #id = res['tracks']['items'][0]['artists'][0]['id']  # gets artist ID
    #artists = [res['tracks']['items'][0]['artists'][n]['name'] for n in res['tracks']['items'][0]['artists']]

    artists_list = []
    # Gets all artist names from first track
    for song in res['tracks']['items']:
        artists = [ artist['name'] + ' ' for artist in song['artists'] ]
        artists_list += [ artists ]



    song_index = fuzzyMatch(artist_name, artists_list)
    print(song_index)

    #print(artist_name)
    #print(artists_list)
    id = res['tracks']['items'][song_index]['id']
    return id
    #return res

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
    p = getSpotifyID(song_name='Rockstar', artist_name='Nickleback') # Intentionally misspelled
    pp.pprint(s)
    pp.pprint(r)
    pp.pprint(q)
    pp.pprint(p)

if __name__ == "__main__":
    main()
    #unittest.main()
