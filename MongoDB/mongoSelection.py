import sys
import time
from pymongo import MongoClient
if(len(sys.argv)<2):
    print('Indique qual dos selects devem ser operados')
    exit(0);
client=MongoClient()
db = client.banco
alunos = db.alunos #Coleção de alunos
op=int(sys.argv[1])
if(op==1):
    start=time.perf_counter()
    res=alunos.find({"CR":{"$gt":0.95}})
    print(res.count())
    stop=time.perf_counter()
if(op==2):
    start=time.perf_counter()
    res=alunos.find({"RA":{"$regex":"^1"},"projeto":{"$exists":True},"projeto.salario":{"$gt":500}})
    print(res.count())
    stop=time.perf_counter()
if(op==3):
    start=time.perf_counter()
    res=alunos.find({"dependencias":{"$exists":True},"RA":{"$regex":"^0"},"nome":{"$regex":"^a"},"projeto":{"$exists":False},"$or":[{"CR":{"$gt":0.3,"$lt":0.9}},{"semestre":1},{"dependencias":{'$size':5}}],"dependencias":"Banco de Dados 1"})
    print(res.count())
    stop=time.perf_counter()
if(op==4):
    start=time.perf_counter()
    res=alunos.find({"$or":[{"dependencias":{"$exists":False},"RA":{"$regex":"^0"},"nome":{"$regex":"^a"},"projeto":{"$exists":True},"CR":{"$gt":0.3,"$lt":0.9},"semestre":{"$gt":3,"$lt":9},"projeto.salario":{"$gt":500,"$lt":1000},"projeto.especie":"monitoria"},{"dependencias":{"$exists":True},"RA":{"$regex":"^0"},"nome":{"$regex":"^a"},"projeto":{"$exists":False},"$or":[{"CR":{"$gt":0.3,"$lt":0.9}},{"semestre":1},{"dependencias":{'$size':5}}],"dependencias":"Banco de Dados 1"}],"CR":{"$lt":0.8},"semestre":{"$gt":1}})
    print(res.count())
    stop=time.perf_counter()
print(stop-start)
