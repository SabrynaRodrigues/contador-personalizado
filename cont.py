# Contador Personalizado - Desafio 98 do Mundo 3/Curso Python

def contador(i,f,p):
    print(f'A contagem de {i} a {f} de {p} em {p} é igual a:')
    c = i
    if i < f:
        while c <= f:
            print(f'{c}', end=' ')
            c += p
        print('FIM')
    else:
        while c >= f:
            print(f'{c}', end=' ')
            c -= p
        print('FIM')

# Programa Principal
contador(1,10,1)
contador(10,0,2)
d = int(input('Início:'))
f = int(input('Fim:'))
g = int(input('Passo:'))
contador(d,f,g)