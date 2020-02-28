
#### install poetry and add packages

- for mac

```bash
brew install poetry
```

#### init poetry

using python `v3.*.*` on venv

install python3 in local PC(for mac)

```bash
brew install python3
```

```bash
poetry init
```

use python ^3.7

then create pyproject.toml.

- add package

```bash
poetry add "package name"
```

#### run container

- run jupyter lab

```bash
docker-compose up -d jupyter
```

then access localhost:8888

- run python script in docker

attach docker container.

```bash
docker-compose run jupyter /bin/bash
```

you can exec `python` command.

- run api

```bash
docker-compose up -d api
```

#### publish as python package

- build pacakge

```bash
poetry build
```

then, create files for distribution in `dist/`

##### testing install and uninstall

- install pacakge to your env

https

```bash
pip3 install --user https://github.com/uni-3/fastapi_mock.git
```

ssh

```bash
pip3 install --user git+ssh://git@github.com:uni-3/fastapi_mock.git

```

then, `Successfully installed`

```sh
pip3 list

...
fastapi-mock 0.1.0          
...

```

- uninstall package

```
pip3 uninstall  fastapi-mock
```

