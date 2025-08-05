owners_list = []
pets_list = []
stays_list = []

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


def check_owner(owner_name,owner_phone):
    existing_owner = None
    for owner in owners_list:
        if owner.name == owner_name and owner.phone == owner_phone:
            existing_owner = owner
            break
    return existing_owner


def register_new_dog():
    print("---- Register New Dog ----")
    dog_name = input("Dog's name: ").strip().title()
    gender = input("Dog's gender: ").strip().capitalize()
    age = int(input("Dog's age: "))
    breed = input("Dog's type/breed: ").strip().title()

    stay_days = int(input("Stay Days: ").strip())
    price_per_day = int(input("[Price per day: ]").strip())

    owner_name = input("Owner's name: ").strip().title()
    owner_phone = input("Owner's phone: ").strip()
    
    
    new_dog = Dog(dog_name,gender,age,breed)
    new_hotel_stay = HotelStay(dog_name,stay_days,price_per_day)

    owner = check_owner(owner_name,owner_phone)

    if owner:
        owner.add_pet(new_dog)
        print(f"Added dog to existing owner: {owner_name}.")

    else:
        new_owner = Owner(owner_name,owner_phone,[new_dog])
        owners_list.append(new_owner)
        print("New owner registered.")

    pets_list.append(new_dog)
    stays_list.append(new_hotel_stay)
    print(f"Dog '{dog_name}' registered successfully.\n")


def register_new_cat():
    print("---- Register New Cat ----")
    cat_name = input("Cat's name: ").strip().title()
    gender = input("Cat's gender: ").strip().capitalize()
    age = int(input("Cat's age: "))
    breed = input("Cat's type/breed: ").strip().title()
    color = input("Cat's color: ").strip().title()

    stay_days = int(input("Stay Days: ").strip())
    price_per_day = int(input("[Price per day: ]").strip())

    owner_name = input("Owner's name: ").strip().title()
    owner_phone = input("Owner's phone: ").strip()

    new_cat = Cat(cat_name,gender,age,breed,color)
    new_hotel_stay = HotelStay(cat_name,stay_days,price_per_day)

    owner = check_owner(owner_name,owner_phone)

    if owner:
        owner.add_pet(new_cat)
        print(f"Added cat to existing owner: {owner_name}.")

    else:
        new_owner = Owner(owner_name,owner_phone,[new_cat])
        owners_list.append(new_owner)
        print("New owner registered.")

    pets_list.append(new_cat)
    stays_list.append(new_hotel_stay)
    print(f"Cat '{cat_name}' registered successfully.\n")


def renew_stay_pet():
    pet_name = (input("Enter pet's name: ").strip().title())
    renew_days = int(input("Enter days wanted to renew: ").strip())

    found = False
    for pet in stays_list:
        if pet.pet_name == pet_name:
            pet.days += renew_days
            print(f"Stay for pet '{pet_name}' renewed for {renew_days} more days.")
            print(f"New total: {pet.days} days | Total cost: {pet.total_cost}")
            found = True
            break

    if not found:
        print("Invalid pet name.")



def search_for_pet():
    pet_name = input("Enter pet name: ").strip().title()
    found = False

    for pet in pets_list:
        if pet.name == pet_name:
            print(f"Name: {pet.name}")
            print(f"Gender: {pet.gender}")
            print(f"Age: {pet.age}")
            print(f"Type: {pet.type}")

            if isinstance(pet, Cat):
                print(f"Color: {pet.color}")

            for stay in stays_list:
                if stay.pet_name == pet_name:
                    print(f"Days: {stay.days}")
                    print(f"Total Cost: {stay.total_cost} EGP")
            found = True
            break

    if not found:
        print("Invalid Pet name.")


    