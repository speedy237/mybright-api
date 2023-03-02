#from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
Base = declarative_base()
# Define the User table
class User(Base):
    __tablename__ = 'user'
    idU = Column(Integer, primary_key=True)
    nom = Column(String(50), nullable=False)
    prenom = Column(String(50), nullable=False)
    grade = Column(String(50), nullable=False)
    laboratoire = Column(String(50), nullable=False)
    login = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    exams = relationship("Exam", back_populates="user")

# Define the Patient table
class Patient(Base):
    __tablename__ = 'patient'
    idP = Column(Integer, primary_key=True)
    nom = Column(String(50), nullable=False)
    prenom = Column(String(50), nullable=False)
    sexe = Column(String(10), nullable=False)
    age = Column(Integer, nullable=False)
    exams = relationship("Exam", back_populates="patient")

# Define the Exam table
class Exam(Base):
    __tablename__ = 'exam'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=datetime.utcnow)
    idP = Column(Integer, ForeignKey('patient.idP'))
    idU = Column(Integer, ForeignKey('user.idU'))
    images = Column(String(200), nullable=False)
    result = Column(String(200), nullable=False)
    patient = relationship("Patient", back_populates="exams")
    user = relationship("User", back_populates="exams")