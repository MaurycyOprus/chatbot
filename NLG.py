import random
import database_getter


class NLG:
    @staticmethod
    def answer(system_act):
        if system_act['sys_act'] == "recommend":
            if system_act["type"] in ["food", "drink", "sauce"]:
                if system_act["value"] is not None:
                    recommendations = database_getter.get_by_type(system_act["value"])
                    if len(recommendations) > 0:
                        return "Polecam: " + str(recommendations)
                    else:
                        return "Nie mamy takich pozycji w naszej restauracji."
                else:
                    if system_act["type"] == "food":
                        food_types = ["deser", "salatka", "makaron", "zupa", "danie", "pizza", "sniadanie"]
                        recommendations = database_getter.get_by_type(random.choice(food_types))
                        return "Polecam " + str(random.choice(recommendations))
                    elif system_act["type"] == "drink":
                        drink_types = ["kawa", "herbata", "cola", "sok", "woda", "piwo", "wino"]
                        recommendations = database_getter.get_by_type(random.choice(drink_types))
                        return "Polecam " + str(random.choice(recommendations))
                    else:
                        return "Nie potrafie ci pomoc. :("

        elif system_act['sys_act'] == 'bye':
            return "Do widzenia. Dziekuje za wspolprace"

        elif system_act['sys_act'] == "canthelp":
            return random.choice(["Nie potrafie ci pomoc :(", "Nie rozumiem", "Moglbym inaczej sformulowac swoja prosbe?"])

        else:
            return random.choice(["Nie potrafie ci pomoc :(", "Nie rozumiem", "Moglbym inaczej sformulowac swoja prosbe?"])
