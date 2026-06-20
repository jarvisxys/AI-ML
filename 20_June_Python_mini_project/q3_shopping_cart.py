# Aditya Kumar (20 June)

# Part A - Spot the Bug

def add_item_buggy(item, cart=[]):
    cart.append(item)
    return cart


print("Part A Output:")
print(add_item_buggy("apple"))
print(add_item_buggy("banana"))
print(add_item_buggy("milk", cart=["bread"]))
print(add_item_buggy("eggs"))

# Explanation:
# The default list cart=[] is created only once.
# So apple, banana and eggs use the same list again and again.


# Part B - Fixed Function

def add_item(item, cart=None):
    if cart is None:
        cart = []

    cart.append(item)
    return cart


print("\nPart B Output:")
print(add_item("apple"))
print(add_item("banana"))


# Part C - Shopping Cart Program

def create_cart(owner, discount=0):
    return {
        "owner": owner,
        "items": [],
        "discount": discount
    }


def add_to_cart(cart, name, price, qty=1):
    item = {
        "name": name,
        "price": price,
        "qty": qty
    }

    cart["items"].append(item)


def update_price(price_tuple, new_price):
    try:
        price_tuple[1] = new_price
    except TypeError:
        print("TypeError: Tuple cannot be changed because tuple is immutable")


def calculate_total(cart):
    total = 0

    for item in cart["items"]:
        total += item["price"] * item["qty"]

    discount_amount = total * cart["discount"] / 100
    final_total = total - discount_amount

    return final_total


cart1 = create_cart("Aarav", 10)
cart2 = create_cart("Riya")

add_to_cart(cart1, "Apple", 30, 2)
add_to_cart(cart1, "Milk", 50, 1)

add_to_cart(cart2, "Bread", 40, 2)
add_to_cart(cart2, "Butter", 80, 1)

print("\nPart C Output:")
print("Cart 1:", cart1)
print("Cart 2:", cart2)

print("Total of Cart 1:", calculate_total(cart1))
print("Total of Cart 2:", calculate_total(cart2))

price_tuple = ("Apple", 30)
update_price(price_tuple, 40)


# Discussion Points:

# 1. discount=0 is safe because int is immutable.
#    cart=[] is dangerous because list is mutable and the same list is reused.

# 2. Rebinding means assigning a variable to a new object.
#    Mutating means changing the same object without creating a new one.

# 3. Mutable: list, dict, set
#    Immutable: tuple, str, int

# 4. Yes, when we pass a list into a function and modify it,
#    changes reflect outside because list is mutable and passed by object reference.
