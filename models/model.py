import os
import datetime
from pony.orm import *

db = Database()

class User(db.Entity):
    name = Required(str)
    passwd = Required(str)

class Role(db.Entity):
    name = Required(str)

class Product(db.Entity):
    name = Required(str)
    common_name = Optional(str)
    price = Required(float)
    requirement = Required(str)
    certification = Required(str)
    category = Optional('Category')
    producer = Required('Producer')
    supplier = Required('Supplier')
    entry_record = Set('EntryRecord')

class Producer(db.Entity):
    name = Required(str)
    addr = Required(str)
    telephoe = Required(str)
    products = Set(Product)

class Supplier(db.Entity):
    name = Required(str)
    addr = Required(str)
    telephoe = Required(str)
    product = Set(Product)

class Category(db.Entity):
    name = Required(str)
    products = Set(Product)

class EntryRecord(db.Entity):
    quantity = Required(float)
    date = Required(datetime.datetime)
    term_validity = Required(datetime.datetime)
    product = Required(Product)

set_sql_debug(True)
filename = os.path.join(os.path.abspath(os.curdir),'my.db')
db.bind(provider='sqlite', filename=filename, create_db=True)
db.generate_mapping(create_tables=True)