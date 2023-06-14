class Alumno:
    facultad = "FES Aragón"

    def __init__(self, nom, ed, carr):
        self.__nombre = nom
        self.__edad = ed
        self.__carrera = carr
    def set_nombre(self,nom):
        self.__nombre = nom

    def get_nombre(self):
        return self.__nombre

    def set_edad(self,ed):
        if ed >= 8 and ed < 120:
            self.__edad = ed
        else:
            print("esa edad no es corecta")
            self.__edad = ed
    def get_edad(self):
        return self.__edad

    def set_carrera(self, carr):
        self.__carrera = carr

    def get_carrera(self):
        return self.__carrera



    def __str__(self):
        cadena = "--------- \n nombre: " + self.__nombre
        cadena= cadena + "\n edad:" + str(self. __edad)
        cadena = cadena + "\n carrera:" + self.__carrera
        cadena = cadena + "\n --------------"
        return cadena

    def estudiar(self,horas=1):
        print(f"el alumno {self.__nombre} esta estudiando {horas}")


class Perro:
    reino = "Canino"

    def __init__(self, raza, edad, estatura):
        self.__raza = raza
        self.__edad = edad
        self.__estatura = estatura

    #metodo de acceso get
    @property
    def raza(self):
        return self.__raza

    #metodo de acceso set
    @raza.setter
    def raza(self, la_raza):
        self.__raza = la_raza

    @property
    def edad(self):
        return self.__edad


    @edad.setter
    def edad(self, la_edad):
        if la_edad > 0 and la_edad < 20:
            self.__edad = la_edad
        else:
            print("esa edad no es valida")
            self.__edad = 0
    @property
    def estatura(self):
        return self.__estatura



    @estatura.setter
    def estatura(self, la_estatura):
        if la_estatura > 0.1 and la_estatura < 1.1:
            self.__estatura = la_estatura
        else:
            print("no way")
            self.__estatura = 0.1
    def __str__(self):
        return f"""
        __________________________
        | RAZA : {self.__raza}          | 
        | EDAD : {self.__edad}          | 
        | ESTATURA : {self.__estatura}          | 
        ----------------------------
        """




    @staticmethod
    def es_cachorro(edad):
        return edad < 3
    @staticmethod
    def dormir(veces = 5):
        for n in range(veces):
            print(f"dando vuelta{n + 1}")
        print("Zzzzzz")

    @classmethod
    def perro_grande(cls, est):
        if est > 0.79:
            return cls ("",0, est)

