for k in range(2):
    for i in range(2, 11):
        for j in range(k * 4 + 2, k * 4 + 6):
            print(f'{j:^3}*{i:^3}= {j * i:<3}\t', end='')
        print()
    print()