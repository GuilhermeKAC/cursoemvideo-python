frase = 'Curso em Vídeo Python'
frase2 = '   Aprenda Python  '

print(frase[::2])
print(frase[13:])
print(frase[3])
print(frase[1:15:2])
print(frase[9::3])
print(len(frase)) #conta o número de char na string
print(frase.count('o')) #conta o número de char definido na string
print(frase.count('o',0,13)) #contar o char entre o valor 0 ao 13
print(frase.find('deo')) #quantas vezes encontra a sequencia
print(frase.find('Android')) #ele retorna -1 se não encontrar
print('Curso' in frase) # procura se é verdadeiro
print(frase.replace('Python', 'Android')) #subistitui python por android
print(frase.upper()) #transforma tudo em maiusculo
print(frase.lower()) #transforma em minusculo
print(frase.capitalize()) #Tudo vira minusculo mas a primeira se torna maiusculo
print(frase.title()) #Analisa quantas frases tem observando os espaços. Transformando todas em maiusculo
print(frase2)
print(frase2.strip()) #remove os espaços no inicio e fim
print(frase2.rstrip()) #colocando o R remove apenas a direita
print(frase2.lstrip()) #remove os espaços apenas a esquerda
print(frase2.split()) #divisão dentro da string considerando os espaços
print(frase.split()) #transformando em uma lista
print('-'.join(frase2)) #junta todos os elementos de frase separando com -
print('-'.join(frase))
print(frase.upper().count('O'))
print(len(frase2.strip()))
print(frase.lower().find('vídeo'))
print(frase.split())
dividido = frase.split()
print(dividido[2][3])
frase = frase.replace('Python', 'Android')
print(frase)
