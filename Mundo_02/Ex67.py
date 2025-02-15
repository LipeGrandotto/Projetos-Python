# EXERCICIO 67

while True:
    print('-=' *25)
    v = int(input('Digite um valor: '))
    if v < 0:
        print('-=' *25)
        print('TABUADA ENCERRADA!')
        print('-=' *25)
        break
    for c in range (1,11):
        print("{} x {} = {}".format(v, c, v*c))