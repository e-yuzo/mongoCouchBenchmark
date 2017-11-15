import couchdb;
import sys;

server = couchdb.Server();
db = server['teste'];
if len(sys.argv) != 2:
    print ("Utilize o seguinte formato: <Nome do Programa> <ID da Query{1 ... 2}>");
else:
    doc['key'] = 'value';
    for document in db:
        db[document.id] = doc;

map_fun = '''function(doc){
    if (doc.doc_type == 'classic'){
    emit(doc._id, doc)
    }}''';

deldoclist = []
for row in db.query(map_fun):
    deldoclist.append(row.key)

for item in deldoclist:
    del db[item]