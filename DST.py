import json


class DST:
    def __init__(self):
        # self.data = json.load(open('data.json'))
        self.slots = self.init_slots()
        self.act = None

    def update_user(self, nlu=None):
        self.act = nlu['act']
        for slot, value in nlu['slots']:
            self.slots[self.act][slot] = value

        return self.act

    @staticmethod
    def init_slots():
        return dict(book={}, order={}, payment={}, recommend={})

    def get_slots(self):
        return self.slots

    def get_values(self):
        return self.act, self.slots
