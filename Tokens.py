class Token:
    def __init__(self, name, result):
        self.name = name
        self.result = result

    def drawing(self):
        print("A {} token was drawn from the bag".format(self.name))

    def present_result(self):
        print("The result of this token is: ", self.result)


# creating all 44 tokens

token_pool = [Token("1", "1"),
              Token("1", "1"),
              Token("1", "1"),
              Token("0", "0"),
              Token("0", "0"),
              Token("0", "0"),
              Token("0", "0"),
              Token("-1", "-1"),
              Token("-1", "-1"),
              Token("-1", "-1"),
              Token("-1", "-1"),
              Token("-1", "-1"),
              Token("-2", "-2"),
              Token("-2", "-2"),
              Token("-2", "-2"),
              Token("-2", "-2"),
              Token("-3", "-3"),
              Token("-3", "-3"),
              Token("-3", "-3"),
              Token("-4", "-4"),
              Token("-4", "-4"),
              Token("-5", "-5"),
              Token("-5", "-5"),
              Token("-6", "-6"),
              Token("-7", "-7"),
              Token("-8", "-8"),
              Token("Skull", "Scenario Based"),
              Token("Skull", "Scenario Based"),
              Token("Skull", "Scenario Based"),
              Token("Skull", "Scenario Based"),
              Token("Cultist", "Scenario Based"),
              Token("Cultist", "Scenario Based"),
              Token("Cultist", "Scenario Based"),
              Token("Cultist", "Scenario Based"),
              Token("Elder Thing", "Scenario Based"),
              Token("Elder Thing", "Scenario Based"),
              Token("Elder Thing", "Scenario Based"),
              Token("Elder Thing", "Scenario Based"),
              Token("Tablet", "Scenario Based"),
              Token("Tablet", "Scenario Based"),
              Token("Tablet", "Scenario Based"),
              Token("Tablet", "Scenario Based"),
              Token("Elder Sign", "Reference the investigator's ability"),
              Token("Auto-fail", "Automatic failure")]

token_pool[42].drawing()
token_pool[42].present_result()
