import sys
from pymongo import MongoClient
if(len(sys.argv)<2):
    print('Indique qual dos selects devem ser operados')
    exit(0);
client=MongoClient()
db = client.banco
alunos = db.alunos #Coleção de alunos
op=int(sys.argv[1])
if(op==1):
    res=alunos.find({"CR":{"$gt":0.9}})
    print(res.count())
if(op==2):
    res=alunos.find({"RA":{"$regex":"^1"},"projeto":{"$exists":True},"projeto.salario":{"$gt":500}})
    print(res.count())
if(op==3):
    res=alunos.find({"dependencias":{"$exists":True},"RA":{"$regex":"^0"},"nome":{"$regex":"^a"},"projeto":{"$exists":False},"$or":[{"CR":{"$gt":0.3,"$lt":0.9}},{"semestre":1},{"dependencias":{'$size':5}}],"dependencias":"Banco de Dados 1"})
    print(res.count())
for i in res:
    print(i)
