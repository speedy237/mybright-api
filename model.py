from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from base import User,Patient,Exam
from datetime import datetime

class UserCreate(BaseModel):
    
    nom: str
    prenom: str
    grade: str
    laboratoire: str
    login: str
    password: str

# Define the PatientCreate model for patient input
class PatientCreate(BaseModel):
    nom: str
    prenom: str
    sexe: str
    age:  int

# Define the ExamCreate model for exam input
class ExamCreate(BaseModel):
    date: datetime
    idP: int
    idU: int
    images:  str
    result: str
class Credentials(BaseModel):
    login: str
    password: str
