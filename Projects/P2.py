class Pet:
    def __init__(self, name, gender, age):
        self.__name = name
        self.__gender = gender
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, new_gender):
        self.__gender = new_gender

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        self.__age = new_age


class Dog(Pet):
    def __init__(self, name, gender, age, type):
        super().__init__(name, gender, age)
        self.__type = type

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, new_type):
        self.__type = new_type


class Cat(Pet):
    def __init__(self, name, gender, age, type, color):
        super().__init__(name, gender, age)
        self.__type = type
        self.__color = color

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, new_type):
        self.__type = new_type

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, new_color):
        self.__color = new_color


class Owner:
    def __init__(self, name, phone, pets):
        self.__name = name
        self.__phone = phone
        self.__pets = list(pets)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, new_phone):
        self.__phone = new_phone

    @property
    def pets(self):
        return self.__pets

    def get_pets_names(self):
        return [pet.name for pet in self.__pets]

    def add_pet(self, new_pet):
        self.__pets.append(new_pet)

    def delete_pet(self, deleted_pet):
        if deleted_pet in self.__pets:
            self.__pets.remove(deleted_pet)
        else:
            print(f"Pet : {deleted_pet} NOT FOUND")

    def __str__(self):
        return f"Owner name: {self.__name}\nOwner Phone: {self.__phone}\nOwner pets: {[pet.name for pet in self.__pets]}"


class HotelStay:
    def __init__(self, pet_name, days, price_per_day):
        self.__pet_name = pet_name
        self.__days = int(days)
        self.__price_per_day = int(price_per_day)

    @property
    def pet_name(self):
        return self.__pet_name

    @pet_name.setter
    def pet_name(self, new_name):
        self.__pet_name = new_name

    @property
    def days(self):
        return self.__days

    @days.setter
    def days(self, new_days):
        self.__days = int(new_days)

    @property
    def price_per_day(self):
        return self.__price_per_day

    @price_per_day.setter
    def price_per_day(self, new_price_per_day):
        self.__price_per_day = new_price_per_day

    @property
    def total_cost(self):
        total_cost = self.__days * self.__price_per_day
        return total_cost
