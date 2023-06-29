# Proyecto Life

![Logo de Life](https://i.pinimg.com/564x/7d/52/dd/7d52dd5601335f8e59b573116a295009.jpg)

Este es el archivo README para el proyecto Life, desarrollado por el equipo E.A.B.M.O.D.E.L de UTN San Rafael. Esta aplicación tiene como objetivo proporcionar un sistema de inicio de sesión de usuario, almacenar datos de usuario, calcular el IMC (Índice de Masa Corporal), el peso ideal y las calorías quemadas diariamente según el nivel de actividad física del usuario. También genera gráficos informativos y guarda los datos del usuario en una base de datos PostgreSQL.

## Instalación

### Configuración de la base de datos

1. Instala Docker en tu sistema. Puedes descargar Docker Desktop desde [este enlace](https://www.docker.com/products/docker-desktop/).

2. Navega hasta el directorio del proyecto.
``` 
cd ProyectoLife
```
3. Inicia la base de datos PostgreSQL utilizando el archivo Docker Compose YAML proporcionado:
```
docker-compose up -d
```


### Configuración de la aplicación

1. Crea un entorno virtual de Python:
```
python -m venv env
```
2. Activa el entorno virtual:
- En Linux o macOS:
  ```
  source env/bin/activate
  ```
- En Windows:
  ```
  .\env\Scripts\activate
  ```
3. Instala las dependencias especificadas en el archivo (Recuerda estar en la ruta raiz ProyectoLife)`requirements.txt`:
```
pip install -r requirements.txt
```
5. Ejecuta el siguiente comando para cargar los datos iniciales en la base de datos:
```
python scripts/cargar_db.py
```
6. Ejecuta la aplicación Flask:
```
flask run
```

## Uso

1. Abre tu navegador web y accede a la aplicación.
2. Registra una cuenta e inicia sesión con tus credenciales.
3. Utiliza la aplicación para calcular tu IMC, peso ideal y calorías quemadas diariamente según tu nivel de actividad física.
4. La aplicación generará gráficos informativos para visualizar tus datos.
5. Todos los datos se almacenarán localmente en tu computadora.

## Créditos

Desarrollado por el equipo E.A.B.M.O.D.E.L de la UTN San Rafael.

## Licencia

Este proyecto está bajo la [Licencia MIT](LICENSE).
