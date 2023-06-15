from NLG import NLG
from NLU import nlu
from DST import DST
from DP import DP

if __name__ == "__main__":

    # init
    dst = DST()
    nlg = NLG()
    dp = DP()

    # while True:
    #     user = input("User: ")
    #     nlu_out = nlu(user)
    #     dst.update(nlu_out)
    #     print(nlu_out)
    #     print(dst.get_state)
    #     print(dst.get_slots)
    #     # print("Stefan: ", nlg())

    user = "jakie pizze polecasz"
    nlu_out = nlu(user)
    print(nlu_out)
    dst.update_user(nlu_out)
    act, slots = dst.get_values()
    print(act, slots)
    system_update = dp.update_bot(act, slots)
    print(system_update)
    answer = nlg.answer(system_update)
    print("Stefan: ", answer)

    # if act == "bye":
    #     break
