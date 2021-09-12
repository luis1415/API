# API

- Para correr la API se necesita docker-compose 3.3 o mayor:

```
docker-compose up
```

- también se puede correr con docker:

```
sh docker_build_and_run.sh
```

- Para correr los unittest:

```
python -m unittest discover
```

- Para la API sin usar docker:

```
pip install -r requirements.txt
```

```
uvicorn property_app:app
```
