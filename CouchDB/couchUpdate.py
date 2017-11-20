import couchdb;
import sys;

server = couchdb.Server();
db = server['teste'];
if len(sys.argv) != 2:
    print ("Utilize o seguinte formato: <Nome do Programa> <ID da Query{1 ... 2}>");
else:
    if(sys.argv[1] == 1):
        map_fun = '''function(doc) {
            if(doc.semestre == 2) {
                emit(doc.name, null);
        }}
        ''';
        results = db.query(map_fun);
        #fazer o acrescimo no cr + 0.01
        for doc in results:
            acresc = 0.01 + doc["cr"];
            update['cr'] = acresc;
            doc = update;
            db.save(doc);
    if(sys.argv[1] == 2):
        map_fun = '''function(doc) {
            if(doc.cr > 0.8 && doc.salario < 600 && "especie" in doc)
                emit(doc.name, null);
        }
        ''';
        results = db.query(map_fun);
        update['salario'] = 600;#salario = 600
        for doc in results:
            doc = update;
            db.save(doc);
