# linguagem_favorita_api
⚙ workshop fabrica de software 2023.2

## Como executar:

1. clonar repositorio:
> via ssh
```bash
git clone git@github.com:pdr-tuche/linguagem_favorita_api.git
```

> via https
```bash
git clone https://github.com/pdr-tuche/linguagem_favorita_api.git
```

2. criar e ativar ambiente virtual:
> ambiente linux
```bash
python3 -m venv venv
source venv/bin/activate
```
> ambiente windows
```ps1
python -m venv venv
.\venv\Scripts\activate.ps1
```

3. fazer download das dependencias do projeto:
```bash
pip install -r requirements.txt
```

4. caso queira um banco de dados vazio, execute:
```bash
python manage.py makemigrations
python manage.py migrate
```
- para usar um banco de dados populado:
```bash
python create_db_from_backup.py
```

5. rodar o servidor:
```bash
python manage.py runserver
```

## Rotas:

**api/**
- *GET*: todos os dados da classe Pessoa
- *POST*: criacao de uma nova instancia de Pessoa:
    > body requisicao:
    ```json
    {
    "nome": "",
    "idade": null,
    "tempo_experiencia": "",
    "linguagem_favorita": ""
    }
    ```

**api/{id}/**
- *PUT*: atualizar dados de uma instancia de Pessoa a partir do id
    > body requisicao:
    ```json
    {
    "nome": "Pedro",
    "idade": 25,
    "tempo_experiencia": "4 anos",
    "linguagem_favorita": "Java"
    }
    ```
- *DELETE*: excluir instancia de Pessoa a partir do id