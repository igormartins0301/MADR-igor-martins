from romanticist import Romanticist
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, registry, relationship

table_registry = registry()


@table_registry.mapped_as_dataclass
class Book:
    __tablename__ = 'books'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    ano: Mapped[str] = mapped_column(String, nullable=False)
    titulo: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    id_romanticista: Mapped[int] = mapped_column(ForeignKey('romanticists.id'))

    romanticista: Mapped['Romanticist'] = relationship(back_populates='books')

    def __repr__(self) -> str:
        return (
            f"<Book(id={self.id}, ano='{self.ano}', "
            f"titulo='{self.titulo}', id_romanticista={self.id_romanticista})>"
        )
