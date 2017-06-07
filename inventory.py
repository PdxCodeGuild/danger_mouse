class Inventory:
    def __init__(self, owner):
        """The most complex object in this game is the inventory object as seen below.
        a full description of it's characteristics and functions can be found in the read
        me"""
        self.bag_of_holding = []
        self.owner = owner

    def put_in(self, item):
        """This method will add an item object to inventory, although"""
        try:
            self.bag_of_holding.append(item)
            print("You have added {} to your inventory.".format(item))
        except:
            print('Error in Inventory method: put_in')

    def put_in_quiet(self, item):
        """This method will add an item object to inventory, although"""
        try:
            self.bag_of_holding.append(item)
        except:
            print('Error in Inventory method: put_in')

    def check_inventory(self, check_word):
        """Quick method to check if an item exists in inventory, returns boolean
        value to call."""
        is_there = False
        if check_word in self.bag_of_holding:
            is_there = True

        return is_there

    def list_inventory(self):
        print("You're inventory contains: ")
        """Displays inventory of object to console, excludes spells that have been cast."""

        print('You\'re inventory contains:')
        i = 1
        inv_dict = {}
        for item in self.bag_of_holding:
            if 'casted' not in item.name:
                inv_dict[str(i)] = item
        return inv_dict

    def poplar(self, item_to_be_popped):
        """Checks for existence of item in inventory, if item exists poplar pops that item."""
        if self.check_inventory(item_to_be_popped):
            als_lament = item_to_be_popped     # ;P
            self.bag_of_holding.remove(item_to_be_popped)
        else:
            # for testing porpoises if the item is not in dah bag, remove later.
            print(" {} was not found in bag of holding.".format(item_to_be_popped))
            return None
        return als_lament
