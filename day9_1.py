def game(playercount, rounds, debug=False):
    marble = [0]
    players = {}

    for i in range(0, playercount):
        players[i] = 0

    current_player = 0
    idx = 0
    current_marble = 1

    for i in range(0, rounds):
        current_player += 1
        if current_player > playercount:
            current_player = 1
        if current_marble % 23 > 0:
            idx = idx + 2
            while idx > len(marble):
                idx -= len(marble)
            marble.insert(idx, current_marble)
        else:
            players[current_player - 1] += current_marble
            idx = idx - 7
            while idx < 0:
                idx += len(marble)
            players[current_player - 1] += marble.pop(idx)
            while idx > len(marble):
                idx -= len(marble)

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
#game(419, 7105200)
