from fractions import gcd

from Crypto.Util import number


def mod_exp(base, ex, mod):
    result = 1
    base = base % mod

    while ex > 0:
        if ex % 2:
            result = (result * base) % mod
        ex = ex >> 1
        base = (base * base) % mod

    return result


def mod_inv(n, mod):
    n = n % mod
    t, newt = 0, 1
    r, newr = mod, n

    while newr != 0:
        q = r / newr
        tmp1, tmp2 = t, r

        t = newt
        newt = tmp1 - q * newt
        r = newr
        newr = tmp2 - q * newr

    if r > 1:
        return 0
    elif t < 0:
        return t + mod
    else:
        return t


class RSA():
    def __init__(self, modsize=1024):
        phiN = 0

        while gcd(65537, phiN) != 1:
            p, q = number.getPrime(modsize), number.getPrime(modsize)
            N, phiN = p * q, (p-1) * (q-1)

        e = 65537
        d = mod_inv(e, phiN)

        self.n, self.e, self.d = N, e, d

    def enc(self, m):
        return mod_exp(m, self.e, self.n)

    def dec(self, c):
        return mod_exp(c, self.d, self.n)
