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
                    recommendations = database_getter.get_by_type("food")
                    return "Polecam " + str(random.choice(recommendations))

        elif system_act['sys_act'] == 'bye':
            return "Do widzenia. Dziekuje za wspolprace"

        else:
            return random.choice["Nie rozumiem", "Moglbys to sformulowac to inaczej?", "Nie do konca zrozumialem"]
