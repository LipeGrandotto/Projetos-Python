# EXERCICIO 89

listam = []
listaf = []
medialista = []
while True:
    listaf.append(str(input('Nome: ')))
    listaf.append(float(input('Nota 1: ')))
    listaf.append(float(input('Nota 2: ')))
    resp = str(input('Quer continuar? [S/N]'))
    listam.append(listaf[:])
    listaf.clear()
    if resp in 'Nn':
        break
print('-=' * 40)
print(f'{"Num.":<8}{"NOME":15}{"MÉDIA":>8}')
print('-' * 38)
for i, l in enumerate(listam):
    media = (listam[i][1] + listam [i][2]) / 2
    medialista.append(media)
    print(f'{i:<8}{listam[i][0]:<15}{medialista[i]:>8.1f}')
print('-' * 38)
while True:
    resp = int(input('Mostrar notas de qual aluno?  (999 interrompe):  '))
    if resp == 999:
        print('PROGRAMA ENCERRADO...  \nVOLTE SEMPRE!')
        break
    if resp <= len(listam) - 1:
        print(f'Aluno: {listam[resp][0]}  \nNOTA 1: {listam[resp][1]}  \nNOTA 2: {listam[resp][2]} ')