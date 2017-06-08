# Creates an inventory with a list and an owner
# {{
class Inventory:
    def __init__(self, owner):
        """The most complex object in this game is the inventory object as seen below.
        a full description of it's characteristics and functions can be found in the read
        me"""
        self.bag_of_holding = []
        self.owner = owner

    
    # Tries to put an item into the list, and prints a message
    # {{
    def put_in(self, item):
        """This method will add an item object to inventory, although"""
        try:
            self.bag_of_holding.append(item)
            print("You have added {} to your inventory.".format(item))
        except:
            print('Error in Inventory method: put_in')
    # }}


    # Tries to put in without printing anything. Will print on error
    # {{
    def put_in_quiet(self, item):
        """This method will add an item object to inventory, although"""
        try:
            self.bag_of_holding.append(item)
        except:
            print('Error in Inventory method: put_in')
    # }}

    # Takes in a search word. If the search word matches an inventory
    # item's name string, then it returns true. Otherwise it returns
    # false 
    # {{
    def check_inventory(self, check_word):
        """Quick method to check if an item exists in inventory, returns boolean
        value to call."""
        is_there = False
        for item in self.bag_of_holding:
            if check_word == item.name:
                is_there = True

        return is_there
    # }}



    # This will create an empty list. If there is food in the inventory,
    # it adds it to the list. Then it randomly outputs one food
    # object
    # {{
    def look_for_food(self):
        food = []
        for item in self.bag_of_holding:
            if type(item) is item.Food:
                food.append(item)
        if food:
            return food[randrange(0, len(food))]
        return ""
    # }}

    # {{
    def list_inventory(self):
        """Displays inventory of object to console, excludes spells that have been cast."""

        print('You\'re inventory contains:')
        #i = 1
        #inv_dict = {}
        for item in self.bag_of_holding:
            if 'casted' not in item.name:
                try:
                    print(item.name)
                except:
                    pass

                #inv_dict[str(i)] = item
                #i += 1
        #return inv_dict
    # }}

    # {{
    def poplar(self, item_to_be_popped):
        """Checks for existence of item in inventory, if item exists poplar pops that item and returns
        as als_lament"""
        if self.check_inventory(item_to_be_popped): # Basic check to see if it's in the list
            als_lament = item_to_be_popped# ;P
            for an_item in self.bag_of_holding:     # here we are extracting an the index of the object in the list
                if self.check_inventory(item_to_be_popped):
                    index = self.bag_of_holding.index(an_item)
            # and here is where the majic happens and the item is removed from the list.
            self.bag_of_holding.remove(self.bag_of_holding[index])
        else:
            # for testing porpoises if the item is not in dah bag, remove later.
            print(" {} was not found in bag of holding.".format(item_to_be_popped))
            return None
        return als_lament
    # }}


    # {{
    def look(self, item_to_be_described):
        """This method simply displays the description attached to an item when supplied
        with the item."""
        for item in self.bag_of_holding:
            if item_to_be_described == item.name:
                print('{}'.format(item.description))
    # }}
