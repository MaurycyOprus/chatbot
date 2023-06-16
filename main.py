from NLG import NLG
from NLU import nlu
from DST import DST
from DP import DP
import HELP

if __name__ == "__main__":

    # init
    dst = DST()
    nlg = NLG()
    dp = DP()

    while True:
        user = input("User: ")
        if user == "help":
            HELP.get_help()
        else:
            nlu_out = nlu(user)
            print(nlu_out)
            dst.update_user(nlu_out)
            act, slots = dst.get_values()
            print(act, slots)
            system_update = dp.update_bot(act, slots)
            print(system_update)
            answer = nlg.answer(system_update)
            print("Zbigniew: ", answer)

    # if act == "bye":
    #     break
