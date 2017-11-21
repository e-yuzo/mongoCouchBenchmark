import couchdb;
import sys;

server = couchdb.Server();
db = server['teste'];
if len(sys.argv) != 2:
    print ("Utilize o seguinte formato: <Nome do Programa> <Tipo do Select{1 ... 3}>");
else:
    if (int(sys.argv[1])) == 1:
        map_fun_A = '''function(doc) {
            if(doc.CR && doc.CR > 0.9)
                emit(doc._id, doc);
        }
        ''';
        results = db.query(map_fun_A);
        for doc in results:
            print(doc.key);
            pass;

    if (int(sys.argv[1])) == 2:
        map_fun_B = '''function(doc) {
            if((doc.projeto.salario > 400) && (doc.RA % 2 == 1))
                emit(doc._id, doc);
        }
        ''';
        #results = db.query(map_fun);
        #print(len(results));
        for doc in db.query(map_fun_B):
            print(doc.key);
            pass;
    #print len(results);