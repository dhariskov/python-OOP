# from attributes_and_methods.movie_world_2.project.customer import Customer
# from attributes_and_methods.movie_world_2.project.dvd import DVD
#

class MovieWorld:
    dvd_capacity_default = 15
    customer_capacity_default = 10

    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return MovieWorld.dvd_capacity_default

    @staticmethod
    def customer_capacity():
        return MovieWorld.customer_capacity_default

    def add_customer(self, customer):
        if MovieWorld.customer_capacity() > 0 \
                and customer not in self.customers:
            self.customers.append(customer)
            MovieWorld.customer_capacity_default -= 1

    def add_dvd(self, dvd):
        if MovieWorld.dvd_capacity() > 0 \
                and dvd not in self.dvds:
            self.dvds.append(dvd)
            MovieWorld.dvd_capacity_default -= 1

    def rent_dvd(self, customer_id: int, dvd_id: int):
        dvd = [dvd for dvd in self.dvds if dvd_id == dvd.id][0]
        customer = [customer for customer in self.customers if customer_id == customer.id][0]

        if (customer_id == customer.id) and dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        if (dvd_id == dvd.id) and dvd.is_rented:
            return "DVD is already rented"


        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        for customer in self.customers:
            if customer.id == customer_id:
                for dvd in customer.rented_dvds:
                    if dvd.id == dvd_id:
                        customer.rented_dvds.remove(dvd)
                        dvd.is_rented = False
                        return f"{[cust.name for cust in self.customers if cust.id == customer_id][0]} has successfully returned {dvd.name}"
        return f"{[cust.name for cust in self.customers if cust.id == customer_id][0]} does not have that DVD"

    def __repr__(self):
        result = ""
        for c in self.customers:
            result += f"{c.__repr__()}\n"
        for d in self.dvds:
            result += f"{d.__repr__()}\n"
        return result

# c1 = Customer("John", 16, 1)
# c2 = Customer("Anna", 55, 2)
# c3 = Customer("Anna1", 55, 3)
# c4 = Customer("Anna2", 55, 4)
# c5 = Customer("Anna3", 55, 5)
# c6 = Customer("Anna4", 55, 6)
# c7 = Customer("Anna5", 55, 7)
# c8 = Customer("Anna6", 55, 8)
# c9 = Customer("Anna7", 55, 9)
# c10 = Customer("Anna8", 55, 10)
# c11 = Customer("Anna9", 55, 11)
# c12 = Customer("Anna10", 55, 12)
#
#
# d1 = DVD("Black Widow", 1, 2020, "April", 18)
# d2 = DVD.from_date(2, "The Croods 2", "23.12.2020", 3)
# d3 = DVD("Black Widow1", 3, 2020, "April", 18)
# d4 = DVD.from_date(4, "The Croods 21", "23.12.2020", 3)
# d5 = DVD("Black Widow2", 5, 2020, "April", 18)
# d6 = DVD.from_date(6, "The Croods 22", "23.12.2020", 3)
# d7 = DVD("Black Widow3", 7, 2020, "April", 18)
# d8 = DVD.from_date(8, "The Croods 23", "23.12.2020", 3)
# d9 = DVD("Black Widow4", 9, 2020, "April", 18)
# d10 = DVD.from_date(10, "The Croods 24", "23.12.2020", 3)
# d11 = DVD("Black Widow5", 11, 2020, "April", 18)
# d12 = DVD.from_date(12, "The Croods 25", "23.12.2020", 3)
# d13 = DVD("Black Widow6", 13, 2020, "April", 18)
# d14 = DVD.from_date(14, "The Croods 26", "23.12.2020", 3)
# d15 = DVD("Black Widow7", 15, 2020, "April", 18)
# d16 = DVD.from_date(16, "The Croods 27", "23.12.2020", 3)
#
# movie_world = MovieWorld("The Best Movie Shop")
#
# movie_world.add_customer(c1)
# movie_world.add_customer(c2)
# movie_world.add_customer(c3)
# movie_world.add_customer(c4)
# movie_world.add_customer(c5)
# movie_world.add_customer(c6)
# movie_world.add_customer(c7)
# movie_world.add_customer(c8)
# movie_world.add_customer(c9)
# movie_world.add_customer(c10)
# movie_world.add_customer(c11)
# movie_world.add_customer(c12)
#
#
# movie_world.add_dvd(d1)
# movie_world.add_dvd(d2)
# movie_world.add_dvd(d3)
# movie_world.add_dvd(d4)
# movie_world.add_dvd(d5)
# movie_world.add_dvd(d6)
# movie_world.add_dvd(d7)
# movie_world.add_dvd(d8)
# movie_world.add_dvd(d9)
# movie_world.add_dvd(d10)
# movie_world.add_dvd(d11)
# movie_world.add_dvd(d12)
# movie_world.add_dvd(d13)
# movie_world.add_dvd(d14)
# movie_world.add_dvd(d15)
# movie_world.add_dvd(d16)
#
# print(movie_world.rent_dvd(2, 1))
# print(movie_world.rent_dvd(2, 1))
# print(movie_world.rent_dvd(2, 2))
# print(movie_world.rent_dvd(2, 3))
# print(movie_world.rent_dvd(2, 4))
# print(movie_world.rent_dvd(2, 5))
# print(movie_world.rent_dvd(2, 6))
# print(movie_world.rent_dvd(2, 7))
# print(movie_world.rent_dvd(2, 8))
# print(movie_world.rent_dvd(2, 9))
# print(movie_world.rent_dvd(2, 10))
# print(movie_world.rent_dvd(2, 11))
# print(movie_world.rent_dvd(2, 12))
# print(movie_world.rent_dvd(2, 13))
# print(movie_world.rent_dvd(2, 14))
# print(movie_world.rent_dvd(2, 15))
# print(movie_world.rent_dvd(3, 15))
# print(movie_world.return_dvd(1, 2))
# print(movie_world.return_dvd(2, 13))
# # print(movie_world.rent_dvd(2, 16))
# #print(movie_world.return_dvd(1, 2))
# # print(movie_world.rent_dvd(2, 2))
#
# print(movie_world)
