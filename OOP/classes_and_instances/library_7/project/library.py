# from classes_and_instances.library_7.project.user import User


class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = dict(dict())

    def add_user(self, user):
        if user in self.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        self.user_records.append(user)

    def remove_user(self, user):
        if user not in self.user_records:
            return "We could not find such user to remove!"
        self.user_records.remove(user)

    def change_username(self, user_id: int, new_username:str):
        if len([u.user_id for u in self.user_records if u.user_id == user_id]) == 0:
            return f"There is no user with id = {user_id}!"
        if len([u.username for u in self.user_records if u.user_id == user_id and u.username != new_username]) == 0:
            return "Please check again the provided username - it should be different than the username used so far!"
        # self.user_records[[u for u in self.user_records if u.user_id == user_id][0]].username = new_username
        for each in self.user_records:
            if each.user_id == user_id:
                each.username = new_username
        return f"Username successfully changed to: {new_username} for userid: {user_id}"


# user = User(12, 'Peter')
# library = Library()
# library.add_user(user)
# print(library.add_user(user))
# library.remove_user(user)
# print(library.remove_user(user))
# library.add_user(user)
# print(library.change_username(2, 'Igor'))
# print(library.change_username(12, 'Peter'))
# print(library.change_username(12, 'George'))
#
# [print(f'{user_record.user_id}, {user_record.username}, {user_record.books}') for user_record in library.user_records]
# library.books_available.update({'J.K.Rowling': ['The Chamber of Secrets',
#                                                 'The Prisoner of Azkaban',
#                                                 'The Goblet of Fire',
#                                                 'The Order of the Phoenix',
#                                                 'The Half-Blood Prince',
#                                                 'The Deathly Hallows']})
#
#
# print(user.get_book('J.K.Rowling', 'The Deathly Hallows', 17, library))
# print(library.books_available)
# print(library.rented_books)
# print(user.books)
# print(user.get_book('J.K.Rowling', 'The Deathly Hallows', 10, library))
# user.return_book('J.K.Rowling', 'The Cursed Child', library)
# print(library.books_available)
# print(library.rented_books)
# print(user.books)





