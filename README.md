# TuPrimeraPagina-TuRoldan
Este es un proyecto web Django que simula un blog, creado como parte de un ejercicio de aprendizaje.

## Requisitos

* Python 3.x
* Django 4.x

## Instalación

1.  Clona el repositorio:

    ```bash
    git clone (https://github.com/AgustinRoldan27/TuPrimeraPagina-TuRoldan.git)
    ```

2.  Navega al directorio del proyecto:

    ```bash
    cd mi_blog
    ```

3.  Crea un entorno virtual (opcional pero recomendado):

    ```bash
    python -m venv venv
    ```

4.  Activa el entorno virtual:

    * En Windows:

        ```bash
        venv\Scripts\activate
        ```

    * En macOS y Linux:

        ```bash
        source venv/bin/activate
        ```

5.  Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

    (Si no tienes un archivo `requirements.txt`, puedes instalar Django con `pip install Django`)

6.  Ejecuta las migraciones:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

7.  Ejecuta el servidor de desarrollo:

    ```bash
    python manage.py runserver
    ```

8.  Abre tu navegador web y visita `http://127.0.0.1:8000/`.

## Funcionalidades

* Crear autores, categorías y publicaciones.
* Buscar publicaciones por título.

## Instrucciones

1.  Para crear un autor, ve a `http://127.0.0.1:8000/blog/autor/crear/`.
2.  Para crear una categoría, ve a `http://127.0.0.1:8000/blog/categoria/crear/`.
3.  Para crear una publicación, ve a `http://127.0.0.1:8000/blog/post/crear/`.
4.  Para buscar una publicación, ve a `http://127.0.0.1:8000/blog/post/buscar/`.

## Autor

agustin roldan
