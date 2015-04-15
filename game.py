
from Crypto.Random import random
from Crypto.Util import number


import rsa


class Move():
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


def get_user_move():
    convert = {
        'rock': Move.ROCK,
        'paper': Move.PAPER,
        'scissors': Move.SCISSORS
    }

    while True:
        userin = raw_input('Please enter a move: ')
        if userin.lower() in convert.keys():
            return convert[userin.lower()]


class Alice():
    def __init__(self, test=False):
        if test:
            self.move = random.randint(0, 2)
        else:
            self.move = get_user_move()
        self.rsa = rsa.RSA(1024)

    def get_c(self, c, target):
        ys = []

        for i in range(10):
            c_i = c + i
            ys.append(self.rsa.dec(c_i))

        p = number.getPrime(256)
        zs = map(lambda y: y % p, ys)

        sent_zs = zs[:self.move+1]
        sent_zs += map(lambda z: z + 1, zs[self.move+1:])
        return target.get_zs(sent_zs, p)


class Bob():
    def __init__(self):
        self.move = random.randint(Move.ROCK, Move.SCISSORS)

    def send_c(self, target):
        self.x = random.getrandbits(512)
        c = target.rsa.enc(self.x)
        return target.get_c(c - self.move, self)

    def get_zs(self, zs, p):
        z_j = zs[self.move]
        G = self.x % p
        return z_j == G

if __name__ == '__main__':
    alice = Alice()
    bob = Bob()
    alicewin = bob.send_c(alice)
    print 'Alice played: {}\nBob played: {}'.format(alice.move, bob.move)
    print ('Alice' if alicewin else 'Bob') + ' wins.'
