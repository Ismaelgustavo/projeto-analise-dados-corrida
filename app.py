import mysql.connector
# conexão com o banco de dados
conn = mysql.connector.connect(
       host = 'localhost',
       user ='root',
       password = 'casa123456',
       database = 'minhas_corridas'
)
cursor = conn.cursor()



def inserçao(): # inserção dos dados da corrida
        print("\n--- Registro de Corrida ---")
        distancia = input('Distância: ').strip()
        duraçao = input('Duração: ').strip()
        calorias = input('Calorias: ').strip()
        dia_semana = input('Dia da semana: ').strip()
        ritmo_medio = input('Ritmo médio: ').strip()
        velocidade = input('Velocidade média: ').strip()
        umidade = input('Umidade do ar: ').strip()
        data = input('Data: ').strip()

        comando = "INSERT INTO corridas (distancia, duraçao, calorias, dia_semana, ritmo_medio, velocidade_media, umidade, data_corrida) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        valores = (distancia,duraçao,calorias,dia_semana,ritmo_medio,velocidade,umidade,data)

        try:
               cursor.execute(comando,valores)
               conn.commit()
               print("\n Corrida registrada com sucesso!")
        except Exception as e:
                print("\n Erro ao registrar corrida:", e)       
        


while True: # Menu de opções
        
        print("\n--- Selecionar opção ---")
        print("\n--- 1 > Registrar Corrida  ---")
        print("\n--- 2 > Encerrar registro  ---")
        opçao = input ('Insira opção: ')
        
        if opçao == '1':
               inserçao()
        elif opçao == '2':
                print('Operação encerrada')
                cursor.close()
                conn.close()
                break   
        else:
            print('opção inválida')   