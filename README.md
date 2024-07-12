# Api_weather

## Aplicação de Consulta de Clima com Streamlit e Docker
Este repositório contém uma aplicação simples que utiliza Streamlit para consultar dados meteorológicos usando a API do OpenWeather. A aplicação está containerizada usando Docker para facilitar o ambiente de desenvolvimento e execução.

## Pré-requisitos
Se você quer utilizar essa aplicação, antes de começar, certifique-se de ter os seguintes requisitos instalados em seu ambiente de desenvolvimento:

## Docker: Instalação do Docker
Chave de API do OpenWeather: Você precisará de uma chave de API válida do OpenWeather para acessar os dados meteorológicos. Essa chave deve ser configurada em um arquivo chave.py conforme descrito abaixo.
Configuração do Ambiente
Clone o Repositório:


## Clonar o repositorio 
git clone https://github.com/https://github.com/Juliano-Aragao/Api_weather.git
cd Api_weather
Configuração da Chave de API:

Crie um arquivo chave.py no diretório raiz do projeto e defina sua chave de API do OpenWeather nele:

# chave.py
api_key_1 = 'sua_chave_de_api_aqui'
Construção da Imagem Docker:

A imagem Docker para a aplicação ser executada, siga os seguintes comandos no diretório raiz do projeto:

## Para construir o dockerfile
docker build -t meu_app_streamlit .
Isso criará uma imagem Docker chamada meu_app_streamlit com base no Dockerfile fornecido.

## Executando a Aplicação
Depois de construir a imagem Docker, você pode executar um contêiner para iniciar sua aplicação Streamlit:


## Acessando a Aplicação
docker run -p 8501:8501 meu_app_streamlit
Isso iniciará a aplicação Streamlit dentro do contêiner e mapeará a porta 8501 do contêiner para a porta 8501 do seu host local. Você pode acessar a aplicação Streamlit em seu navegador usando o seguinte URL:


## Stylo ( Visual FrontEnd )
Estilo CSS: Se você deseja personalizar o estilo da aplicação Streamlit, modifique o arquivo style.css no diretório raiz do projeto.
Gerenciamento de Dependências: As dependências Python da aplicação são listadas no arquivo requirements.txt. Certifique-se de atualizar este arquivo conforme necessário para adicionar ou remover pacotes.
Repositório: Este repositório pode ser modificado e expandido conforme suas necessidades. Sinta-se à vontade para contribuir com melhorias ou funcionalidades adicionais.

# Aplicação de Consulta de Clima com Streamlit - sem a utilização do docker file
Este repositório contém uma aplicação simples que utiliza Streamlit para consultar dados meteorológicos usando a API do OpenWeather.

Pré-requisitos
bom como sempre, antes de começar, certifique-se de ter os seguintes requisitos instalados em seu ambiente de desenvolvimento:

Python 3.8 ou superior
Streamlit
Chave de API do OpenWeather: Você precisará de uma chave de API válida do OpenWeather para acessar os dados meteorológicos. Esta chave deve ser configurada em um arquivo chave.py conforme descrito abaixo.
Configuração do Ambiente
Clone o Repositório:


git clone https://github.com/seu-usuario/Api_weather.git
cd Api_weather
Configuração da Chave de API:

Crie um arquivo chave.py no diretório raiz do projeto e defina sua chave de API do OpenWeather nele:

# chave.py

api_key_1 = 'sua_chave_de_api_aqui'
Instalação das Dependências:

Instale as dependências Python necessárias usando pip. Recomenda-se usar um ambiente virtual para manter as dependências isoladas do sistema global:

## Craiando o ambiente virtual
python -m venv env
source env/bin/activate   # No Windows use `env\Scripts\activate`
pip install -r requirements.txt
O arquivo requirements.txt contém as dependências Python necessárias para executar a aplicação.

Executando a Aplicação
Depois de configurar o ambiente e instalar as dependências, você pode iniciar a aplicação Streamlit:

streamlit run julianWeatherAPI.py
Isso iniciará a aplicação Streamlit localmente. Você pode acessar a aplicação em seu navegador usando o URL fornecido pelo Streamlit (geralmente http://localhost:8501 por padrão).

## Stylo ( Visual FrontEnd )
Estilo CSS: Se você deseja personalizar o estilo da aplicação Streamlit, modifique o arquivo style.css no diretório raiz do projeto.
Atualizações: Lembre-se de atualizar o arquivo requirements.txt conforme necessário para adicionar ou remover pacotes Python.
Contribuições: Este repositório é aberto para contribuições. Sinta-se à vontade para enviar melhorias ou funcionalidades adicionais.
