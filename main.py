import json
from pprint import pprint


class Conflict:
    def __init__(self, a, b):
        self.a = a
        self.b = a
        self.pop = 0

    def add(self):
        self.pop += 1 

    def __repr__(self):
        return str(self.a) + ' - ' + str(self.b) + ':' + str(self.pop)
        

conflicts = []

with open('input.json') as f:
    data = json.load(f)
    rooms = data["rooms"]
    sessions = data["sessions"]
    people = data["people"]

    for sessionA in sessions:
        for sessionB in sessions:
            if sessionA != sessionB:
                # print(sessionA["id"])
                # print( sessionB["id"])
                newC = Conflict(sessionA["id"], sessionB["id"])
                conflicts.append(newC)

    for person in people:
        print(person)
        a_set = set(person["sessions"])
        for conflict in conflicts:
            if conflict.a in a_set and conflict.b in a_set:
                conflict.add()

pprint(conflicts)
