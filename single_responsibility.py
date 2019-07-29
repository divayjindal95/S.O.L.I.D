"""
One and only one reason to change. Similar properties and functionalities should be put together.
If class handles more than one responsilbilty, change in one responsibility effects the other one
Thi will have domino effect which is more time consuming and painfull.
"""


class User:

    def __init__(self, u_id, url):
        self.id = u_id
        self.url = url

    def get_details(self, db):
        return db.connect(self.url).fetch(self.id)

    def put_details(self, db):
        db.connect(self.url).save(self.id)


class User:

    def __init__(self, id):
        self.id = id

    def get_details(self, db_connection):
        db_connection.fetch_details(self.id)

    def put_details(self, db_connection):
        db_connection.save_details(self.id)


class Db:
    def __init__(self, url):
        self.connection = db.connect(self.url)

    def fetch_details(self, id):
        self.connection.fetch(id)

    def save_details(self, id):
        self.connection.save(id)
