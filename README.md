# Proyecto de Extracción de Números

## Descripción
Este proyecto es una API desarrollada con FastAPI que permite extraer números dentro de un rango específico (1-100). El proyecto cuenta con una parte grafica y tambien cuenta con una api con la cual puedes interactuar.

## Instalación
Sigue estos pasos para instalar y ejecutar el proyecto en tu entorno local:

```bash
# Clonar el repositorio
git clone https://github.com/usuario/extract_number_technical_test.git

# Navegar al directorio del proyecto
cd extract_number_technical_test

# Crear un entorno virtual
python -m venv venv

# Activar el entorno virtual
# En Windows
venv\Scripts\activate
# En macOS/Linux
source venv/bin/activate

# Instalar las dependencias
pip install -r requirements.txt
```

## Uso
Para ejecutar el proyecto, utiliza el siguiente comando:

```bash
# Iniciar el servidor FastAPI
uvicorn app.main:app --reload
```

Accede a la aplicación en tu navegador en `http://localhost:8000` para interactuar con la interfaz de usuario o utiliza herramientas como Postman para probar los endpoints de la API.

## Licencia
Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo LICENSE.

## Contacto
Para preguntas o soporte adicional, por favor contacta a [perez.sergiob@gmail.com].