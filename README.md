# Análise de Corridas Pessoais com Python, SQL e API de Clima

Projeto pessoal onde aplico o que aprendi até o momento no meu curso de Data Science, utilizando os dados das minhas corridas ao longo de 9 meses.

---

## Visão Geral

Em 2024, descobri e iniciei duas novas paixões: corridas e ciência de dados. Nesse ano de 2025, na tentativa de encontrar ideias de projetos que me permitissem aplicar o conhecimento adquirido e gerar portfólio para futuras oportunidades, tive a ideia de unir os dois.

Criei uma tabela com mais de 60 corridas, com o objetivo de tirar algum conhecimento da minha evolução nas corridas. O projeto inclui:

- Uma **API para buscar dados de umidade** (meu app parou de registrar a partir da 20ª corrida);
- Um **script para inserção de dados** das corridas via terminal (VS Code);
- Alguns **gráficos e análises** usando Python e SQL.

---

## Estrutura dos Arquivos

| Arquivo              | Descrição                                               |
|----------------------|---------------------------------------------------------|
| `analises.ipynb`     | Gráficos e análises com Pandas/Matplotlib               |
| `api.py`             | Script que busca a umidade do dia da corrida via API    |
| `app.py`             | Script que insere novos dados no banco via terminal     |
| `sql_scripts.sql`    | Consultas SQL para análise dos dados                    |
| `README.md`          | Este documento                                          |

---

## Tecnologias Utilizadas

- Python (Pandas, Matplotlib)
- MySQL
- VS Code

---

##  Dados Utilizados

- **Total de corridas**: 69
- **Período**: de 30/09/2024 a 19/06/2025
- **Campos**: distância, calorias, data, dia da semana, umidade, ritmo médio (min/km), duração (min), velocidade média (km/h)
- **Fonte dos dados**: App Adidas Running coleta manual

---

## Insights Gerados

###  Análises Gerais:
- A maioria das corridas está entre 5 e 7 km.
- A mediana da distância foi de 5.3 km (usei a mediana pois o boxplot revelou um outlier acima de 10 km).
- Ritmo médio: 5,53 min/km
- Maior velocidade registrada: 13,1 km/h

### Evolução:
-A partir de Maio desse ano tive uma queda no ritmo médio,ou seja fiquei mais rápido e a velocidade média acompanha essa tendência aumentando a partir desse ponto.Sinal de evolução do meu desempenho.

###  Fatores externos:
- A umidade não parece ter influenciado significativamente o desempenho.
  
###  Descanso:
- Com média de 3 dias de descanso entre corridas, consegui manter distâncias maiores com mais facilidade.
- Mais consistência = melhor desempenho.

---

## Possíveis Melhorias Futuras

- Adicionar novas corridas e atualizar os dados antigos
- Criar um dashboard interativo com Streamlit ou Power BI
- Aplicar modelos de IA e ir evoluindo minhas corridas.

---


