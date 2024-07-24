# library/models/book.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    ano = Column(String, nullable=False)
    titulo = Column(String, unique=True, nullable=False)
    id_romanticista = Column(Integer, ForeignKey('romanticists.id'))


    romanticista = relationship("Romanticist", back_populates="books")

    def __repr__(self):
        return f"<Book(id={self.id}, ano={self.ano}, titulo='{self.titulo}', id_romanticista={self.id_romanticista})>"
