import dis

def test1():
    scoring = {
        "A": 1,
        "B": 2,
        "C": 3,
        "X": 1,
        "Y": 2,
        "Z": 3
    }

    scoring["A"]
    scoring["B"]
    scoring["Y"]
    scoring["A"]
    scoring["B"]
    scoring["Y"]
    scoring["A"]
    scoring["B"]
    scoring["Y"]

def test2():
    scoring_opp = ('A', 'B', 'C')
    scoring_player = ('X', 'Y', 'Z')

    scoring_opp.index('A')
    scoring_opp.index('B')
    scoring_player.index('Y')
    scoring_opp.index('A')
    scoring_opp.index('B')
    scoring_player.index('Y')
    scoring_opp.index('A')
    scoring_opp.index('B')
    scoring_player.index('Y')

dis.dis(test1)
dis.dis(test2)

# Pretty hard to beat a dictionary when it comes to KVP searches in python
# Not really anything faster
