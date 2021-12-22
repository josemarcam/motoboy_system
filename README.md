# Motoboy_system

Python 3.8

## Pré-requisitos Ambiente Docker:

Para trabalhar nesse projeto você ira precisar instalar:

*[ Docker ](https://www.docker.com/get-started)			
*[ Docker Compose ](https://docs.docker.com/compose/install/)


## Ambiente de desenvolvimento

Rode o comando de build

    sudo docker-compose build

Para subir o banco de dados execute o comando de up

    sudo docker-compose up

    //Para rodar em background execute:
    sudo docker-compose up -d

Iniando a API:

    //Crie o ambiente virtual python
    python3.8 -m venv venv

    //Acione o ambiente virtual

* Windows
    
    `./venv/Scripts/activate.bat`
* UNIX
    
    `source venv/bin/activate`
    
    
    //Instale as bibliotecas necessarias
    pip install -r requirements.txt

    //Rode as migrations
    python console.py db upgrade heads

    //Iniciar a API
    flask run
    

## Documentação e Requests

Existe uma pasta chamada `request_collection`, dentro dela esta o arquivo necessario para importar a collection de requests da API.

## Simulando o ambiente do teste
    
Para simular o ambiente que foi passado no teste, rode a seguinte linha
    
    python console.py create-zax-environment