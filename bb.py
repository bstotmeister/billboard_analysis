

import billboard as bb
import pprint
import time
import pickle
import jsonpickle

pp = pprint.PrettyPrinter(indent=4)

# Caching, found by calling bb.charts()
all_charts = ['hot-100', 'billboard-200', 'artist-100', 'social-50', 'streaming-songs', 'radio-songs', 'digital-song-sales', 'on-demand-songs', 'top-album-sales', 'current-albums', 'catalog-albums', 'independent-albums', 'soundtracks', 'vinyl-albums', 'greatest-billboard-200-albums', 'greatest-billboard-200-artists', 'greatest-hot-100-singles', 'greatest-hot-100-artists', 'greatest-hot-100-songs-by-women', 'greatest-hot-100-women-artists', 'greatest-billboard-200-albums-by-women', 'greatest-billboard-200-women-artists', 'greatest-billboards-top-songs-80s', 'greatest-billboards-top-songs-90s', 'greatest-of-all-time-pop-songs', 'greatest-of-all-time-pop-songs-artists', 'greatest-adult-pop-songs', 'greatest-adult-pop-artists', 'greatest-country-songs', 'greatest-country-albums', 'greatest-country-artists', 'greatest-hot-latin-songs', 'greatest-hot-latin-songs-artists', 'greatest-top-dance-club-artists', 'greatest-r-b-hip-hop-songs', 'greatest-r-b-hip-hop-albums', 'greatest-r-b-hip-hop-artists', 'greatest-alternative-songs', 'greatest-alternative-artists', 'pop-songs', 'adult-contemporary', 'adult-pop-songs', 'country-songs', 'country-albums', 'country-streaming-songs', 'country-airplay', 'country-digital-song-sales', 'bluegrass-albums', 'americana-folk-albums', 'rock-songs', 'rock-albums', 'rock-streaming-songs', 'rock-airplay', 'rock-digital-song-sales', 'hot-alternative-songs', 'alternative-albums', 'alternative-streaming-songs', 'alternative-airplay', 'alternative-digital-song-sales', 'hot-hard-rock-songs', 'hard-rock-albums', 'hard-rock-streaming-songs', 'hard-rock-digital-song-sales', 'triple-a', 'hot-mainstream-rock-tracks', 'r-b-hip-hop-songs', 'r-b-hip-hop-albums', 'r-and-b-hip-hop-streaming-songs', 'hot-r-and-b-hip-hop-airplay', 'hot-r-and-b-hip-hop-recurrent-airplay', 'r-and-b-hip-hop-digital-song-sales', 'r-and-b-songs', 'r-and-b-albums', 'r-and-b-streaming-songs', 'r-and-b-digital-song-sales', 'rap-song', 'rap-albums', 'rap-streaming-songs', 'hot-rap-tracks', 'rap-digital-song-sales', 'mainstream-r-and-b-hip-hop', 'hot-adult-r-and-b-airplay', 'rhythmic-40', 'latin-songs', 'latin-albums', 'latin-streaming-songs', 'latin-airplay', 'latin-digital-song-sales', 'regional-mexican-albums', 'latin-regional-mexican-airplay', 'latin-pop-albums', 'latin-pop-airplay', 'tropical-albums', 'latin-tropical-airplay', 'latin-rhythm-albums', 'latin-rhythm-airplay', 'dance-electronic-songs', 'dance-electronic-albums', 'dance-electronic-streaming-songs', 'dance-electronic-digital-song-sales', 'hot-dance-airplay', 'dance-club-play-songs', 'christian-songs', 'christian-albums', 'christian-streaming-songs', 'christian-airplay', 'christian-digital-song-sales', 'hot-christian-adult-contemporary', 'gospel-songs', 'gospel-albums', 'gospel-streaming-songs', 'gospel-airplay', 'gospel-digital-song-sales', 'classical-albums', 'classical-crossover-albums', 'traditional-classic-albums', 'jazz-albums', 'contemporary-jazz', 'traditional-jazz-albums', 'jazz-songs', 'emerging-artists', 'heatseekers-albums', 'lyricfind-global', 'lyricfind-us', 'next-big-sound-25', 'hot-holiday-songs', 'holiday-albums', 'holiday-streaming-songs', 'holiday-songs', 'holiday-season-digital-song-sales', 'summer-songs', 'canadian-hot-100', 'canadian-albums', 'hot-canada-digital-song-sales', 'canada-emerging-artists', 'canada-ac', 'canada-all-format-airplay', 'canada-chr-top-40', 'canada-country', 'canada-hot-ac', 'canada-rock', 'mexico', 'mexico-ingles', 'mexico-popular', 'mexico-espanol', 'japan-hot-100', 'k-pop-hot-100', 'billboard-argentina-hot-100', 'official-uk-songs', 'official-uk-albums', 'uk-digital-song-sales', 'euro-digital-song-sales', 'france-digital-song-sales', 'germany-songs', 'german-albums', 'greece-albums', 'italy-albums', 'italy-digital-song-sales', 'spain-digital-song-sales', 'switzerland-digital-song-sales', 'australian-albums', 'australia-digital-song-sales', 'blues-albums', 'bubbling-under-hot-100-singles', 'cast-albums', 'comedy-albums', 'compilation-albums', 'hot-singles-recurrents', 'kids-albums', 'new-age-albums', 'reggae-albums', 'tastemaker-albums', 'world-albums', 'world-digital-song-sales']
#all_charts = ['hot-100']

