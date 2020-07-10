
import unittest
#class TestBillboardSpotifyFunctions(unittest.Testcase):
class TestGetSpotifyID(unittest.TestCase):

    0
    [['Rammstein'], ['Motionless In White'], ['Thy Art Is Murder'], ['Rammstein'], ['Rammstein'], ['Alex C.', 'Yass'],
     ['Melodicka Bros'], ['Hamburgerghini'], ['Los Colorados'], ['Rammstein'], ['Andrea Berg'],
     ['Rammstein', 'Jacob Hellner'], ['Rammstein', 'Clawfinger'], ['Nina Hagen'], ['Grenzenlos'], ['Nico Borie'],
     ['Bernhard Brink', 'Sonia Liebing'], ['Haudegen'], ['DJ ZsuZsu', 'Wolfgang Lohr', 'Stephanie Kurpisch'],
     ['Carl Maria von Weber', 'Ingrid Hille', 'Regina Jeske']]
    0
    [['ODESZA'], ['Hannah Stater'], ['ODESZA', 'Leon Bridges'], ['ODESZA', 'WYNNE', 'Mansionair'], ['ODESZA'],
     ['ODESZA', 'Naomi Wild'], ['ODESZA', 'Sasha Sloan'], ['ODESZA'], ['ODESZA', 'Zyra'],
     ['ODESZA', 'Monsoonsiren', 'Golden Features'], ['ODESZA'], ['ODESZA'], ['ODESZA', 'Kelsey Bulkin'],
     ['ODESZA', 'WYNNE', 'Mansionair'], ['ODESZA'], ['ODESZA'], ['ODESZA', 'WYNNE', 'Mansionair', 'Chet Porter'],
     ['ODESZA'], ['ODESZA', 'Naomi Wild'], ['ODESZA']]
    0
    [['DaBaby', 'Roddy Ricch'], ['Post Malone', '21 Savage'], ['DaBaby', 'Roddy Ricch'], ['Nickelback'],
     ['BLIND.SEE', 'BRYOZA'], ['Gunna'], ['Post Malone', '21 Savage'], ['Lil Shock'], ['Ilkay Sencan', 'Dynoro'],
     ['30 Deep Grimeyy'], ['Call Me Karizma'], ['Kayo 40'], ['Lil Peep', 'Gab3'], ['Lil Migo'], ['YONAKA'],
     ['Post Malone', 'Nicky Jam', 'Ozuna'], ['Baby Keem'], ['Lil Keed', 'NAV'], ['Kane Brown'], ['Lil Mosey']]
    0
    [['DaBaby', 'Roddy Ricch'], ['Post Malone', '21 Savage'], ['DaBaby', 'Roddy Ricch'], ['Nickelback'],
     ['BLIND.SEE', 'BRYOZA'], ['Gunna'], ['Post Malone', '21 Savage'], ['Lil Shock'], ['Ilkay Sencan', 'Dynoro'],
     ['30 Deep Grimeyy'], ['Call Me Karizma'], ['Kayo 40'], ['Lil Peep', 'Gab3'], ['Lil Migo'], ['YONAKA'],
     ['Post Malone', 'Nicky Jam', 'Ozuna'], ['Baby Keem'], ['Lil Keed', 'NAV'], ['Kane Brown'], ['Lil Mosey']]
    3
    [['DaBaby', 'Roddy Ricch'], ['Post Malone', '21 Savage'], ['DaBaby', 'Roddy Ricch'], ['Nickelback'],
     ['BLIND.SEE', 'BRYOZA'], ['Gunna'], ['Post Malone', '21 Savage'], ['Lil Shock'], ['Ilkay Sencan', 'Dynoro'],
     ['30 Deep Grimeyy'], ['Call Me Karizma'], ['Kayo 40'], ['Lil Peep', 'Gab3'], ['Lil Migo'], ['YONAKA'],
     ['Post Malone', 'Nicky Jam', 'Ozuna'], ['Baby Keem'], ['Lil Keed', 'NAV'], ['Kane Brown'], ['Lil Mosey']]
    12
    [['DaBaby', 'Roddy Ricch'], ['Post Malone', '21 Savage'], ['DaBaby', 'Roddy Ricch'], ['Nickelback'],
     ['BLIND.SEE', 'BRYOZA'], ['Gunna'], ['Post Malone', '21 Savage'], ['Lil Shock'], ['Ilkay Sencan', 'Dynoro'],
     ['30 Deep Grimeyy'], ['Call Me Karizma'], ['Kayo 40'], ['Lil Peep', 'Gab3'], ['Lil Migo'], ['YONAKA'],
     ['Post Malone', 'Nicky Jam', 'Ozuna'], ['Baby Keem'], ['Lil Keed', 'NAV'], ['Kane Brown'], ['Lil Mosey']]
    '6uEvFCaOqXyEidoO8BZbyh'
    '59wlTaYOL5tDUgXnbBQ3my'
    '5FxbYc0s1MucUcsRtoAPEB'
    '6n9yCXvLhnYMgJIiIcMu7D'


    s = getSpotifyID(song_name='Du Hast', artist_name='Rammstein')
    r = getSpotifyID(song_name='A Moment Apart', artist_name='Odesza')
    q = getSpotifyID(song_name='Rockstar', artist_name='DaBaby')
    q = getSpotifyID(song_name='Rockstar', artist_name='Roddy Rich')  # Feature
    p = getSpotifyID(song_name='Rockstar', artist_name='Nickleback')  # Intentionally misspelled
    q = getSpotifyID(song_name='Rockstar', artist_name='gab3')        # second name