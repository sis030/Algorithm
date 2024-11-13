T = int(input())
datelist = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

for i in range(1, T + 1):
    YMD = input()
    Y = YMD[0:4]
    M = YMD[4:6]
    D = YMD[6:8]

    if 0 < int(M) < 13 and 0 < int(D) <= datelist[int(M)]:
        print(f'#{i} {Y}/{M}/{D}')
    else:
        print(f'#{i} -1')