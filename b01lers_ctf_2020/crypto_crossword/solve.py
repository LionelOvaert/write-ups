from sympy import init_printing
from sympy import Matrix

init_printing()

alphabet_length = 26


def decrypt(matrix, words):
    cipher = ""
    M = Matrix(matrix)
    M = M.inv_mod(alphabet_length)
    length = len(M)
    d = {}
    d2 = {}
    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for x in range(len(alph)):
        d[alph[x]] = x
        d2[x] = alph[x]
    # print d
    count = 0
    l = []

    for ch in words:
        if (count + 1) % (5 + 1) == 0:
            m = Matrix(l)
            dot_pr_m = M * m
            n = []
            for i in dot_pr_m:
                cipher += d2[i % alphabet_length]
            count = 0
            l = []
        l.append(d[ch])
        count += 1
    if (count + 1) % (5 + 1) == 0:
        m = Matrix(l)
        dot_pr_m = M * m
        n = []
        for i in dot_pr_m:
            cipher += d2[i % alphabet_length]
    return cipher


if __name__ == "__main__":
    secret = [
        [13, 19, 23, 0, 2],
        [22, 7, 8, 11, 4],
        [14, 17, 3, 4, 17],
        [7, 4, 0, 17, 19],
        [2, 4, 17, 19, 18],
    ]
    ciphertext = "WKYQMRKNQLMESZLBSTIKSIPTSLELQLEFEHZZQPNBEZKNOTKJVDHWWRVAULIHXUTYUIHCJMEIXTHDVWCANBMHS"
    print(ciphertext)

print(decrypt(secret, ciphertext))
# MESSAGEXISXNOXBLACKXSQUARESXAMIGOXSEPARATEDXBYXSPACEXANDXENCLOSEDXINXTHEXUSUALXFORMAT
# MESSAGE IS NO BLACK SQUARES AMIGO SEPARATED BY SPACE AND ENCLOSED IN THE USUAL FORMAT
