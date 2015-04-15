import game


if __name__ == '__main__':
    cases = 20
    correct = 0

    for _ in range(cases):
        alice = game.Alice(test=True)
        bob = game.Bob()
        alicewin = bob.send_c(alice)
        if alicewin == (alice.move >= bob.move):
            correct += 1
        else:
            print alice.move, bob.move

    print '{} / {} Cases Passed'.format(correct, cases)
