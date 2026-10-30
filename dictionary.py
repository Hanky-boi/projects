def shop():
        local_corner_store = [
        {
            "name": "Sandwich",
            "price": 10.99,
            "department": "food",
            "desc": "A sandwich, freshly made right here."
        },
        {
            "name": "Arizona Iced Tea",
            "price": 0.99,
            "department": "food",
            "desc": "22 oz bottle of Arizona Iced Tea, price was the same for a long time."
        },
        {
            "name": "Mysterious Needle",
            "price": 19.99,
            "department": "misc",
            "desc": "Random needle i found in the back alley, do what you want with it."
        },
        {
            "name": "Baker Rifle",
            "price": 299.99,
            "department": "weapons",
            "desc": "The Baker rifle is a flintlock rifle used by the British Army during the Napoleonic Wars. It was known for its accuracy and range, making it a preferred weapon for sharpshooters."
        },
        {
            "name": "Terren",
            "price": 0.99,
            "department": "misc",
            "desc": "Terren is just a regular guy."
        },
        {
            "name": "Ratatouille",
            "price": 24.99,
            "department": "food",
            "desc": "Yes, the same one from the famous movie. This is a delicious French dish made from stewed vegetables, often including eggplant, zucchini, peppers, and tomatoes. Just hope theres no actual rat in there."
        },
        {
            "name": "Miraziz's shop",
            "price": 1.99,
            "department": "misc",
            "desc": "I stole his entire shop lol"
        },
        {
            "name": "trombone",
            "price": 1799.99,
            "department": "music",
            "desc": "A musical instrument, often used in orchestras and jazz bands. Very expensive."
        },
        {
            "name": "Robotic's class",
            "price": 0.00,
            "department": "misc",
            "desc": "A useless class for learning about robotics. Free of charge, it really sucks."
        },
        ]
        cart = []
        while True:
            def show_items(items):
                for index, item in enumerate(items):
                    print(index+1, item["name"])
            show_items(local_corner_store)
            x = int(input("Which item number do you want to buy? : \n"))
            print(local_corner_store[x-1]["name"])
            print(local_corner_store[x-1]["price"])
            print(local_corner_store[x-1]["desc"])
            ask = input("Do you want to add this item to your cart? (y/n) ")
            if ask.lower() == "y":
                selected_item = local_corner_store[x-1]
                cart.append(selected_item)
                print(f"Added {selected_item['name']} to cart.")
            elif ask.lower() == "n":
                print("Item not added to cart.")
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
            print("Current cart:")
            for item in cart:
                print(f"{item['name']} - ${item['price']}")
            print("Total cart value:", f"${sum(item['price'] for item in cart)}")
            checkout = input("Do you want to checkout? (y/n) ")
            if checkout.lower() == "y":
                total = sum(item['price'] for item in cart)
                print(f"ur total is: ${total}")
                print("Thank 4 monies lol")
                cart.clear()
                break
            elif checkout.lower() == "n":
                print("You have not checked out.")
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
            print()
shop()