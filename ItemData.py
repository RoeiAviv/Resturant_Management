from objects.Item import Item
import csv
import os

"Implement an ItemData class that handles operations related to item data." 
"It provides methods to save, load and retrieve item details from a CSV file." 
"The class interacts with the Item class to create and manipulate Item objects."

class ItemData:
    "Handling item data stored in a CSV file"
    def __init__(self, filename):
        self.filename = filename

    def save_info(self, items):
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'category', 'price', 'ingredients', 'reviews'])
            for item in items:
                reviews_str = ';'.join(item.reviews)
                writer.writerow([item.name, item.category, item.price, '.'.join(item.ingredients), reviews_str])

    def load_info(self):
        items = []
        if os.path.isfile(self.filename) and os.access(self.filename, os.R_OK):
            with open(self.filename, 'r', newline='') as file:
                reader = csv.reader(file)
                header = next(reader)  # Read and ignore the header row
                for row in reader:
                    if len(row)>=4:
                        name = row[0]
                        category = row[1]
                        price = float(row[2])
                        ingredients = [ingredient.strip() for ingredient in row[3].split(',')]
                        reviews = [] if len(row) < 5 else [r.strip() for r in row[4].split(';')]
                        item = Item(name, category, price, ingredients)
                        item.reviews = reviews
                        items.append(item)
        return items

    def get_item_by_name(self, item_name):
        items = self.load_info()
        for item in items:
            if item.name.lower() == item_name.lower():
                return item
        return None
