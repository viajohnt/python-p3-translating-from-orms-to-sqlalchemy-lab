#!/usr/bin/env python3

from sqlalchemy import (PrimaryKeyConstraint, Column, String, Integer)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Dog(Base):
    __tablename__ = 'dogs'
<<<<<<< HEAD:lib/models.py
<<<<<<< HEAD
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer())
    name = Column(String())
    breed = Column(String())
=======
    __table_args__ = (PrimaryKeyConstraint('dog_id'),)

    dog_id = Column(Integer())
    dog_name = Column(String())
    dog_breed = Column(String())
>>>>>>> bbae1be (re-re-add solution)
=======
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer())
    name = Column(String())
    breed = Column(String())
>>>>>>> b1d5e75 (rename columns):app/models.py
