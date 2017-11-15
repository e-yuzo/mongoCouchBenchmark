import couchdb;
import sys;

server = couchdb.Server();
db = server['teste'];
if len(sys.argv) != 2:
    print ("Utilize o seguinte formato: <Nome do Programa> <ID da Query{1 ... 2}>");
else:
    
    #doc['key'] = 'value';

    for document in db.view('_all_docs'):
        document['Key'] = "replacement value";
        db.save(document);
        #db[document.id] = doc;
