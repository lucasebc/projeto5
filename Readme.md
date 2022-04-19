

## Projeto 5 - Biopark


### Setup de Ambiente DEV

> Requisitos: Python V3


#### Passo 1 - Criando virtual env (raiz do projeto clonado)
```bash
python3 -m venv .venv
```
Ativando o virtual env

```
.venv\Script\activate
```

#### Passo 2 - Instalando Requisitos

```
pip install -r requirements.txt
```

#### Passo 3 - Executando migrations

```
python manage.py migrate --run-syncdb
```

#### Passo 4 - Carregando Fixtures

```
python manage.py loaddata projeto5_website\fixtures\initial_data.json
```

#### Passo 5 - Criando superusuário

```
python manage.py createsuperuser
```


#### Passo 6 - Rodando Server

```
python manage.py runserver
```

Abra seu navegador para [Link](http://localhost:8000/)

# Github actions
- Quando é feita uma alteração através de um merge ou pull request na branch teste, a action django.yml faz o merge para a branch main.
- Quando é feita uma alteração através de um merge ou pull request na branch main, a action django.yml roda o teste do django.
