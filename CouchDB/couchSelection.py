import couchdb;
import sys;

server = couchdb.Server();
db = server['teste'];
if len(sys.argv) != 2:
    print ("Utilize o seguinte formato: <Nome do Programa> <ID da Query{1 ... 3}>");
else:
    if(sys.argv[1] == 1):
        map_fun_A = '''function(doc) {
            if("cr" in doc && doc.cr > 0.9)
                emit(doc.name, null);
        }
        ''';
        results = db.query(map_fun_A);
    elif(sys.argv[1] == 2):
        map_fun_B = '''function(doc) {
            if("especie" in doc && doc.salario < 400 && (doc.ra % 2) == 1)
                emit(doc.name, null);
        }
        ''';
        results = db.query(map_fun_B);
    print len(results);
    for doc in results:
        pass;
