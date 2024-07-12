# Api_weather
/API_WEATHER
├── julianWeatherAPI.py         
├── requirements.txt  

## Aplicação de Consulta de Clima com Streamlit e Docker
Este repositório contém uma aplicação simples que utiliza Streamlit para consultar dados meteorológicos usando a API do OpenWeather. A aplicação está containerizada usando Docker para facilitar o ambiente de desenvolvimento e execução.

## Pré-requisitos
Antes de começar, certifique-se de ter os seguintes requisitos instalados em seu ambiente de desenvolvimento:

## Docker: Instalação do Docker
Chave de API do OpenWeather: Você precisará de uma chave de API válida do OpenWeather para acessar os dados meteorológicos. Essa chave deve ser configurada em um arquivo chave.py conforme descrito abaixo.
Configuração do Ambiente
Clone o Repositório:

bash
Copiar código
git clone https://github.com/https://github.com/Juliano-Aragao/Api_weather.git
cd Api_weather
Configuração da Chave de API:

Crie um arquivo chave.py no diretório raiz do projeto e defina sua chave de API do OpenWeather nele:

python
Copiar código
# chave.py

api_key_1 = 'sua_chave_de_api_aqui'
Construção da Imagem Docker:

Construa a imagem Docker para sua aplicação executando o seguinte comando no diretório raiz do projeto:

bash
Copiar código
docker build -t meu_app_streamlit .
Isso criará uma imagem Docker chamada meu_app_streamlit com base no Dockerfile fornecido.

## Executando a Aplicação
Depois de construir a imagem Docker, você pode executar um contêiner para iniciar sua aplicação Streamlit:

bash
## Copiar código
docker run -p 8501:8501 meu_app_streamlit
Isso iniciará a aplicação Streamlit dentro do contêiner e mapeará a porta 8501 do contêiner para a porta 8501 do seu host local. Você pode acessar a aplicação Streamlit em seu navegador usando o seguinte URL:

arduino
Copiar código
http://localhost:8501
Notas Adicionais
Estilo CSS: Se você deseja personalizar o estilo da aplicação Streamlit, modifique o arquivo style.css no diretório raiz do projeto.
Gerenciamento de Dependências: As dependências Python da aplicação são listadas no arquivo requirements.txt. Certifique-se de atualizar este arquivo conforme necessário para adicionar ou remover pacotes.
Repositório: Este repositório pode ser modificado e expandido conforme suas necessidades. Sinta-se à vontade para contribuir com melhorias ou funcionalidades adicionais.
