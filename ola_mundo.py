#-*- utf-8 -*- # Para compilar com caracteres especiais.
import random

print("Hello World")
print("Olá mundo!!")

print(10/3)
print(1%3)

a = 1
b = 5
c = 7

print("\nif")
if c < b:
	print("'c' menor que 'b'")
else:
	print("'c' é maior que 'b'")


print("\nwhile")
x=1
while x < 10:	
	print(x)
	x += 1


print("\nlistas")
lista1= [1,2,3,4,5,6,7,8]
lista2= ["tem", "alguém", "nesse lugar","?", "ou", "não?" ]
lista3= ["0", "fui...", True,  3.556, 27]

for i in lista3:
	print(i)

print("\nUse of range() to access Python list using index number:\n")
sample_list = ["Palavra 1", "20", 30, "Texto", 50]
for i in range(len(sample_list)):
	print("List item at index ", i, "is ", sample_list[i])


print("\n....................\n")
x = {"name" : "John", "age" : 36}

#display x:
print(x)
#display the data type of x:
#print(type(x)) 


for k in range(5, 15, 2):
	print(k)

print("\nStrings...\n")
var1 ="aaXXAhA¨AAtt¨VajLKJl.*/*-k#&*oPOrquwe787lkjhfasASDFAS435234"
var2 = 5.77
var3 = True
var4 = "34232345234234"

var5 = var1 + " " + var4

print(len(var5))

print(var5[2])
print(var5[5:])
print(var5[0:5])


#maiuscula/minuscula
string = "QWEWEQWEW32434"
print (string.lower())

print(string[0:3].upper())

#removendo caracteres

print("Remover espaço - split()")
remover_espaco = " sdgasgd dfsas\naasddas \n"
print(remover_espaco)
print(remover_espaco.strip())

print("Lista - split()")
montar_lista = "O rato roeu a roupa do rei de roma"
print(montar_lista.split('r'))


print("Substring - se nao encontrar retorna -1")

busca = montar_lista.find("rei")

print(montar_lista[busca:]) 
m_string = montar_lista.replace("o rei", "a rainha")
print(m_string)

print("\nFuncoes...........................\n")

def soma(x, y):
	return x+y

def multiplicacao(x,y):
	return x*y 	

s = soma(4,7)
m = multiplicacao(3,6)

print(s, m)

print("\nLEITURA DE ARQUIVO")

arquivo = open("arquivo.txt")

texto_completo = arquivo.read()

print(texto_completo)

print("\nLEITURA DE ARQUIVO por linha")
arquivo = open("arquivo.txt")

linhas = arquivo.readlines()
print (linhas)
for linha in linhas:
	print(linha)


print("\nCriando ARQUIVOS")

w = open("C:\\Users\\acrainieri\\Downloads\\arquivo1.txt", "w") 
w.write("Esse é meu arquivo Python\n yeess")
w.close()

#append no arquivo
w = open("C:\\Users\\acrainieri\\Downloads\\arquivo2.txt", "a") 
w.write("Esse é meu arquivo Python\n")
w.close()


print("\nLISTAS\n")
minha_lista =["abacaxi","melancia", "abacate"]
minha_lista2 = [1,2,3,4,5]
minha_lista3 = ["abacaxi", 2, 9.89, True]

print(minha_lista3[2])

for item in minha_lista2:
	print(item)
for item in minha_lista:
	print(item)

print(minha_lista2[2]) 
print("\n")
print(len(minha_lista2))


minha_lista.append("limao")

for item in minha_lista:
	print(item)

if 3 in minha_lista2:
	print("\n3 está na lista\n")


print("\nRemovendo itens acima de dois\n")
del minha_lista[2:]

for item in minha_lista:
	print(item)	


print("\n\n..... Lista Animais .......\n")
l_animais = ["cavalo", "vaca", "cachorro"]	
print(l_animais)
l_animais.append("gato")


for animal in l_animais:
	if animal == "gato":
		print(animal+"\n..................")

for ix in range(len(l_animais)):
	print(ix)
	if   ix ==    2   :
		print(l_animais[ix])


print("\n........... Leitura de arquivo ..................\n")
arqX = open("C:\\Users\\acrainieri\\Downloads\\arquivo1.txt")	
l_linhas = arqX.readlines()

for linha_ in l_linhas:
	print(linha_)

print("\n......... ordenando listas ............\n")	

l_desordenada = [44,66,77,22,7,45,898,34,2,578,4,55]
print(l_desordenada)

l_desordenada.sort()
print(l_desordenada)

l_desordenada.reverse()
print(l_desordenada)

print("\n............. palavras ordenadas.............")
l_palavras=["2_mosca","0jabuti", "_xibungo","zabumba","boi zebu", "carangueijo", "sagui", "abacaxi", "sabugo"]
l_palavras.sort()
print(l_palavras)
l_palavras.sort(reverse=True)
print(l_palavras)



print("\n\n<< dicionarios em python {'x':'y'} - São pares de chave/valor.................>>\n")
dicionario_sites = {"Diego": "diegomariano.com", "Google": "google.com", "Udemy": "udemy.com"}
 
for chave in dicionario_sites:
    print(dicionario_sites[chave])

print(dicionario_sites["Google"])   


dicionario = {"A":"Ameixa", "B":"Bacalhau", "C":"Jujuba"}
print(dicionario)

for chave in dicionario:
	print(chave)
print("\n.....")

for chave in dicionario:
	print(chave + " - " + dicionario[chave])


print("\n.....Itens")
for i_dic in dicionario.items():
	print(i_dic)

print("\n.....Values")
for i_dic in dicionario.values():
	print(i_dic)	

print("\n.....keys")
for i_dic in dicionario.keys():
	print(i_dic)	

numero = random()