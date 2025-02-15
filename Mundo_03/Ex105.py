def notas(*n, sit=False):
    """
    -> FUNÇÃO PARA ANALISAR NOTAS E SITUAÇÕES DE VÁRIOS ALUNOS.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com vária informaçãoes sobre a situação da turma.
    """
    r = dict ()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n) / len(n)
    if sit: 
        if r['Média'] >= 7:
            r['Situação'] = 'BOA'
        elif r['Média'] >= 5:
            r['Situação'] = 'RAZOÁVEL'
        else:
            r['Situação'] = 'RUIM'

    return r

# PROGRAMA PRINCIPAL
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)