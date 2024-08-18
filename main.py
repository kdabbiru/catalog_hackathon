import random

# Product Catalog
products = {
    1: {"name": "T-shirt", "size": "M", "style": "casual", "color": "blue", "price": 19.99, "category": "clothing", "description": "Comfortable cotton T-shirt, perfect for everyday wear."},
    2: {"name": "Jeans", "size": "32", "style": "slim fit", "color": "black", "price": 39.99, "category": "clothing", "description": "Stylish slim-fit jeans, ideal for a night out."},
    3: {"name": "Dress", "size": "S", "style": "formal", "color": "red", "price": 49.99, "category": "clothing", "description": "Elegant red dress, perfect for special occasions."},
    4: {"name": "Sneakers", "size": "9", "style": "athletic", "color": "white", "price": 59.99, "category": "footwear", "description": "High-performance sneakers for your active lifestyle."},
    5: {"name": "Backpack", "size": "L", "style": "casual", "color": "green", "price": 29.99, "category": "accessories", "description": "Spacious backpack for everyday use."},
    6: {"name": "Sunglasses", "size": "one size", "style": "trendy", "color": "black", "price": 14.99, "category": "accessories", "description": "Fashionable sunglasses to protect your eyes in style."},
    7: {"name": "Hoodie", "size": "L", "style": "casual", "color": "gray", "price": 34.99, "category": "clothing", "description": "Warm and cozy hoodie for chilly days."},
    8: {"name": "Boots", "size": "8", "style": "casual", "color": "brown", "price": 69.99, "category": "footwear", "description": "Durable and comfortable boots for outdoor adventures."},
    9: {"name": "Watch", "size": "one size", "style": "classic", "color": "silver", "price": 79.99, "category": "accessories", "description": "Timeless watch to complete your look."},
    10: {"name": "Hat", "size": "one size", "style": "casual", "color": "beige", "price": 9.99, "category": "accessories", "description": "Sun protection with a touch of style."},
    11: {"name": "Scarf", "size": "one size", "style": "trendy", "color": "multicolor", "price": 12.99, "category": "accessories", "description": "Colorful scarf to add a pop to your outfit."},
    12: {"name": "Belt", "size": "34", "style": "classic", "color": "brown", "price": 19.99, "category": "accessories", "description": "Leather belt for a polished look."},
    13: {"name": "Wallet", "size": "one size", "style": "minimalist", "color": "black", "price": 24.99, "category": "accessories", "description": "Slim and functional wallet for everyday carry."},
    14: {"name": "Socks", "size": "M", "style": "casual", "color": "assorted", "price": 7.99, "category": "clothing", "description": "Pack of comfortable socks for all-day wear."},
    15: {"name": "Tie", "size": "one size", "style": "formal", "color": "navy", "price": 29.99, "category": "accessories", "description": "Silk tie for professional attire."}
}

# User profile
user_profile = {
    "size": "",
    "preferred_styles": [],
    "virtual_cart": []
}

# Function to get user profile information
def get_user_profile():
    user_profile["size"] = input("Enter your size (e.g., S, M, L): ")

    while True:
        print("\nChoose your preferred styles (enter numbers separated by commas):")
        print("1. Casual")
        print("2. Streetwear")
        print("3. Formal")

        choices = input("Enter your choices: ")
        if choices:
            for choice in choices.split(','):
                choice = choice.strip()
                if choice == '1':
                    user_profile["preferred_styles"].append("casual")
                elif choice == '2':
                    user_profile["preferred_styles"].append("streetwear")
                elif choice == '3':
                    user_profile["preferred_styles"].append("formal")
            break
        else:
            print("Please enter at least one choice.")

# Function to search for products by ID
def search_products():
    # Display all products in the catalog
    print("\nProduct Catalog:")
    for id, product in products.items():
        print(f"{id}. {product['name']} - {product['description']} (Style: {product['style']}, Price: ${product['price']:.2f})")

    # Prompt the user to enter a product ID to search for
    product_id = input("\nEnter the product ID to view details or 'b' to go back: ")

    # Validate input and display product details if the ID is valid
    if product_id.isdigit():
        product_id = int(product_id)
        if product_id in products:
            product = products[product_id]
            print(f"\nProduct Details for ID {product_id}:")
            print(f"Name: {product['name']}")
            print(f"Size: {product['size']}")
            print(f"Style: {product['style']}")
            print(f"Color: {product['color']}")
            print(f"Price: ${product['price']:.2f}")
            print(f"Category: {product['category']}")
            print(f"Description: {product['description']}")
        else:
            print("Invalid product ID. Please try again.")
    elif product_id.lower() == 'b':
        return  # Go back to the main menu
    else:
        print("Invalid input. Please enter a valid product ID or 'b' to go back.")

