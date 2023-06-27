"The Item class represents an item with attributes such as" 
"name, category, price, ingredients, and reviews." 
"It provides methods to add reviews to the item and retrieve the list of reviews."

class Item:
    def __init__(self, name, category, price, ingredients):
        self.name = name
        self.category = category
        self.price = price
        self.ingredients = ingredients
        self.reviews = []  # List to store item reviews

    
    def add_review(self, review):
        self.reviews.append(review)

    def get_reviews(self):     
        return self.reviews



