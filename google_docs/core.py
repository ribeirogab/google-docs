from api import main
import json


def start():
    with open("./google_docs/content/content.json", "r") as file:
        content = json.load(file)
    service = main()
    return [service, content]


def create_documment():
    [service, content] = start()
    doc = service.documents().create(body=content).execute()
    print("Created document with title: {0}".format(doc.get("title")))


def get_documment():
    [service] = start()
    doc = (
        service.documents()
        .get(documentId="1tW0rAhVFhuR5S07vcxcJhXocVu8LZmg2pAUd8JEJhV4")
        .execute()
    )

    print("The title of the document is: {}".format(doc.get("title")))

