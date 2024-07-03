num = [int(i) for i in input().split()]

def duplicate(num):
    dupl = []
    for k in num:
        if num.count(k) > 1 and k not in dupl:
            dupl.append(k)
    print(dupl.sort())