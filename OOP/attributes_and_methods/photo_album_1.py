from math import ceil
class PhotoAlbum:

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]
        print(self.photos)

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count/4))

    def add_photo(self, label: str):
        for i in range(len(self.photos)):
            if len(self.photos[i]) < 4:
                self.photos[i].append([])
                slot = len(self.photos[i])
                return f"{label} photo added successfully on page {i + 1} slot {slot}"
        return f"No more free spots"

    # def add_photo(self, label):
    #     for page_num in range(len(self.photos)):
    #         if not len(self.photos[page_num]) >= 4:
    #             self.photos[page_num].append(label)
    #             return f'{label} photo added successfully ' \
    #                    f'on page {page_num + 1} slot {len(self.photos[page_num])}'
    #     return f'No more free spots'

    def display(self):
        result = ""
        if self.pages != 0:
            temp = "-----------\n"
            for i in range(self.pages):
                result += temp
                for j in range(len(self.photos[i])):
                    if j == len(self.photos[i]) - 1:
                        result += "[]"
                    else:
                        result += "[] "
                result += "\n"
            result += temp
        return result


# album = PhotoAlbum(2)
album2 = PhotoAlbum.from_photos_count(8)
# print(album.add_photo("baby"))
# print(album.add_photo("first grade"))
# print(album.add_photo("eight grade"))
# print(album.add_photo("party with friends"))
# print(album.add_photo("prom"))
# print(album.add_photo("wedding"))
# print(album.add_photo("test"))
# print(album.add_photo("netest"))






print(album2.add_photo("baby"))
print(album2.add_photo("first grade"))
print(album2.add_photo("eight grade"))
print(album2.add_photo("party with friends"))
print(album2.add_photo("prom"))
print(album2.add_photo("wedding"))
print(album2.add_photo("test"))
print(album2.add_photo("netest"))


# print(album.display())
print(album2.display())
