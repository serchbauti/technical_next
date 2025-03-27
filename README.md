# Technical Test extract number

## Descripción
Este proyecto es una API desarrollada con FastAPI que permite extraer números dentro de un rango específico (1-100). El proyecto cuenta con una parte grafica y tambien cuenta con una api con la cual puedes interactuar, cabe mencionar que de igual manera el proyecto se encuentra desplegado en RENDER puede consultar la siguiente url para poder interactuar https://technical-next.onrender.com online NOTA(la primera vez en abrir el link puede llegar a tardar maximo 1 minuto en cargar la pagina).

## 🚀 Instalación
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

Accede a la aplicación en tu navegador en `http://localhost:8000` para interactuar con la interfaz de usuario o utiliza herramientas como Postman para probar los endpoints de la API los cuales puedes explorar en la ruta `http://localhost:8000/docs`.

## Licencia
Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo LICENSE.

## Contacto
Para preguntas o soporte adicional, por favor contacta a [perez.sergiob@gmail.com].
