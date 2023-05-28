from pyArango.connection import Connection

# Verbinden mit der ArangoDB-Datenbank
conn = Connection(username='root', password='root')
db = conn["SchluesselWert"]

# Erstellen einer neuen Sammlung für die Schlüssel-Wert-Datenbank
collection_name = 'kunde'
if not db.hasCollection(collection_name):
    collection = db.createCollection(name=collection_name)
else:
    collection = db[collection_name]

# Hinzufügen von Schlüssel-Wert-Paaren als Dokumente in die Sammlung
doc1 = collection.createDocument()
doc1["key1"] = "Max Mustermann,30"
doc1.save()

doc2 = collection.createDocument()
doc2["key2"] = "Anna Schmidt,25"
doc2.save()

doc3 = collection.createDocument()
doc3["key3"] = "Michael Meier,40"
doc3.save()
