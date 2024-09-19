import os

def existe_arquivo(arq):
    return os.path.exists(arq)
        
def criar_arquivo(arq):
    a = open(arq, 'w')
    a.close()

def gravar_contato(arq, tupla):
    a = open(arq, 'a')
    notas = ""
    for nota in tupla[2]:
        notas += str(nota) + "\t"
    notas = notas.strip()
    a.write(f"{tupla[0]}\t{tupla[1]}\t{notas}\n")
    a.close()

def menu():
    print('1- Cadastrar aluno e notas')
    print('2- Mostrar alunos e notas')
    print('3- Pesquisar aluno')
    print('0- Sair')

def validar_nota(nota):
    if nota < 0 or nota > 10:
        print('Nota inválida!')
        return False
    else:
        return True
    
def cadastrar_aluno():
    lista = []
    tupla = ()
    pront = input('Prontuário: ')
    nome = input('Nome: ')
    for i in range(3):
        while True:
            nota = float(input('Nota: '))
            if validar_nota(nota):
                lista.append(nota)
                break
    tupla = (pront,nome,lista)
    return tupla

def inserir_dicio(dicio,tupla):
    dicio[tupla[0]] = [tupla[1], tupla[2]]
    return dicio

def calcular_media(notas):
    soma = 0
    for nota in notas:
        soma += nota
    media = soma / len(notas)
    return media

def situacao(media):
    if media < 4:
        print('Reprovado')
    elif 4 <= media < 6:
        print('IFA')
    else:
        print('Aprovado')

def mostrar_aluno(dicio):
    for k,v in dicio.items():
        print(f'Prontuário: {k}')
        print(f'Nome: {v[0]}')
        print('Notas:')
        for nota in v[1]:
            print(nota)
        media = calcular_media(v[1])
        print(f'Média: {media}')
        situacao(media)

def pesquisar_aluno(dicio, pront):
    if pront in dicio:
        v = dicio[pront]
        print(f'Prontuário: {pront}')
        print(f'Nome: {v[0]}')
        print('Notas:')
        for nota in v[1]:
            print(nota)
        media = calcular_media(v[1])
        print(f'Média: {media}')
        situacao(media)
    else:
        print('Aluno não cadastrado!')

def carregar_contatos(arq):
    a = open(arq, 'r')
    dicio = {}
    for linha in a:
        infos = linha.strip().split('\t')
        prontuario = infos[0]
        nome = infos[1]
        notas = []
        for nota in infos[2:]:
            notas.append(float(nota))
        dicio[prontuario] = [nome, notas]
    a.close()
    return dicio

def main():
    arq = 'notas_apr1.txt'
    if not existe_arquivo(arq):
        criar_arquivo(arq)

    dicio = carregar_contatos(arq)
    while True:
        menu()
        opc = int(input('Opção: '))
        if opc == 0:
            break
        elif opc == 1:
           tupla = cadastrar_aluno()
           dicio = inserir_dicio(dicio, tupla)
           gravar_contato(arq,tupla)
        elif opc == 2:
            mostrar_aluno(dicio)
        elif opc == 3:
            pront = input('Qual o prontuário do aluno que deseja encontrar?\n')
            pesquisar_aluno(dicio, pront)
        else:
            print('Opção inválida!')
            
main()

