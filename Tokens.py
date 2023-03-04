class Token:
    def __init__(self, name, result):
        self.name = name
        self.result = result

    def drawing(self):
        print("A {} token was drawn from the bag".format(self.name))

    def present_result(self):
        print("The result of this token is: ", self.result)


# creating all numerical tokens first

Token("1", "1")
Token("1", "1")
Token("0", "0")
Token("0", "0")
Token("0", "0")
Token("-1", "-1")
Token("-1", "-1")
Token("-1", "-1")
Token("-2", "-2")
Token("-2", "-2")
Token("-3", "-3")
Token("-3", "-3")
Token("-4", "-4")
Token("-4", "-4")
Token("-5", "-5")
Token("-6", "-6")
Token("-8", "-8")
