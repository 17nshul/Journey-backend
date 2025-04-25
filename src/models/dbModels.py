# app/models.py
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    email = Column(String(128), primary_key=True)
    password = Column(String(128))  # Increased length for hashed passwords
    name = Column(String(32), nullable=False)  # Changed from full_name
    created_at = Column(DateTime, default=datetime.now())

class JournalEntry(Base):
    __tablename__ = "journal_entry"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_email = Column(String(128), ForeignKey("user.email"), nullable=False)
    entry_text = Column(Text, nullable=False)
    mood = Column(String(32))
    created_at = Column(DateTime, default=datetime.now())