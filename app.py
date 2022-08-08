from pyexpat import model
from peewee import *
import datetime

db = PostgresqlDatabase('contact_book', user='ohnosir', password='123',
                        host='localhost', port=5432)

db.connect()


class BaseModel(Model):
    class Meta:
        database = db


class Person(BaseModel):
    first_name = CharField()
    last_name = CharField()


db.create_tables([Person])

eric = Person(first_name="Eric", last_name="Guzman")


paul = Person(first_name="Paul", last_name="Kim")


mitch = Person(first_name="Mitch", last_name="Raznick")


mickey = Person(first_name="Mickey", last_name="Mouse")


find_eric = Person.get((Person.first_name == "Eric"))
find_every_eric = Person.select().where(Person.first_name == "Eric")
print(find_eric)
print(find_every_eric)
eric.last_name = "Namzug"
eric.save()
print(eric.last_name)

eric.delete_instance()
