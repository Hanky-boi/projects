# shopping_cart.py
# A simple console-based shopping cart system in Python

class Product:
    """Represents a product in the store."""
    def __init__(self, name: str, price: float):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"


class ShoppingCart:
    """Represents the user's shopping cart."""
    def __init__(self):
        self.items = []  # List of tuples (Product, quantity)

    def add_product(self, product: Product, quantity: int = 1):
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        self.items.append((product, quantity))
        print(f"Added {quantity} x {product.name} to cart.")

    def remove_product(self, product_name: str):
        for i, (product, qty) in enumerate(self.items):
            if product.name.lower() == product_name.lower():
                del self.items[i]
                print(f"Removed {product.name} from cart.")
                return
        print("Product not found in cart.")

    def view_cart(self):
        if not self.items:
            print("Your cart is empty.")
            return
        print("\n--- Shopping Cart ---")
        total = 0
        for product, qty in self.items:
            subtotal = product.price * qty
            total += subtotal
            print(f"{product.name} x {qty} = ${subtotal:.2f}")
        print(f"Total: ${total:.2f}\n")

    def checkout(self):
        if not self.items:
            print("Your cart is empty. Cannot checkout.")
            return
        self.view_cart()
        print("Thank you for shopping!")
        self.items.clear()


def main():
    # Sample products
    store_products = [

    ]

    cart = ShoppingCart()

    while True:
        print("\n--- Store Menu ---")
        print("A. View Products")
        print("B. Add to Cart")
        print("C. Remove from Cart")
        print("D. View Cart")
        print("E. Checkout")
        print("F. Exit")

        choice = input("Enter choice (A-F): ").strip()

        while True:
            if choice.upper() == "A":
                print("\n--- Available Products ---")
                for idx, product in enumerate(store_products, start=1):
                    print(f"{idx}. {product.name} - ${product.price:.2f}")

            elif choice.upper() == "B":
                idx = input("Enter product number to add: ").strip()
                qty = input("Enter quantity: ").strip()
                if not idx.isdigit() or not qty.isdigit():
                    print("Invalid input. Please enter numbers only.")
                    continue
                idx, qty = int(idx), int(qty)
                if 1 <= idx <= len(store_products):
                    cart.add_product(store_products[idx - 1], qty)
                else:
                    print("Invalid product number.")

            elif choice.upper() == "C":
                name = input("Enter product name to remove: ").strip()
                cart.remove_product(name)

            elif choice.upper() == "D":
                cart.view_cart()

            elif choice.upper() == "E":
                cart.checkout()

            elif choice.upper() == "F":
                print("Exiting... Goodbye!")
                break

            else:
                print("Invalid choice. Please select A-F.")
if __name__ == "__main__":
    main()
