# spikeball game stat tracker
team1 = 0
team2 = 0


class GameRunner:
    print("new game")

    class Player:
        def __init__(self, name, spikes, aces, assists, saves, faults, errors):
            self.name = name
            self.spikes = spikes
            self.aces = aces
            self.assists = assists
            self.saves = saves
            self.faults = faults
            self.errors = errors

    p1 = Player("p1", 0, 0, 0, 0, 0, 0)
    p2 = Player("p2", 0, 0, 0, 0, 0, 0)
    p3 = Player("p3", 0, 0, 0, 0, 0, 0)
    p4 = Player("p4", 0, 0, 0, 0, 0, 0)
    print("team 1")
    p1.name = input("enter player 1: ")
    p2.name = input("enter player 2: ")
    print("team 2")
    p3.name = input("enter player 3: ")
    p4.name = input("enter player 4: ")

    score = int(input("score up to?: "))

    def box_stats(p1, p2, p3, p4):
        print("box stats | spk   ace   ast   save  err   flt")
        print('%8s' % p1.name + "    " + str(p1.spikes) + "     " + str(p1.aces) + "     " + str(p1.assists) +
              "     " + str(p1.saves) + "     " + str(p1.errors) + "     " + str(p1.faults))
        print('%8s' % p2.name + "    " + str(p2.spikes) + "     " + str(p2.aces) + "     " + str(p2.assists) +
              "     " + str(p2.saves) + "     " + str(p2.errors) + "     " + str(p2.faults))
        print('%8s' % p3.name + "    " + str(p3.spikes) + "     " + str(p3.aces) + "     " + str(p3.assists) +
              "     " + str(p3.saves) + "     " + str(p3.errors) + "     " + str(p3.faults))
        print('%8s' % p4.name + "    " + str(p4.spikes) + "     " + str(p4.aces) + "     " + str(p4.assists) +
              "     " + str(p4.saves) + "     " + str(p4.errors) + "     " + str(p4.faults))

    def point(p1, p2):  # point flow function
        SoA = input("spike[1] or ace[2]?: ")
        if SoA == '1':
            AoU = input("Assisted[1] or Unassisted[2]?: ")
            if AoU == '1':
                p1.spikes += 1
                p2.assists += 1
            elif AoU == '2':
                p1.spikes += 1
            else:
                print("invalid input")
        elif SoA == '2':
            p1.aces += 1
        else:
            print("invalid input")
        return SoA

    def error(p1):  # error flow function
        EoF = input("in game error[1] or serving fault[2]?: ")
        if EoF == '1':
            p1.errors += 1
        elif EoF == '2':
            p1.faults += 1
        else:
            print("invalid input")
        return EoF

    def deduct(p1):  # Zeeshan mechanic/deduction flow function
        stat = input("Spikes[1], Aces[2], Assists[3], Saves[4], Errors[5], or Faults[6]?")
        if stat == '1':
            p1.spikes -= 1
        elif stat == '2':
            p1.aces -= 1
        elif stat == '3':
            p1.assists -= 1
        elif stat == '4':
            p1.saves -= 1
        elif stat == '5':
            p1.errors -= 1
        elif stat == '6':
            p1.faults -= 1
        else:
            print("invalid input")
        return stat
        # Game loop
    while not ((team1 >= score or team2 >= score) and abs(team1 - team2) >= 2):
        print("score: " + p1.name + " and " + p2.name + ": " + str(
            team1) + "   " + p3.name + " and " + p4.name + ": " + str(team2))
        outcome = input("point[1], save[2], or error[3]?: ")
        if outcome == '1':  # point tracker
            pointAtt = input(p1.name + "[1], " + p2.name + "[2], " + p3.name + "[3], or " + p4.name + "[4]?: ")
            if pointAtt == '1':
                confirm = point(p1, p2)
                if confirm == '1' or confirm == '2':
                    team1 += 1
            elif pointAtt == '2':
                confirm = point(p2, p1)
                if confirm == '1' or confirm == '2':
                    team1 += 1
            elif pointAtt == '3':
                confirm = point(p3, p4)
                if confirm == '1' or confirm == '2':
                    team2 += 1
            elif pointAtt == '4':
                confirm = point(p4, p3)
                if confirm == '1' or confirm == '2':
                    team2 += 1
        elif outcome == '2':  # save tracker
            saveAtt = input(p1.name + "[1], " + p2.name + "[2], " + p3.name + "[3], or " + p4.name + "[4]?")
            if saveAtt == '1':
                p1.saves += 1
            elif saveAtt == '2':
                p2.saves += 1
            elif saveAtt == '3':
                p3.saves += 1
            elif saveAtt == '4':
                p4.saves += 1
            else:
                print("invalid input")
        elif outcome == '3':  # error tracker
            errorAtt = input(p1.name + "[1], " + p2.name + "[2], " + p3.name + "[3], or " + p4.name + "[4]? ")
            if errorAtt == '1':
                confirm = error(p1)
                if confirm == '1' or confirm == '2':
                    team2 += 1
            elif errorAtt == '2':
                confirm = error(p2)
                if confirm == '1' or confirm == '2':
                    team2 += 1
            elif errorAtt == '3':
                confirm = error(p3)
                if confirm == '1' or confirm == '2':
                    team1 += 1
            elif errorAtt == '4':
                confirm = error(p4)
                if confirm == '1' or confirm == '2':
                    team1 += 1
            else:
                print("invalid input")
        elif outcome == 'stats':  # stat check
            box_stats(p1, p2, p3, p4)
        elif outcome == 'd' or 'D' or '-':  # Redo/Zeeshan mechanic
            print("which player would you like to deduct stats from?")
            player = input(p1.name + "[1], " + p2.name + "[2], " + p3.name + " [3], or " + p4.name + "[4]? ")
            if player == '1':
                pointloss = deduct(p1)
                if pointloss == '1' or pointloss == '2':
                    team1 -= 1
                elif pointloss == '5' or pointloss == '6':
                    team2 -= 1
            if player == '2':
                pointloss = deduct(p2)
                if pointloss == '1' or pointloss == '2':
                    team1 -= 1
                elif pointloss == '5' or pointloss == '6':
                    team2 -= 1
            if player == '3':
                pointloss = deduct(p3)
                if pointloss == '1' or pointloss == '2':
                    team2 -= 1
                elif pointloss == '5' or pointloss == '6':
                    team1 -= 1
            if player == '4':
                pointloss = deduct(p4)
                if pointloss == '1' or pointloss == '2':
                    team2 -= 1
                elif pointloss == '5' or pointloss == '6':
                    team1 -= 1
        else:
            print("invalid input")
    if team1 > team2:
        print(p1.name + " and " + p2.name + " win!")
    else:
        print(p3.name + " and " + p4.name + " win!")
    print("final score: " + p1.name + " and " + p2.name + ": " + str(team1) + "   " + p3.name + " and " + p4.name + ": "
          + str(team2))
    box_stats(p1, p2, p3, p4)
