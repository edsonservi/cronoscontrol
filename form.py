# Importar as bibliotecas
import streamlit as st
import csv
from datetime import datetime

st.title("REGISTRO - Inspeções Predial")

local = [" - ", "Torre 1", "Torre 2", "Entrada Pedestre Torre 1", "Entrada Pedestre Torre 2", "Entrada de Veículos", "Estacionamento", "Garagem", "Piscina", "Quiosque"]
areas = [" - ", "1º Andar", "2º Andar", "3º Andar", "4º Andar", "5º Andar", "6º Andar", "7º Andar", "8º Andar", "9º Andar", "Barrilete","Caixa de Água", "Bicicletário", "Casa de Bombas", "Casa de Máquinas", "Cisterna", "Depósito", "Poço", "Sala de Jogos", "Sala de Reunião", "Sala do Sindico", "Soprador", "Subsolo", "Térreo", "Zeladoria"]
subareas = [" - ", "Antecâmnara", "Banheiro", "Escada", "Hall", "Rampa"]
pontos = ["Iluminação", "Luz de Emergência", "Sinalização", "Extintor", "Hidrante", "Sensor de Presença", "Limpeza", "Manutenção"]
status = ["NA", "OK", "Necessita Atenção", "Crítico"]

with st.expander("🔍 Inspeção Predial", expanded=False):
    with st.form("form_inspecao", clear_on_submit=True):
        user = st.text_input("Usuário")
        local = st.selectbox("Local", local)
        area = st.selectbox("Area", areas)
        subarea = st.selectbox("Sub-Area", subareas)
        
        status_pontos = {}  # Dicionário para armazenar os status
        for ponto in pontos:
            selection = st.segmented_control(ponto, options=status, default="OK", selection_mode="single", key=ponto)
            status_pontos[ponto] = selection  # Armazena o status selecionado para cada ponto

        descricao = st.text_area("Descrição")
                
        submitted = st.form_submit_button("Registrar Inspeção")
        if submitted:
            agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # Salvar os dados em um arquivo CSV
            if user.strip() == "zelador":
                with open('inspecoes_predial.csv', mode='a', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    row = [agora, local, area, subarea] + [f'{situacao}' for ponto, situacao in status_pontos.items()] + [descricao.replace('\n', '=nl=').replace(',', "=virgula=")]
                    writer.writerow(row)
                    st.success("Inspeção gravada com sucesso!")
            st.success("Inspeção registrada com sucesso!")
            st.write(f"**Local: ** {local}")
            st.write(f"**Area: ** {area}")
            st.write(f"**Subarea: ** {subarea}")
            st.write(f"**Descrição: ** {descricao}")
            
            st.write("### Situação dos Pontos Avaliados:")
            for ponto, situacao in status_pontos.items():
                st.write(f"**{ponto}**: {situacao}")


        