# Function to get product recommendations based on user profile
def get_recommendations():
    print("\nRecommended Products:")
    for id, product in products.items():
        if (product["style"] in user_profile["preferred_styles"] or not user_profile["preferred_styles"]) and (product["size"] == user_profile["size"] or product["size"] == "one size"):
            print(f"{id}. {product['name']} - {product['description']} (Style: {product['style']}, Price: ${product['price']:.2f})")
    if not user_profile["preferred_styles"]:
        print("No style preferences set. Showing all products based on size.")

# Function to simulate trying on a product
def try_on(product_id):
    if product_id in products:
        product = products[product_id]
        feedback = [
            f"Product Name: {product['name']}",
            f"Style: {product['style']}",
            f"Color: {product['color']}",
            f"Price: ${product['price']:.2f}",
            "Try-on feedback: Looks great!"
        ]
        return feedback
    else:
        return ["Invalid product ID."]

# Function to add a product to the cart
def add_to_cart(product_id):
    if product_id in products:
        user_profile["virtual_cart"].append(product_id)
        print(f"Product ID {product_id} added to cart.")
    else:
        print("Invalid product ID. Please try again.")

# Function to remove a product from the cart
def remove_from_cart(product_id):
    if product_id in user_profile["virtual_cart"]:
        user_profile["virtual_cart"].remove(product_id)
        print(f"Product ID {product_id} removed from cart.")
    else:
        print("Product ID not in cart.")

# Function to view the cart
def view_cart():
    if user_profile["virtual_cart"]:
        print("\nYour Cart:")
        for product_id in user_profile["virtual_cart"]:
            product = products[product_id]
            print(f"ID: {product_id}, Name: {product['name']}, Price: ${product['price']:.2f}")
    else:
        print("Your cart is empty.")

# Function to checkout
def checkout():
    if user_profile["virtual_cart"]:
        total = sum(products[product_id]['price'] for product_id in user_profile["virtual_cart"])
        print(f"\nCheckout Summary:")
        print(f"Total amount: ${total:.2f}")
        print("Thank you for your purchase!")
        user_profile["virtual_cart"].clear()  # Clear the cart after checkout
    else:
        print("Your cart is empty. Add items to the cart before checking out.")

# Function to view the product catalog
def view_product_catalog():
    print("\nProduct Catalog:")
    for id, product in products.items():
        print(f"{id}. {product['name']} - {product['description']} (Style: {product['style']}, Price: ${product['price']:.2f})")

# Main function to run the user interaction
def main():
    print("Welcome to the Virtual Shopping Experience!")
    get_user_profile()

    while True:
        print("\nMenu:")
        print("1. Search products")
        print("2. Get recommendations")
        print("3. Try on a product")
        print("4. Add to cart")
        print("5. Remove from cart")
        print("6. View cart")
        print("7. Checkout")
        print("8. Exit")
        print("9. View Product Catalog")

        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            search_products()
        elif choice == '2':
            get_recommendations()
        elif choice == '3':
            product_id = int(input("Enter product ID to try on: "))
            if product_id in products:
                feedback = try_on(product_id)
                print("\nTry-On Feedback:")
                for item in feedback:
                    print(f"- {item}")
            else:
                print("Invalid product ID. Please try again.")
        elif choice == '4':
            product_id = int(input("Enter product ID to add to cart: "))
            add_to_cart(product_id)
        elif choice == '5':
            product_id = int(input("Enter product ID to remove from cart: "))
            remove_from_cart(product_id)
        elif choice == '6':
            view_cart()
        elif choice == '7':
            checkout()
        elif choice == '8':
            print("Thank you for visiting! Goodbye.")
            break
        elif choice == '9':
            view_product_catalog()
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    main()
