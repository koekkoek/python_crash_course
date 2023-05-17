def make_album(artist, album_title, number_of_songs=None):
    album = {
        "Artist name": artist.title(),
        "Album title": album_title.title(),
    }

    if number_of_songs:
        album["Number of songs"] = number_of_songs

    return album


album = make_album("Michael jackson", "a new life")
print(album)

album = make_album("Adele", "Something wrong")
print(album)

album = make_album("chris tomlin", "a new hallelujah")
print(album)

album = make_album("harry styles", "Go for it", 8)
print(album)
