class Sweet:
    def __init__(self, id, name, category, price, quantity):
        # Initialize sweet properties
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity


    def __repr__(self):
        # Provide a readable string representation of the sweet
        return f"{self.id} {self.name} {self.category} {self.price} {self.quantity}"


# Define a class to represent the Sweet Shop
class SweetShop:
    def __init__(self):
        # Initialize the shop with an empty list of sweets
        self.sweets = []

    # Method to add a new sweet
    def add_sweet(self, sweet):
        # Check for duplicate sweet ID
        if any(s.id == sweet.id for s in self.sweets):
            raise ValueError("Sweet with this ID already exists.")
        # Add the sweet to the list
        self.sweets.append(sweet)

        # Method to view all sweets
    def view_sweets(self):
        return self.sweets