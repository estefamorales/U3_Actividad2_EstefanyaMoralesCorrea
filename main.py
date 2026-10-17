import os
from dotenv import load_dotenv
from faker import Faker
from sqlalchemy import create_engine, String, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

# Cargar la configuración de conexión desde el archivo .env
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError(
        "No se encontró DATABASE_URL. Crea el archivo .env y configura MySQL."
    )

fake = Faker("es_CO")


class Base(DeclarativeBase):
    """Clase base para los modelos de SQLAlchemy."""
    pass


class Persona(Base):
    """Modelo que representa la tabla personas en MySQL."""
    __tablename__ = "personas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(80), nullable=False)
    apellido: Mapped[str] = mapped_column(String(80), nullable=False)
    correo: Mapped[str] = mapped_column(String(150), nullable=False, unique=True)
    ciudad: Mapped[str] = mapped_column(String(100), nullable=False)


def main():
    engine = create_engine(DATABASE_URL, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    total_registros = 100_000
    tamano_lote = 5_000

    with Session() as session:
        # Se limpia la tabla para que la ejecución deje exactamente 100.000 filas.
        session.query(Persona).delete()
        session.commit()

        for inicio in range(0, total_registros, tamano_lote):
            limite = min(inicio + tamano_lote, total_registros)
            lote_personas = []

            for numero in range(inicio, limite):
                lote_personas.append(
                    Persona(
                        nombre=fake.first_name(),
                        apellido=fake.last_name(),
                        correo=f"persona{numero + 1}@ejemplo.com",
                        ciudad=fake.city(),
                    )
                )

            session.add_all(lote_personas)
            session.commit()
            print(f"Registros insertados: {limite}/{total_registros}")

    with engine.connect() as conexion:
        cantidad = conexion.exec_driver_sql(
            "SELECT COUNT(*) FROM personas"
        ).scalar_one()

    print(f"Total de registros en la tabla personas: {cantidad}")


if __name__ == "__main__":
    main()
