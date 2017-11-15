import couchdb;
import sys;

if len(sys.argv) != 2:
    print ("Utilize o seguinte formato: <Nome do Programa> <Número de Documentos>");
else:
    server = couchdb.Server();
    db = server.create('teste');
    #print (db);
    db = server['teste'];
    #print (db.name);
    count = 1;
    for i in range(int(sys.argv[1])):
        db.create(); #save document in database
        print((float(count)/float(sys.argv[1])) * 100, "% ");
        count = count + 1;
    #del server['teste'];