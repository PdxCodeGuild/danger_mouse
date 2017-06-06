class Inventory:
    def __init__(self):
        self.bag_of_holding = []
        pass

    def put_in(self, item):
        '''This method will add an item object to inventory, although'''
        try:
            self.bag_of_holding.append(item)
            print("You have added {} to your inventory.".format(item))
        except:
            print('Error in Inventory method: put_in')


    def check_inventory(self, check_word):
        is_there = False
        if check_word in self.bag_of_holding:
            is_there = True

        return is_there

    def list_inventory(self):
        print('You\'re inventory contains:')
        for item in self.bag_of_holding:
            print(item)

    def poplar(self, item_to_be_popped):
        if self.check_inventory(item_to_be_popped) == True:
            als_lament = item_to_be_popped     # ;P
            self.bag_of_holding.remove(item_to_be_popped)
        else:
            # for testing porpoises if the item is not in dah bag, remove later.
            print(" {} was not found in bag of holding.".format(item_to_be_popped))
            return None
        return als_lament