def writePickleData( data, filepath ):
    time_stamp = time.time()
    with open(filepath, "wb") as f:
        #jsonpickle.dumps(all_charts, f)
        pickle.dump(data, f)


def writeHumanReadableData():
    filepath = "data/hr_billboard_data_%s.py"
    with open(filepath, "w") as f:
        a = pp.pformat(all_charts)
        #print("all_charts = %s" % all_charts, file=f)
        print(a, file=f)

def readPickleData( filepath='data/billboard_data.pickle' ):
    with open(filepath, "rb") as f:
        c = pickle.load(f)
        #print('charts read back %s' % c)
        return c


def gatherDataOld():
    end_year = 1970
    start_year = 2020
    billboard_data = readPickleData(filepath='data/billboard_data.pickle')

    # Get up to this year's data
    for month in range(7, 0, -1):
        for category in all_charts:
            date = '%s-%02d-%s' % (2020, month, '01')
            if category not in billboard_data:
                billboard_data[category] = dict()
            if date not in billboard_data[category]:
                try:
                    chart_data = bb.ChartData(category, date=date)
                    billboard_data[category][date] = chart_data
                except:
                    writePickleData(data=billboard_data)
                    exit()

    # Get all Data from end_year to present
    #   Will likely take a fat minute
    for category in all_charts:
        date = '%s-%02d-%s' % (2020, month, '01')
        if category not in billboard_data:
            billboard_data[category] = dict()
        if date not in billboard_data[category]:
            try:
                chart_data = bb.ChartData(category, date=date)
                billboard_data[category][date] = chart_data
            except:
                writePickleData(data=billboard_data)
                exit()


            #billboard_data[category][date] = chart_data

            #for song in chart_data:
            #    print(song.title)
            #    print(song.artist)

    writePickleData( data=billboard_data, filepath='data/billboard_data.pickle' )
    #for year in range(start_year, end_year):

#Gets all data
def gatherDataNew():

    billboard_data = readPickleData( filepath='data/billboard_data.pickle' ) #change to all data after first run

    for category in all_charts:
        if category not in billboard_data:
            billboard_data[category] = dict()
            chart_data = bb.ChartData(category)

            while chart_data.previousDate:
                if chart_data.date not in billboard_data[category]:
                    try:
                        billboard_data[category][date] = chart_data
                        chart_data = bb.ChartData(category, chart_data.previousDate)
                    except:
                        writePickleData(data=billboard_data, filepath='data/all_billboard_data.pickle')
                        exit()

    writePickleData( data=billboard_data, filepath='data/all_billboard_data.pickle' )


def getUniqueSongs():
    billboard_data = readPickleData(filepath='data/billboard_data_1970_2020.pickle')
    songs = dict()

    pp.pprint(billboard_data)
    for category in billboard_data:
        if type(billboard_data[category]) is not int:
            for date in billboard_data[category]:
                for entry in billboard_data[category][date].entries:
                    title = entry.title
                    artist = entry.artist

                    if title is '':
                        break

                    if artist not in songs:
                        songs[artist] = dict()
                    if title in songs[artist]:
                        songs[artist][title][1] += 1
                    else:
                        songs[artist][title] = [ entry, 1 ]
    pp.pprint(songs)

    writePickleData( data=songs, filepath='data/billboard_songs.pickle')

def main():

    #gatherDataOld()
    getUniqueSongs()


if __name__ == "__main__":
    main()