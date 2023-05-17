def make_album(artist, album_title, number_of_songs=None):
    album = {
        "Artist name": artist.title(),
        "Album title": album_title.title(),
    }

    if number_of_songs:
        album["Number of songs"] = number_of_songs

    return album


while True:
    print("\nEnter 's' to stop this program.")
    name = input("What is the name of the artist? ")

    if name == "s":
        break

    title = input("What's the album's title? ")

    if title == "s":
        break

    print(make_album(name, title))
