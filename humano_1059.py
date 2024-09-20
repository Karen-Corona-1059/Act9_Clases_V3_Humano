print("\nActividad 9 clase humano")
print("Karen Corona Mat: 22308051281059")

#Zona de clases

class Humano1059:
    #Zona de atributos dentro de la clase
    edad=0
    genero=""
    colorp=""
    estatura=0
    peso=0
    coloro=""

    #Zona de funciones dentro de la clase

    def correr1059(self,n):
        print(f"{n} esta corriendo...")

    def caminar1059(self,n):
        print(f"{n} esta caminando en el parque..")

    def comer1059(self,n,c):
        print(f"{n} esta comiendo {c}")

    def nadar1059(self,n,c):
        print(f"{n} esta nadando en {c}")

    def hablando1059(self,n,c):
        print(f"{n} esta hablando con {c}")


#Zona de creacion de objetos
Jose=Humano1059()
Keila=Humano1059()


#Zona de usando objetos
print("\n-------------Resultado para Jose:----------------")

print("\nAtributos:")
Jose.edad=18
Jose.genero="Hombre"
Jose.estatura=1.80
Jose.coloro="Verdes"
Jose.colorp="Cafe"
Jose.peso=70

print(f"Edad: {Jose.edad}")
print(f"Genero: {Jose.genero}")
print(f"Estatura: {Jose.estatura}")
print(f"Color de ojos: {Jose.coloro}")
print(f"Color de cabello: {Jose.colorp}")
print(f"Peso: {Jose.peso} kg")

print("\nFunciones:")
Jose.correr1059("Jose")
Jose.caminar1059("Jose")
Jose.comer1059("Jose","Sopa")
Jose.nadar1059("Jose","el mar")
Jose.hablando1059("Jose","Lidia")

print("\n-------------Resultados para Agripina-------------")

print("\nAtributos:")
Keila.edad=17
Keila.genero="Mujer"
Keila.estatura=1.65
Keila.coloro="Cafe"
Keila.colorp="Negro"

print(f"Edad: {Keila.edad}")
print(f"Genero: {Keila.genero}")
print(f"Estatura: {Keila.estatura}")
print(f"Color de ojos: {Keila.coloro}")
print(f"Color de cabello: {Keila.colorp}")

print("\nFunciones:")
Keila.correr1059("Keila")
Keila.caminar1059("Keila")
Keila.comer1059("Keila","Sushi")
Keila.hablando1059("Keila","Arturo")
print("\n")