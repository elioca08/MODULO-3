import pymongo
from  pymongo import MongoClient

client = MongoClient("mongodb+srv://admin16:animo0845@cluster0.inzdy.mongodb.net/Word?retryWrites=true&w=majority")
db = client["Word"]
colecction = db["Word"]


print("Escoger una opción")
print("A.Agregar nueva palabra")
print("B.Editar palabra")
print("C.ELiminar palabra")
print("D.Buscar significado de palabra")
print("E.Mostrar palabras")

opc = str(input("Elegir "))


if opc == 'A':
  p = input("Escribir la palabra que desea añadir ")
  s = input("Escribir el significado de la palabra ")
  client.set("palabra",p,s)
  print(client.get("palabra"))


if opc == 'B':
  p = input("Escribir la palabra que desea cambiar ")
  w = input("Escribir la nueva palabra palabra ")
  s = input("Escribir el nuevo significado de la palabra ")
  result = colecction.update_one({"palabra" : p},{"$set":{"significado" : s}})
  result = colecction.update_one({"significado" : s}, {"$set":{"palabra" : w}})


if opc == 'C':
  p = input("Escribir la palabra que desea borrar ")
  result = colecction.delete_one({"palabra" : p})
 

if opc == 'D':
  p = input("Escribir la palabra que desea buscar ")
  result = colecction.find({"palabra" : p})
  for x in result: 
   print(x["palabra"],"=",x["significado"])


if opc == 'E':
  result = colecction.find({})
  for x in result:
    print(x["palabra"],"=",x["significado"])



