N1 = int(input("Ingrese la primera nota: "))
N2 = int(input("Ingrese la segunda nota: "))
N3 = int(input("Ingrese la tercera nota: "))
N4 = int(input("Ingrese la cuarta nota: "))

Media = (N1 + N2+ N3 +N4)/4
print(Media)

if Media > 89:
    print("Puntuacion es A")
elif Media < 89 and Media > 79:
    print("Puntuacion es B")
elif Media < 79 and Media > 69:
    print("Puntuacion es C")
elif Media < 69 and Media > 59:
    print("Puntuacion es D")
else:
    print("Puntuacion es E")