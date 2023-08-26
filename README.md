# POKE-APP
This APP has all logic to consume async PokeAPI

## Installation

To install this project run:

```bash
  docker compose up --build poke-app
```

In your browser put this URL:

```txt
  http://localhost:8000/pokemon/<ID>
```

you can change the param url for other number that you want **ID**
## Testing

The next step, open the shell from Docker Container **poke-app**

```bash
λ docker ps -a

CONTAINER ID   IMAGE          COMMAND                  CREATED              STATUS              PORTS                    NAMES       
0713bfcb3a67   poke-app   "python run.py"          17 seconds ago       Up 14 seconds       0.0.0.0:8000->8000/tcp   poke-app

```

With the **Container ID** of **poke-app** image run

```bash
  docker exec -it <CONTAINER ID> bash
```

Into the Container bash run:

```bash
  root@<CONTAINER ID>:/app# pytest tests/test_routes.py
```

With this you can test the logic async about **poke-app**

## Screenshots

![image](https://github.com/sdparada97/Pokedex-App/assets/49702755/74dea807-db29-43d8-8e3c-8a4a56775ce4)