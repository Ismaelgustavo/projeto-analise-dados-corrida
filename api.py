import requests

datas_faltantes = ['2025-06-05','2025-06-07','2025-06-13','2025-06-15','2025-06-17','2025-06-19','2025-06-08']
umidades=[]

def buscar_umidade(data):# Traz a umidade da data em questão
    url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Caet%C3%A9%20MG/{data}?unitGroup=us&key=WLSDX3BZSEY4E6SLZWTSC44B6&include=days&elements=humidity,tempcontentType=json'
    resposta = requests.get(url)
    dados = resposta.json()

    umidade = dados['days'][0]['humidity']
    return umidade

# itera sobre cada data da lista datas_faltantes
for data in datas_faltantes:
    umidade = buscar_umidade(data)
    umidades.append(umidade) 
   
print(umidades)

