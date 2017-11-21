import couchdb;
import sys;

server = couchdb.Server();
db = server['teste'];
if len(sys.argv) != 2:
    print ("Utilize o seguinte formato: <Nome do Programa> <ID da Query{1 ... 2}>");
else:
    if(sys.argv[1] == 1):
        map_fun = '''function(doc){
            if (doc.dependencias && doc.dependencias.length > 10 && doc.semestre >= 6){
                emit(doc._id, doc)
            }}''';
    if(sys.argv[1] == 2):
        map_fun = '''function(doc){
            if (doc.projeto && doc.CR < 0.6){
                emit(doc._id, doc)
            }}''';
    deldoclist = [];
    for row in db.query(map_fun):
        deldoclist.append(row.key);
    for item in deldoclist:
        del db[item];