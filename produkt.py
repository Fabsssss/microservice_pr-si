from pyArango.connection import Connection
import json

# Verbindung zur ArangoDB-Datenbank herstellen
conn = Connection(username="root", password="root")
db = conn["Dokumentenorientiert"]

# Eine Sammlung auswählen oder erstellen
collection_name = "Produkt"
# Pfad zur JSON-Datei mit den Produktinformationen
json_file_path = "./produkt.json"

# Name der Zielsammlung in ArangoDB


# JSON-Daten aus der Datei lesen
with open(json_file_path, "r") as file:
    json_data = json.load(file)

# Sammlung erstellen, falls sie nicht existiert
if not db.hasCollection(collection_name):
    collection = db.createCollection(name=collection_name)
else:
    collection = db[collection_name]

# JSON-Daten in die Sammlung importieren
for product in json_data:
    doc = collection.createDocument()
    doc.set(product)
    doc.save()

print("Datenimport abgeschlossen.")