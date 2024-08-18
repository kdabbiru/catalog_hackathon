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
        style = input("Enter a preferred style (or 'done' to finish): ")
        if style.lower() == 'done':
            break
        user_profile["preferred_styles"].append(style)

# Function to simulate the try-on experience 
def try_on(product_id):
    product = products[product_id]
    feedback = []

    # Size, style, price & category feedback 
    if product["size"] == user_profile["size"]:
        feedback.append("The item fits you perfectly!")
    elif product["size"] < user_profile["size"]:
        feedback.append("You might need a larger size.")
    else:
        feedback.append("You might need a smaller size.")

    if product["style"] in user_profile["preferred_styles"]:
        feedback.append("This style matches your preferences!")

    if product["price"] < 30:
        feedback.append("This is a great deal!")
    elif product["price"] > 50:
        feedback.append("This is a premium item.")

    if product["category"] == "clothing":
        feedback.append("Imagine how stylish you'll look in this!")
    elif product["category"] == "footwear":
        feedback.append("These will definitely up your shoe game!")

    return feedback

# Function to provide recommendations 
def get_recommendations():
    filtered_products = [id for id, product in products.items() if product["style"] in user_profile["preferred_styles"]]
    
    if filtered_products:
        recommended_products = random.sample(filtered_products, min(2, len(filtered_products))) 
        print("\nRecommended products for you:")
        for id in recommended_products:
            print(f"{id}. {products[id]['name']}")
    else:
        print("\nNo recommendations based on your preferred styles at the moment.")

# Function to add/remove items from the virtual cart & view it
def add_to_cart(product_id):
    if product_id in products:
        user_profile["virtual_cart"].append(product_id)
        print(f"{products[product_id]['name']} added to your cart!")
    else:
        print("Invalid product ID. Please try again.")

def remove_from_cart(product_id):
    if product_id in user_profile["virtual_cart"]:
        user_profile["virtual_cart"].remove(product_id)
        print(f"{products[product_id]['name']} removed from your cart!")
    else:
        print("Item not found in your cart.")

def view_cart():
    if user_profile["virtual_cart"]:
        print("\nYour Cart:")
        for id in user_profile["virtual_cart"]:
            print(f"- {products[id]['name']} (${products[id]['price']:.2f})")
    else:
        print("\nYour cart is empty.")

# Function to search for products by keyword
def search_products(keyword):
    matching_products = []
    for id, product in products.items():
        if keyword.lower() in product["name"].lower() or keyword.lower() in product["style"].lower() or keyword.lower() in product["category"].lower():
            matching_products.append(id)

    if matching_products:
        print("\nMatching products:")
        for id in matching_products:
            print(f"{id}. {products[id]['name']}")
    else:
        print("\nNo products found matching your search.")

# Function to calculate the total price & simulate checkout
def calculate_total_price():
    total = 0
    for id in user_profile["virtual_cart"]:
        total += products[id]["price"]
    return total

def checkout():
    if user_profile["virtual_cart"]:
        total_price = calculate_total_price()
        print("\nCheckout Summary:")
        view_cart()
        print(f"\nTotal Price: ${total_price:.2f}")

        while True:
            confirm = input("Confirm checkout? (y/n): ")
            if confirm.lower() == 'y':
                print("Thank you for shopping with us!")
                user_profile["virtual_cart"] = []  
                break
            elif confirm.lower() == 'n':
                print("Checkout cancelled.")
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

# Main function to run the user interaction
def main():
    print("Welcome to the Virtual Shopping Experience!")
    get_user_profile()

    while True:
        print("\nMenu:")
        print("1. Try on a product")
        print("2. Get recommendations")
        print("3. Add to cart")
        print("4. Remove from cart")
        print("5. View cart")
        print("6. Search products")
        print("7. Checkout")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            product_id = int(input("Enter product ID to try on: "))
            if product_id in products:
                feedback = try_on(product_id)
                print("\nTry-On Feedback:")
                for item in feedback:
                    print(f"- {item}")
            else:
                print("Invalid product ID. Please try again.")
        elif choice == '2':
            get_recommendations()
        elif choice == '3':
            product_id = int(input("Enter product ID to add to cart: "))
            add_to_cart(product_id)
        elif choice == '4':
            product_id = int(input("Enter product ID to remove from cart: "))
            remove_from_cart(product_id)
        elif choice == '5':
            view_cart()
        elif choice == '6':
            keyword = input("Enter keyword to search for products: ")
            search_products(keyword)
        elif choice == '7':
            checkout()
        elif choice == '8':
            print("Thank you for visiting! Goodbye.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
