from typing import List

from book import Book
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, registry, relationship

table_registry = registry()


@table_registry.mapped_as_dataclass
class Romanticist:
    __tablename__ = 'romanticists'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    nome: Mapped[str] = mapped_column(String, nullable=False, unique=True)

    livros: Mapped[List['Book']] = relationship(
        'Book', back_populates='romanticista'
    )

    def __repr__(self) -> str:
        return f"<Romanticist(id={self.id}, nome='{self.nome}')>"
