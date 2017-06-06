class Inventory:
    def __init__(self):
        self.bag_of_holding = []
        pass

    def put_in(self, item):
        '''This method will add an item object to inventory, although  '''
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
        if item_to_be_popped in self.bag_of_holding:
            self.bag_of_holding.remove(item_to_be_popped)