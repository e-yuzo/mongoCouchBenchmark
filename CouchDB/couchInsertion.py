import couchdb;
import sys;
from randomDocs import geradorAluno;
import time
#import arquivo gerador

if len(sys.argv) != 2:
    print ("Utilize o seguinte formato: <Nome do Programa> <Número de Documentos>");
else:
    server = couchdb.Server();
    db = server.create('teste');
    #print (db);
    db = server['teste'];
    #print (db.name);
    #count = 1;
    doc=[];
    for i in range(int(sys.argv[1])):
        doc.append(geradorAluno()); #save document in database
    start=time.perf_counter()
    db.update(doc);
    stop=time.perf_counter()
        #print(count, " ");
        #count = count + 1;
    #del server['teste'];
    print(stop-start)
