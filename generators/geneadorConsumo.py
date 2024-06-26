import random
def generarDatos():
    datos =[]
    for i in range(5000):
        dato ={}
        id=random.randint(1,10000)
        referencia=random.choice(["ACH01","ACH22","ACH43"])
        marca=random.choice(["sony","rico","kalley"])
        capacidad=random.randint(100,2000)
        ciudad=random.choice(["bello","medelllin","envigado","itagui","sabaneta"])
        responsable=random.choice(["Laura Perez","Yaneth Perez","Tomas Cadavid","Sara Arango","Carolina Cano"])

        dato=[id,referencia,marca, capacidad, ciudad, responsable] 
        datos.append(dato)
    return datos
print(generarDatos())