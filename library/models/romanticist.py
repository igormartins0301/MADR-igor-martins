from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Romanticist(Base):
    __tablename__ = 'romanticists'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)

    books = relationship('Book', back_populates='romanticista')

    def __repr__(self):
        return f"<Romanticist(id={self.id}, nome='{self.nome}')>"
