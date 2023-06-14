from cosas import Alumno, Perro


def main():
    al1 = Alumno("jose", 19, "ICO")
    print(vars(al1))
    al1.__nombre = "diego"
    print(vars(al1))
    al1.set_nombre("maria")
    print(vars(al1))
    print("------To string ------")
    print(al1)
    al1.set_edad(999)
    print(al1)
    al1.estudiar(4)

    print("------- PERRO --------")
    perro1 = Perro("poddle", 2, 0.35)
    perro1(vars(perro1))
    perro1.raza = "de la calle"  # set en notacion pythonic
    print(vars(perro1))
    perro1.__raza = "otra"
    print(vars(perro1))
    perro1.edad = 12
    perro1.estatura = 0.43
    print(perro1)
    cachorro = Perro.es_cachorro(perro1.edad)
    print(cachorro)
    Perro.dormir()
    danes = Perro.perro_grande(0.8)
    print(danes)


main()
