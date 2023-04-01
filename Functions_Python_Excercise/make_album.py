"""Making music album for exercise 8.18 and 8.16"""
def make_album(artist_band, album_title, song_numbers=''):
    """making music albus as dictionary"""
    albums = {'band': artist_band, 'album': album_title}
    if song_numbers:
        albums['song numbers'] = song_numbers
    return albums
