
## Readme

Sistema de gestión escolar.

Prueba de conocimiento de un sistema orientado a la Gestión Escolar,  contiene módulos para salones, materias, registro de estudiantes, estado de asistencia de los estudiantes y administración de las tablas de salones y materias.  

## Instalación del programa.

1. Asegúrate de tener [Python 3.12.1](https://www.python.org/downloads/) instalado.

2. Descargar el proyecto del repositorio: https://github.com/alejandro2232/PruebaTecnicaWeb2py

o clonarlo.

`git clone https://github.com/alejandro2232/PruebaTecnicaWeb2py`

Ubicarse en la raíz del proyecto.

3. Descargar e instalar Node (https://nodejs.org/en).

## Configuración de la Base de Datos

1. Descarga e instala pgAdmin

2. Crea una base de datos en PostgreSQL para el proyecto.

3. Configura la base de datos con el nombre base de datos=postgres, usuario=director, contraseña=1234, Hostname/address=localhost y puerto=5432

## Ajustes

1. En la raíz del proyecto ejecute este comando:

`pip install -r requirements.txt`

3. En la raíz del proyecto ejecute este comando:

`tsc --project applications/sistemaGestionEscolar/static`

En caso de que salga un error de que no reconoce tsc ejecutar el comando 

`npm install -g typescript`

4. En la raíz del proyecto ejecute este comando:

`alembic upgrade head`

## Ejecutar

1. En la raíz del proyecto ejecuté este comando: python web2py.py -a 1234 -i 0.0.0.0 -p 8000 (de esta forma la contraseña del administrador queda predefinida como 1234, puede cambiarla si es necesario) o python web2py.py (en caso de que lo haga de esta forma tendrá que digitar manualmente la contraseña de administrador que será usado más adelante)

2. Diríjase al link http://127.0.0.1:8000/ y dé clic en el botón 'Mis sitios' ubicado en la barra de navegación.

3. Digite la contraseña del administrador (en este caso, 1234).

4. De la aplicación sistemaGestionEscolar seleccioné el menú desplegable Gestionar y después editar. Cuando lo haga, podrá visualizar la estructura del programa.

## Carpetas de interes 

En la aplicación sistemaGestionEscolar, se destacan las siguientes carpetas y archivos:

De la carpeta controllers:

estudiante_controlador.py, materias_controlador.py y salones_controlador.py,

De la carpeta models: 

estudiantes.py, materias.py y salones.py, 

De la carpeta modules: 

render.py, repository.py, carpeta factory y carpeta modelos

De la carpeta views:

Carpeta estudiante_controlador, materias_controlador y salones_controlador

De la carpeta static: 

Carpeta ts

## Estructura de directorio

    project/
        README
        LICENSE
        VERSION                    > esta versión web2py
        web2py.py                  > el script de inicio
        anyserver.py               > trabajar con servidores de terceros
        ...                        > otros controladores y archivos de ejemplo
        gluon/                     > las bibliotecas centrales
            packages/              > submódulos web2py
              dal/
            contrib/               > bibliotecas de terceros
            tests/                 > unittests
        applications/              > las aplicaciones
            admin/                 > IDE basado en web
                ...
            examples/              > ejemplos, documentos, enlaces
                ...
            welcome/               
                ABOUT
                LICENSE
                models/
                views/
                controllers/
                sessions/
                errors/
                cache/
                static/
                uploads/
                modules/
                cron/
                tests/
            ...                    > tus propias aplicaciones
        examples/                  > archivos de configuración de ejemplo, mv .. y personalizar
        extras/                    > otros archivos necesarios para construir web2py
        scripts/                   > utilidad y scripts de instalación
        handlers/
            wsgihandler.py         > Manejador para conectarse a WSGI
            ...                    > Manejadores para Fast-CGI, SCGI, Gevent, etc.
        site-packages/             > módulos opcionales adicionales
        logs/                      > los archivos de registro irán aqui
        deposit/                   > un lugar donde web2py almacena aplicaciones temporalmente


