# Order class
# Takes the user input and based on that changes the states of its attributes
# so the Cart class can do the right processing

class Order:

    def __init__(self):
        self.quit = False
        self.add = False
        self.delete = False
        self.item = None

    def get_input(self):
        print("[command] [item] [command is a to add, d to delete, q to quit]")
        line = input()
        command = line[:1] #access the input from user and extract first char which is the command
        self.item = line[2:] #extract the item using offset "2:" which is first letter

        if command == "a":
           self.add = True
        elif command == "d":
            self.delete = True
        elif command == "q":
            self.quit = True
