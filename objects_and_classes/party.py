class Party:
    def __init__(self):
        self.people = []


party = Party()
while True:
    line = input()
    if line == "End":
        people = ", ".join(party.people)
        print(f"Going: {people}")
        print(f"Total: {len(party.people)}")
        break
    party.people.append(line)
