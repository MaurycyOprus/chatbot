from collections import defaultdict
import jmespath
import json


class DP:
    @staticmethod
    def update_bot(act, slots):
        type_name = next(iter(slots[act]))
        name_val = slots[act][next(iter(slots[act]))]
        name = None
        if act == "order":
            return {"sys_act": "order", "type": type_name, "value": name}

        elif act == "recommend":
            if name_val in ["pizza", "pizze"]:
                name = "pizza"
            if name_val in ["makaron", "makarony"]:
                name = "makaron"
            if name_val in ["salatka", "salatke", "salatki"]:
                name = "salatka"
            if name_val in ["deser", "desery"]:
                name = "deser"
            return {"sys_act": "recommend", "type": type_name, "value": name}

        # elif act == "book":


        elif act == "book":
            return {"sys_act": "welcomemsg"}

        elif act == "hello":
            return {"sys_act": "welcomemsg"}

        elif act == "bye":
            return {"sys_act": "byemsg"}

        else:
            return {"sys_act": "canthelp"}

                    
