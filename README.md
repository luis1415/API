# API

Se usa fastapi y docker.

- Para correr la API con docker-compose:

```
docker-compose up
```

- Para correr la API con con docker:

```
sh docker_build_and_run.sh
```

- Para correr la API sin usar docker:

```
pip install -r requirements.txt
```

```
uvicorn property_app:app
```

- Para correr los unittest:

```
python -m unittest discover
```

- Para ver el swagger e interactuar con la API ir a :

```
http://localhost:8000/docs
```

- Para ver la documentacion legible de la API ir a :

```
http://localhost:8000/redoc
```

# Diagrama Entidad relación

Para los likes se tiene relación muchos a muchos, entonces sale un tabla intermedia, con los likes por propiedad, en la tabla likes se almacena la cantidad de likes de cada propiedad por eso la relacion es uno a uno entre likes y propiedades.

![E-R](https://user-images.githubusercontent.com/16037872/132977078-5d8f1e49-e5bb-4e92-a237-74c955e90517.png)
