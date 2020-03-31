
def delete(lista):
    for i in range(len(lista)):
        lista[i].pop(0)
        for j in range(len(lista[i])):
            lista[i][j] = lista[i][j].replace("\n", "")
def compare_genom(genom1, genom2):
    list = []
    list.append(open(genom1).readlines())
    list.append(open(genom2).readlines())
    delete(list)
    t1 = ""
    for i in list[0]:
        t1 += i
    t2 = ""
    for i in list[1]:
        t2 += i
    if len(t1) < len(t2):
        M = t2
        m = t1
    else:
        M = t1
        m = t2
    porc = 0
    for i in range(len(M)):
        if i <= len(m)-1:
            if t1[i] == t2[i]:
                porc += 1
    porc = (porc / len(M)) * 100
    return porc
def imprime(a, b):
    return round(compare_genom(a, b), 1)

h1 = 'Porcentaje de concidencia- genomas'
print(h1.center(40, " "))
print()

txt1 = 'AY274119.txt'
txt2 = 'AY278488.2.txt'
txt3 = 'MN908947.txt'
txt4 = 'MN988668.txt'
txt5 = 'MN988669.txt'

print('{:^7}{:^7}{:^7}{:^7}{:^7}{:^7}'.format('        ', 'AY274119', 'AY278488.2', 'MN908947', 'MN988668', 'MN988669'))
for i in range(5):
    if i == 0:
        print('{:^7}{:^7}{:^7}{:^7}{:^7}{:^7}'.format('AY274119', imprime(txt1, txt1), imprime(txt1, txt2), imprime(txt1, txt3), imprime(txt1, txt4), imprime(txt1, txt5)))
    elif i == 1:
        print('{:^7}{:^7}{:^7}{:^7}{:^7}{:^7}'.format('AY278488.2', imprime(txt2, txt1), imprime(txt2, txt2), imprime(txt2, txt3), imprime(txt2, txt4), imprime(txt2, txt5)))
    elif i == 2:
        print('{:^7}{:^7}{:^7}{:^7}{:^7}{:^7}'.format('MN908947', imprime(txt3, txt1), imprime(txt3, txt2), imprime(txt3, txt3), imprime(txt3, txt4), imprime(txt3, txt5)))
    elif i == 3:
        print('{:^7}{:^7}{:^7}{:^7}{:^7}{:^7}'.format('MN988668', imprime(txt4, txt1), imprime(txt4, txt5), imprime(txt4, txt3), imprime(txt4, txt4), imprime(txt4, txt5)))
    elif i == 4:
        print('{:^7}{:^7}{:^7}{:^7}{:^7}{:^7}'.format('MN988669', imprime(txt5, txt1), imprime(txt5, txt3), imprime(txt5, txt3), imprime(txt5, txt4), imprime(txt5, txt5)))
