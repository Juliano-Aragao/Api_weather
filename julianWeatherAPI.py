import streamlit as st
import requests
from chave import api_key_1

css_path = "style.css"    
with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
   
# Função para consultar a API do OpenWeather
def consultar_clima(cidade):
    api_key = api_key_1  # chave de API da OpenWeather
    url = f'http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric'
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except requests.exceptions.RequestException as e:
        st.error(f"Erro na requisição: {e}")
        return None
 
 

# Título da página e descrição
st.title('Consulta de Clima')
st.write('Insira o nome da cidade para consultar o clima.')

# Campo para o usuário inserir a cidade
cidade = st.text_input('Digite o nome da cidade')

# Botão para enviar a requisição
if st.button('Consultar Clima'):
    if cidade:
        dados_clima = consultar_clima(cidade)
        if dados_clima:
            # Exibir os dados meteorológicos obtidos
            st.write(f'Dados meteorológicos de {cidade}:')
            st.write(f'Temperatura: {dados_clima["main"]["temp"]} °C')
            st.write(f'Umidade: {dados_clima["main"]["humidity"]} %')
            #st.write(f'Tempo: {dados_clima["weather"][0]["description"]}')
            descricao_tempo = dados_clima["weather"][0]["description"]

            # Aplicando a lógica de transformação da descrição do tempo
            if descricao_tempo == "overcast clouds":
                tempo_1 = "Tempo Nublado"
            elif descricao_tempo == "few clouds":
                tempo_1 = "Poucas Nuvens"
            else:
                tempo_1 = "Céu Aberto"

            # Escrevendo no Streamlit com a nova variável tempo_1
            st.write(f'Tempo: {tempo_1}')
            
            # Botão de reset após exibir os dados
            st.button("Reset")
            
        else:
            st.write(f'Erro ao obter dados meteorológicos para {cidade}.')
    else:
        st.write('Por favor, insira o nome da cidade.')
        
       
