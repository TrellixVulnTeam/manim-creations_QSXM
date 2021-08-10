from fractions import Fraction

b = 1
# half
h = 1 / 2
# thirds
t = Fraction(b, 3)
# two thirds
tt = 2 * t


A = [
    [("7", [4*b])],
    [("7 4' 7 0'", [t, b + tt, b, b])],
    [("4' 8 8", [tt, t, 3 * b])],
    [("8", [4 * b])],
    [("9", [4 * b])],
    [("9 10 11 4' 7 6 5 1'", [tt, t, tt, t, tt, t, tt, t])],
    [("0' 4 4", [tt, t, 3 * b])],
    [("4", [4 * b])],
]

B = [
    [("9 0' 0'", [tt, t, 3 * b])],
    [("4' 5 9 0'", [t, b + tt, b, b])],
    [("4' 9 9", [tt, b + t, 2*b])],
    [("9", [4*b])],
    [("9 0' 0'", [tt, t, 3 * b])],
    [("4' 6 9 0'", [t, b + tt, b, b])],
    [("4' 9 9", [tt, t, 3*b])],
    [("9 8", [2*b, 2*b])],
]

A_prime = [
    [("7", [4*b])],
    [("7 4' 7 0'", [t, b + tt, b, b])],
    [("4' 8 8", [tt, t, 3 * b])],
    [("8", [4 * b])],
    [("9", [4 * b])],
    [("9 10 11 4' 7 6 5 1'", [tt, t, tt, t, tt, t, tt, t])],
    [("0' 4 5 6", [t, b + tt, b, b])],
    [("7 9 11 0' R 0", [tt, t, tt, t, b, b])],
]

take_the_a_train = [
        *A,
        *B,
        *A_prime
]

A = [
    [("7' 5' 9 0' 4'", [tt, t, tt, t, 2*b])],
    [("7' 5' 9 0' 4'", [tt, t, tt, t, 2*b])],
    [("7' 5' 9 0' 4' 4'", [tt, t, tt, t, b, b])],
    [("4' 4' 2' 0' 9", [2*b, tt, t, tt, t])],
    [("0' 0' 0'", [b,b,2*b])],
    [("0' 4' 2' 0' 9", [2*b, tt, t, tt, t])],
    [("0'", [4*b])],
    [("0' R", [2*b, 2*b])],
]

B = [
    [("0' 2'", [2*b, 2*b])],
    [("3' 4'", [2*b, 2*b])],
    [("R 5' 7' 5' 7'", [b, tt, b, t, b])],
    [("8' 7' 5'", [b, tt, 2*b + t])],
    [("2' 4'", [2*b, 2*b])],
    [("5' 6'", [2*b, 2*b])],
    [("R 7' 9' 7' 9'", [b, tt, b, t, b])],
    [("10' 9' 7'", [b, tt, 2*b + t])],
]

honey_suckle_rose = [
    *A, *A, *B, *A
]

A = [
    [("R 7 0' R 11 R 9 7", [b, tt, t, tt, t, tt, t])],
    [("7 9 4 5", [b, b, b, b])],
    [("7 0' 11 0'", [b, b, b, b])],
    [("R", [4*b])],
]

B = [
    [("4' 5' 7'", [2*b, b + tt, t])],
    [("R", [4 * b])],
    [("5' 4' 2'", [2*b, b + tt, t])],
    [("R", [4*b])],
]

C = [
    [("4' 2'", [2*b, 2*b])],
    [("0' 9", [b + tt, t + 2*b])],
    [("7 0' 11 0'", [b, b, b, b])],
    [("R", [4*b])],
]

st_thomas = [
        *A, *A, *B, *C
]

A = [
    [("9 11 0' 2'", [b, b, b, b])],
    [("4' 7' 2' 0'", [b, b, b, b])],
    [("2'", [4*b])],
    [("2' R 4'", [2*b, tt, t + b ])],
    [("0' 2' 4' 7'", [b, b, b, b])],
    [("9' 0'' 9' 7'", [b, b, b + tt, t])],
    [("9'", [4*b])],
    [("9' 7'", [3*b, b])],
]

