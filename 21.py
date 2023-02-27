K = 4
N = 2 ** K
seq = [bin(j)[2:] for j in range(N) if not "111" in bin(j)[2:]]

print(len(seq))


N = int(input())
LIST = [0] * (N + 4)
LIST[1] = 2
LIST[2] = 4
LIST[3] = 7
for i in range(4, N+1):
    LIST[i] = (LIST[i-1] + LIST[i-2] + LIST[i-3]) % 12345

print(LIST[N])