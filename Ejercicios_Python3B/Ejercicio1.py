#PALABRAS PROHIBIDAS:
#Define una lista de 5 palabras aleatorias y una lista de letras prohibidas que contenga tres letras.
#Filtra las palabras en tu lista original crea una nueva lista de palabras filtradas que solo contenga
#aquellas palabras que no tienen ninguna letra prohibida.

al_words = ['casa','perro','comedor','unidades','cancion']
lett1, lett2, lett3 = input("Escribe 3 Letras que quieres Prohibir: \n")
lett_canc = [lett1, lett2, lett3]
fter_words = []
cncel_words = []

for word in al_words:
    if lett1 in word or lett2 in word or lett3 in word:
        cncel_words.append(word)
    else:
        fter_words.append(word)

print(fter_words)
print(cncel_words)

fter_words.clear()
print(fter_words)

for word1 in al_words:
   incluir = True
   for prohibido in lett_canc:
       if prohibido in word1:
          incluir = False
   if incluir:
    fter_words.append(word1)
    

print(fter_words)