there_will_never_be_another_you = [
    *A,
    [("0'' 9' 7' 5'", [b, b, b, b])],
    [("4' 2' 4' 5'", [b, b, b, b])],
    [("7' 4' 2' 0'", [b, b, b, b])],
    [("2' 0' 2' 0'", [b, tt, t + b, b])],
    [("11' 9' 7' 6'", [b, b, b, b])],
    [("4' 2' 4' 2'", [b, b, b, b])],
    [("5'", [4*b])],
    [("5' 7',", [3*b, b])],
    *A,
    [("0'' 9' 7' 5'", [b, b, b, b])],
    [("4' 2' 4' 5'", [b, b, b, b])],
    [("7' 4' 2' 0' 11", [b, b, b, tt, t])],
    [("11 R 9", [2*b, tt, t + b])],
    [("7' 0'' 11' 9'", [b, b, b, b])],
    [("7' 0' 7' 5'", [b, b, b, b])],
    [("2' 4'", [2*b, 2*b])],
    [("0'", [4*b])],
]



jens_solo_arps = [
    [("0' 4' 7' 11' R", [tt, t, tt, t + b, b])],
    [("R 7' 4' 7' 7'", [tt, t, tt, t + b, b])],
    [("9' 6' R", [b + tt, t + b, b])],
    [("6' 2' 9' 6' 0'' 9' R", [tt, t, tt, t, tt, t, b])],
    [("5' 2' 9' 0'' 5'", [tt, t, tt, t + b, b])],
    [("2' 7 11 2' 5' 2' R", [tt, t, tt, t, tt, t, b])],
    [("4' 4' 4' 0'", [b, tt, t + b, b])],
    [("11 7 11 2' 5' 2' R", [tt, t, tt, t, tt, t, b])],
    [("4' 0' R 4' R 4' R 4'", [tt, t, tt, t, tt, t, tt, t])],
    [("7' 4' 7' 7' R 11'", [tt, t, tt, t, 1 + tt, t])],
    [("0'' 0'' 9' R 9' 6'", [b, tt, t, tt, t, b])],
    [("R 2' 2' 2' R", [b, b, tt, t, b])],
    [("0'' 0'' 9' R 9' 5'", [b, tt, t, tt, t, b])],
    [("R 2' 11 5' 2' 11 7", [b, tt, t, tt, t, tt, t])],
    [("4' 0' R 4' 0' R", [tt, t, tt, t, b, b])],
    [("7' 4' 7' 10' R", [tt, t, tt, t + b, b])],
    [("R 9 0' 9 0' 9", [b, b, tt, t, tt, t])],
    [("5 9 0' 4' R", [tt, t, tt, t + b, b])],
    [("R 0' 4' 0' R", [b, b, tt, t, b])],
    [("9 0' 5 R", [b, tt, t + b, b])],
    [("2' R 0'' 6' 9' 6'", [b, b, tt, t, tt, t])],
    [("0'' 0'' 9' R", [b, tt, t + b, b])],
    [("9' R 9' 2' 5' 2'", [b, b, tt, t, tt, t])],
    [("11 11 2' R", [b, tt, t + b, b])],
    [("4' 0' 7' 0' R 4' 7' 11'", [tt, t, tt, t, tt, t, tt, t + b])],
    [("7' 11' R", [tt, t + b, b])],
    [("6' 2' 9' 2' R 9'", [tt, t, tt, t, b, b])],
    [("0'' 6' R 9' R", [tt, t, tt, t + b, b])],
    [("9' 2' R 5' 2'", [tt, t, tt, t + b, b])],
    [("5' 11 R 2' 5'", [tt, t, tt, t + b, b])],
    [("4' 0' 7' 4' 7' 11'", [tt, t, tt, t, tt, t + b])],
    [("R", [4 * b])],
]
