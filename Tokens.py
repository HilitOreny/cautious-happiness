class Token:
    def __init__(self, name, result):
        self.name = name
        self.result = result

    def drawing(self):
        print("A {} token was drawn from the bag".format(self.name))

    def present_result(self):
        print("The result of this token is:", self.result)


class PlusOneToken(Token):
    def __init__(self):
        super().__init__(name="1", result="1")


class ZeroToken(Token):
    def __init__(self):
        super().__init__(name="0", result="0")


class MinusOneToken(Token):
    def __init__(self):
        super().__init__(name="-1", result="-1")


class MinusTwoToken(Token):
    def __init__(self):
        super().__init__(name="-2", result="-2")

class MinusThreeToken(Token):
    def __init__(self):
        super().__init__(name="-3", result="-3")


token_pool = [PlusOneToken(), PlusOneToken(), PlusOneToken(),
              ZeroToken(), ZeroToken(), ZeroToken(), ZeroToken(),
              MinusOneToken(), MinusOneToken(), MinusOneToken(), MinusOneToken(), MinusOneToken(),
              MinusTwoToken(), MinusTwoToken(), MinusTwoToken(), MinusTwoToken(),
              MinusThreeToken(), MinusThreeToken(), MinusThreeToken(),
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

token_pool[16].drawing()