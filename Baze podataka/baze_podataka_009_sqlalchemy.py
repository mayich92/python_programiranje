from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os
os.chdir('Baze podataka')

db_name = 'employees.db'
engine = create_engine('sqlite:///' + db_name, echo=True)
Base = declarative_base()

class Employee(Base):
    __tablename__ = 'Employees'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
e1 = Employee(name='Alice', email='alice@alice.com', phone='123-4567')
e2 = Employee(name='Bob', email='bob@algebra.com', phone='124-4567')
employees_list = [e1, e2]
session.add_all(employees_list)
session.commit()