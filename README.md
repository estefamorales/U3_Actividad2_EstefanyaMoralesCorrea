# Actividad 2: Python, SQLAlchemy, Faker y MySQL

## Objetivo
Crear una tabla en MySQL y generar 100.000 registros ficticios mediante Python, SQLAlchemy y Faker.

## Requisitos
- Python 3.10 o superior
- Servidor MySQL instalado y en ejecución
- DBeaver para comprobar la cantidad de registros

## Crear la base de datos
Conéctate a MySQL desde DBeaver y ejecuta:
```sql
CREATE DATABASE actividad_python;
```

## Instalar dependencias
Desde la terminal, dentro de esta carpeta:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
En Windows, activar el entorno con:
```powershell
.venv\Scripts\activate
```

## Configurar la conexión
Copia `.env.example` con el nombre `.env` y modifica usuario y contraseña para que correspondan a tu instalación de MySQL. No publiques el archivo `.env`.

## Ejecutar
```bash
python main.py
```
El programa crea la tabla `personas`, inserta 100.000 registros por lotes de 5.000 y muestra el avance. Si lo ejecutas otra vez, elimina las filas que haya en `personas` antes de generar las nuevas.

## Verificar en DBeaver
Ejecuta:
```sql
SELECT COUNT(*) FROM personas;
```
El conteo esperado es `100000`. Guarda una captura real de la consulta y el resultado para la entrega.

## Archivos
- `main.py`: programa principal.
- `requirements.txt`: librerías necesarias.
- `.env.example`: plantilla para configurar la conexión.
- `.gitignore`: evita publicar secretos y archivos temporales.
- `README.md`: guía de uso.

## Publicar en GitHub
Crea un repositorio público, sube los archivos anteriores y no incluyas `.env`. Realiza al menos cinco commits reales durante el desarrollo, por ejemplo: estructura inicial, dependencias, modelo, generación de registros y documentación/verificación.

Proyecto académico de generación de datos ficticios con Python y MySQL.

Instrucciones de configuración y ejecución del proyecto.
