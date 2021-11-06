import json
from csv import DictReader

with open("/home/ed/Desktop/users.json", "r") as users_file:
    users = json.loads(users_file.read())

lst_result = []
for user in users:
    d = dict()
    d["name"] = user["name"]
    d["gender"] = user["gender"]
    d["address"] = user["address"]
    d["age"] = user["age"]
    d["books"] = []
    lst_result.append(d)


def books_generator(books_path):
    with open(books_path, newline='') as books_file:
        reader = DictReader(books_file)
        for row in reader:
            yield row


bk = books_generator("/home/ed/Desktop/books-39204-271043.csv")

try:
    while True:
        for i in lst_result:
            next_book = next(bk)
            i["books"].append(next_book)
except StopIteration:
    pass

with open("/home/ed/Desktop/result.json", "w") as result_file:
    create_json = json.dumps(lst_result, indent=4)
    result_file.write(create_json)
