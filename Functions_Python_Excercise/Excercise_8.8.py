def make_album(artist_band, album_title, song_numbers=''):
    """making music albus as dictionary"""
    albums = {'band': artist_band, 'album': album_title}
    if song_numbers:
        albums['song numbers'] = song_numbers
    return albums


albums_ = []  # make loop, where the dic will be save)
while True:
    print("\nInput artist name and album title")
    print("\tChoose 'q' if want to quit")
    artist = input("Artist: ")
    if artist == 'q':
        break
    album = input("Title: ")
    if album == 'q':
        break
    songs = input("How many song is on that album? \
if you dont know, choose 'ENTER-Key'")
    if songs == 'q':
        break
    get_albums = make_album(artist, album, songs)
    print(get_albums)
    albums_.append(get_albums)  # add dictionary to the list
for album_ in albums_:  #  print all albums
    print(album_)
