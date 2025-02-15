# EXERCICIO 83

expr = str(input('Digite a expressão: '))
pi = expr.count('(')
pf = expr.count(')')
if expr.index(')') > expr.index('('):
    if pi == pf:
        print('Expressão válida')
    else:
        print('Expressão é inválida')
else:
    print('Expressão inválida')

expr = str(input('Digite a expressão: '))
lista = []
for simb in expr:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão está válida! ')
else:
    print('Sua expressão está inválida!')