import couchdb;
import sys;

server = couchdb.Server();
db = server['teste'];
if len(sys.argv) != 2:
    print ("Utilize o seguinte formato: <Nome do Programa> <ID da Query{1 ... 3}>");
else:
    if(sys.argv[1] == 1):
        map_fun_A = '''function(doc) {
            if(doc.type == 'Person')
                emit(doc.name, null);
        }
        ''';
        results = db.query(map_fun_A);
    elif(sys.argv[1] == 2):
        map_fun_B = '''function(doc) {
            if(doc.type == 'Person')
                emit(doc.name, null);
        }
        ''';
        results = db.query(map_fun_B);
    elif(sys.argv[1] == 3):
        map_fun_C = '''function(doc) {
            if(doc.type == 'Person')
                emit(doc.name, null);
        }
        ''';
        results = db.query(map_fun_C);
    print len(results);
    for doc in results:
        pass; #wait
