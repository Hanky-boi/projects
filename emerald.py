def E(N,L):
    W = 0
    M = 0
    list = L.split()
    for i in range(N):
        if int(list[i]) % 2 == 0:
            W = W + int(list[i])
        elif int(list[i]) % 2 == 1:
            if W > M:
                M = W
            W = 0
    print(M)
E(13,"2 3 4 4 5 6 1 2 2 2 1 8 2")                                                           