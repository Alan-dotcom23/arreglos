
playlistDelCurso = [
    "Beat-it.mp3",
    "Loba.mp3",
    "15B.mp3",
    "Diva-virtual.mp3",

]
print(playlistDelCurso[3])

print("---------- IMPRIMIR EL TAMAÑO DEL ARREGLO ----------")
listsize = len(playlistDelCurso)
print(listsize)

print("---------- IMPRIMIR EL ULTIMO ELEMENTO DE LA PLAYLIST ----------")
print(playlistDelCurso[listsize-1])

print("---------- IMPRIMIR TODAS LAS LETRAS DE UNA PALABRA ----------")
palabra = "ANA"
for i in range(len(palabra)):

    print(palabra[i])

print("---------- IMPRIMIR SI ES PALINDROMO O NO ----------")

print("Es palindromo?")
palabraReversa = palabra[::-1]
if palabra == palabraReversa:
    print("Es palindromo 👍")
else:
    print("No es palindromo 👎")

print(palabra)

palabraReversa = palabraReversa[::-1]

print(palabraReversa)
