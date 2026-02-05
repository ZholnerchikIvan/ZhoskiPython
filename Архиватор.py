s = str() 
K = str()
cs = str() # текущий символ
p = 0 # индекс числа в конечном списке

s = str(input())

lists = list(s)
clists = [None] * len(lists)

print(clists)

for i in range(len(lists) - 1):
    cs = lists[i]

    print(f'Весь список {lists}, текущий символ {cs} (ТЕСТИРОВАНИЕ) i = {i}, len(lists) = {len(lists)}')

    if cs == lists[i + 1]:
        if clists[p] is None:
            clists[p] = 1
        else:
            clists[p] = int(clists[p]) + 1
            if i < len(lists) - 2:
                if lists[i + 2] != cs:
                    p += 1
    else:
        clists[p] = lists[i]
        p += 1


print(clists)