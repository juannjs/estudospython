# O append é para adicionar novos conteúdos em outro espaço da lista 
# O index é para sinalizar em qual posição da variável dentro da lista
# O count serve para saber quantas vezes uma mesma variável aparece dentro da lista
# O remove serve para remover alguma variável de dentro da lista
# O reverse serve para inverter a ordem na qual a lista é apresentada

lista=[1,3,6,"Juan",23,12]
lista2=[1]
lista.append("array")
lista.append(29)
lista.index("Juan")
lista.remove(1)
lista.reverse()

print(lista.count(1))
print(lista.index("Juan"))
print(lista)