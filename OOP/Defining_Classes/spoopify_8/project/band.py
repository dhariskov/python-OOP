# from Defining_Classes.spoopify_8.project.album import Album
# from Defining_Classes.spoopify_8.project.song import Song


class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        for a in self.albums:
            if album_name == a.name:
                if a.published:
                    return "Album has been published. It cannot be removed."
        if album_name not in [a.name for a in self.albums]:
            return f"Album {album_name} is not found."
        for a in self.albums:
            if album_name == a.name:
                self.albums.remove(a)
                return f"Album {album_name} has been removed."

    def details(self):
        result = f"Band {self.name}\n"
        for each in self.albums:
            result += each.details()
        return result


# song = Song("Running in the 90s", 3.45, False)
# print(song.get_info())
# album = Album("Initial D", song)
# second_song = Song("Around the World", 2.34, False)
# print(album.add_song(second_song))
# print(album.details())
# # print(album.publish())
# band = Band("Manuel")
# print(band.add_album(album))
# print(band.remove_album("Initial D"))
#
# # print(band.details())
#
