class Token:
    def __init__(self, name, result):
        self.name = name
        self.result = result

    def drawing(self):
        print("A {} token was drawn from the bag".format(self.name))

    def present_result(self):
        print("The result of this token is: ", self.result)

class Bag:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def create_bag(self):
        if self.difficulty == "easy":
            Token("0", "0")



