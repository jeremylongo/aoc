from collections import deque


def game(playercount, rounds, debug=False):
    marble = deque([0])
    players = {}

    for i in range(0, playercount):
        players[i] = 0

    current_player = 0
    current_marble = 1

    for i in range(0, rounds):
        current_player += 1
        if current_player > playercount:
            current_player = 1
        if current_marble % 23 > 0:
            marble.rotate(-1)
            marble.append(current_marble)
        else:
            old_score = players[current_player - 1]
            players[current_player - 1] += current_marble
            marble.rotate(7)
            score2 = marble.pop()
            marble.rotate(-1)
            players[current_player - 1] += score2
            # if debug:
            # print("score : %s => %s (%s + %s)" % (old_score, players[current_player - 1], current_marble, score2))

        # if i % 10000 == 0:
        #     print("round %s" % i)
        if debug:
            print('[%s] ' % current_player + ' '.join([("(%s)" % m) if m == current_marble else ("%s" % m) for m in marble]))
        current_marble += 1

    maxscore = 0
    for i in range(0, playercount):
        if players[i] > maxscore:
            maxscore = players[i]
    print("score %s" % maxscore)

game(9, 25, True)
game(10, 1618)
game(13, 7999)
game(17, 1104)
game(21, 6111)
game(30, 5807)
game(419, 71052)
game(419, 7105200)

# nb lignes = nb round
# score inc toutes les 23 lignes de no ligne +
