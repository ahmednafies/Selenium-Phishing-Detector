from pymongo import MongoClient
import json


def to_mongodb(domain):
    db_client = MongoClient()
    db = db_client.phishing
    db.whitelist.insert_one(
        {
            "legitimate": {
                "domain_name": domain
            }
        }
    )

def phsihing_to_db():
    jsonFile = open('links-old.json', 'r')
    data = json.load(jsonFile)
    jsonFile.close()

    link_array = []

    for index in data:
        link_array.append(index['url'])

    print (len(link_array))


    for link in link_array:
        to_mongodb(link)
        print(link)


def legit_to_db():
    text_file = open("file.txt", "r")
    lines = text_file.read().split('\n')

    for line in lines:
        domain = line.replace(" ", "")
        to_mongodb(domain)

legit_to_db()