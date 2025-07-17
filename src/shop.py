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

        # Method to delete a sweet by its ID
    def delete_sweet(self, sweet_id):
        # Filter out the sweet with the given ID
        self.sweets = [s for s in self.sweets if s.id != sweet_id]

        # Method to view all sweets
    def view_sweets(self):
        return self.sweets

        # Method to search sweets by partial name match (case-insensitive)
    def search_by_name(self, name):
         return [s for s in self.sweets if name.lower() in s.name.lower()]

         # Method to search sweets by exact category match (case-insensitive)

    def search_by_category(self, category):
        return [s for s in self.sweets if
                category.lower() == s.category.lower()]