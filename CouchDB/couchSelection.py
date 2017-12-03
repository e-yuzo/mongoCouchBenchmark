import couchdb;
import sys;
import time;
server = couchdb.Server();
db = server['test'];
if len(sys.argv) != 2:
    print ("Utilize o seguinte formato: <Nome do Programa> <Tipo do Select{1 ... 3}>");
else:
    start=time.perf_counter()
    if (int(sys.argv[1])) == 1:
        map_fun_A = '''function(doc) {
            if(doc.CR > 0.9)
                emit(doc._id, doc);
        }
        ''';
        results = db.query(map_fun_A);
        print(len(results));
    if (int(sys.argv[1])) == 2:
        map_fun_B = '''function(doc) {
            if((doc.projeto.salario > 500) && (doc.RA[0] == 1))
                emit(doc._id, doc);
        }
        ''';
        results = db.query(map_fun_B);
        print(len(results));
    if (int(sys.argv[1])) == 3:
        map_fun_C = '''function(doc) {
            if((doc.dependencias)
                && (doc.RA[0] == 0)
                && (doc.nome[0] == 'a')
                && (!doc.projeto)
                && (doc.semestre == 1 || doc.dependencias.length == 5 || (doc.CR > 0.3 && doc.CR < 0.9))) {
                    var found = false;
                    for(var i = 0; i < doc.dependencias.length; i++) {
                        if(doc.dependencias[i] == 'Banco de Dados 1') {
                            found = true;
                        }
                    }
                    if(found == true) {
                        emit(doc._id, doc);
                    }
                }
        }
        ''';
        results = db.query(map_fun_C);
        print(len(results));
    stop=time.perf_counter()
    print(stop-start)
