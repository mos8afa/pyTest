import PetHotel

while True:
    print("========= Welcome to the Pet Hotel System =========")
    print("[1] Register a new Dog")
    print("[2] Register a new Cat")
    print("[3] Renew a pet stay")
    print("[4] Search for a pet by name")
    print("[5] Search for an owner by name")
    print("[6] Show all pets")
    print("[7] Show all owners")
    print("[8] Delete pet")
    print("[0] Exit")
    print("===================================================")
    
    try:
        choice = (input("Enter your choice: ")).strip()

        if choice == "1":
            PetHotel.register_new_dog()
        
        elif choice == "2":
            PetHotel.register_new_cat()
            
        elif choice == "3":
            PetHotel.renew_stay_pet()
            
        elif choice == "4":
            PetHotel.search_for_pet()
            
        elif choice == "5":
            PetHotel.search_for_owner()
            
        elif choice == "6":
            PetHotel.show_all_pets()
            
        elif choice == "7":
            PetHotel.show_all_owners()

        elif choice == "8":
            PetHotel.delete_pet()
            pass
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
    except:
        print("Invalid choice")

