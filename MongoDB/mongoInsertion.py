import sys
import time
from randomDocs import geradorAluno
from pymongo import MongoClient
if(len(sys.argv)<2):
        print('Indique a quantidade de alunos a serem inseridos')
        exit(0);
client=MongoClient()
db = client.banco
alunos = db.alunos #Coleção de alunos
db.alunos.delete_many({}) #limpa a coleção
n=int(sys.argv[1])
start=time.perf_counter()
for i in range(0,n):
    alunos.insert_one(geradorAluno())
stop=time.perf_counter()
print(stop-start)
