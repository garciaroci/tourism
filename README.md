# Conociendo Argentina

1. Crear Entorno local de desarrollo para Python (Solo lo ejecutamos al principio)

_Linux/Mac_

```
python3 -m venv venv
```

_Windows_

```
python -m venv venv
```
Cada vez que comenzamos a trabajar en la terminal ejecutamos los siguientes comandos

2. Activar entorno de desarrollo

_Linux/Mac_

```
. venv/bin/activate
```

_Windows_

```
venv\Scripts\Activate.ps1
```

> Si el anterior comando dio algún problema iniciar una consola de PowerShell en modo administrador y ejecutar el siguiente comando `Set-ExecutionPolicy Unrestricted -Force`

3. Cada Vez que agregamos una nueva dependencia o al abrir el proyecto por primera vez, ejecutamos este comando:

```
pip install -r requirements.txt
```

4. Cargar base de datos:

```
python init_database.py
```

5. Ejecutar servidor:

```
flask run --host=0.0.0.0
```
