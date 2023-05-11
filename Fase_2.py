from getpass import getpass
from mysql.connector import connect, Error

fim_do_programa=False
def executarComando(query):
    try:
        with connect(
            host="us-cdbr-east-06.cleardb.net",
            user="be7a3aeaebea72",
            password="ae18ab90",
            database="heroku_4bf3deb1366252e"
        ) as connection:
            create_db_query = "select * from amostras"
            with connection.cursor(create_db_query) as cursor:
                cursor.execute(query)
                connection.commit()
                cursor.execute(create_db_query)
                result = cursor.fetchall()
                print(result)
    except Error as e:
        print(e)

def verificarClassificacao(MP10, MP25, O3, CO, NO2, SO2):
    if 50>=MP10>=0 and 25>=MP25>=0 and 100>=O3>=0 and 9>=CO>=0 and 200>=NO2>=0 and 20>=SO2>=0:
        definirClassificacao("boa")
    elif 250>=MP10>150 or 125>=MP25>75 or 200>=O3>160 or 15>=CO>13 or 1130>=NO2>320 or 800>=SO2>365:
        definirClassificacao("muito ruim")
    elif 150>=MP10>100 or 75>=MP25>50 or 160>=O3>130 or 13>=CO>11 or 320>=NO2>240 or 365>=SO2>40:
        definirClassificacao("ruim")
    elif 100>=MP10>50 or 50>=MP25>25 or 130>=O3>100 or 11>=CO>9 or 240>=NO2>200 or 40>=SO2>20:
        definirClassificacao("moderada")
    else:
        definirClassificacao("pessima")

def definirClassificacao(statusClassificacao):
    if statusClassificacao == "boa":
        print("As condições desse ar está boa, assim não causa efeitos para a saúde.")
    elif statusClassificacao == "muito ruim":
        print("A condição desse ar está muito ruim, assim causando esses efeitos para a saúde:")
        print("Toda a população pode apresentar agravamentos dos sintomas como tosse seca,cansaço, ardor nos olhos, nariz e garganta e ainda falta de ar e respiração ofegante. Efeitos ainda mais graves à saúde de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas")
    elif statusClassificacao == "ruim":
        print("A condição desse ar está ruim, assim causando esses efeitos para a saúde: \n")
        print("Toda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta. Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar efeitos mais sérios na saúde.")
    elif statusClassificacao == "moderada":
        print("A condição desse ar está moderada, assim causando esses efeitos para a saúde: \n")
        print("Pessoas de grupo sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar sintomas como tosse seca e cansaço. A população, em geral, não é afetada.")
    elif statusClassificacao == "pessima":
        print("A condição desse ar está péssima, assim causando esses efeitos para a saúde:")
        print("Toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. Aumento de mortes prematuras em pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias ou cardíacas).")

print("Programa Para Calcular A Qualidade Do Ar!")
print("O programa analisará o número dos poluentes abaixo e irá classificar o ar entre bom, moderado, ruim, muito ruim e péssimo")
print("1)Partículas inaláveis (MP10)") 
print("2)Partículas inaláveis finas (MP2,5)")
print("3)Ozônio (O3)")
print("4)Onóxido de carbono (CO)")
print("5)Dióxido de nitrogênio (NO2)")
print("6)Dióxido de enxofre (SO2)")
fim_do_programa=False
while not fim_do_programa:
    correcoes=True
    while correcoes:
        while True:
            try:
                MP10=float(input("Digite o valor: 1) Partículas inaláveis: "))
            except:
                print("Só numeros por favor!")
                print("Tente novamente!")
            else:
                break
        while True:
            try:
                MP25=float(input("Digite o valor: 2) Partículas inaláveis finas: "))
            except:
                print("Só numeros por favor!")
                print("Tente novamente!")
            else:
                break
        while True:
            try:
                O3=float(input("Digite o valor: 3) Ozônio: "))
            except:
                print("Só numeros por favor!")
                print("Tente novamente!")
            else:
                break
        while True:
            try:
                CO=float(input("Digite o valor: 4) Onóxido de carbono: "))
            except:
                print("Só numeros por favor!")
                print("Tente novamente!")
            else:
                break
        while True:
            try:
                NO2=float(input("Digite o valor: 5) Dióxido de nitrogênio: "))
            except:
                print("Só numeros por favor!")
                print("Tente novamente!")
            else:
                break
        while True:
            try:
                SO2=float(input("Digite o valor: 6) Dióxido de enxofre: "))
            except:
                print("Só numeros por favor!")
                print("Tente novamente!")
            else:
                break
        resp=input("Você gostaria de mudar algum valor? (S/N): ")
        while True:
            if resp not in ["s","S","n","N"]:
                print("A resposta tem que ser S ou N!") 
                print("Tente novamente!")
            else:
                break
        if resp in ["n","N"]:
            correcoes=False
        else:
            while True:
                print("Qual resposta você gostaria de arrumar?")
                print("1) Partículas inaláveis (MP10)") 
                print("2) Partículas inaláveis finas (MP2,5)")
                print("3) Ozônio (O3)") 
                print("4) Onóxido de carbono (CO)") 
                print("5) Dióxido de nitrogênio (NO2)") 
                print("6) Dióxido de enxofre (SO2)") 
                while True:
                    try:   
                        resp2=int(input("Digite a opção: ")) 
                    except:
                        print("Só numeros por favor!")
                        print("Tente novamente!")
                    else:
                        break      
                if resp2==1:
                    while True:
                        try:
                            MP10=float(input("Digite o valor: 1)Partículas inaláveis: "))
                        except:
                            print("Só numeros por favor!")
                            print("Tente novamente!")
                        else:
                            correcoes=False
                            break
                elif resp2==2:
                    while True:
                        try:
                            MP25=float(input("Digite o valor: 2)Partículas inaláveis finas: "))
                        except:
                            print("Só numeros por favor!")
                            print("Tente novamente!")
                        else:
                            correcoes=False
                            break
                elif resp2==3:
                    while True:
                        try:
                            FMC=float(input("Digite o valor: 3) Ozônio: "))
                        except:
                            print("Só numeros por favor!")
                            print("Tente novamente!")
                        else:
                            correcoes=False
                            break
                elif resp2==4:
                    while True:
                        try:
                            O3=float(input("Digite o valor: 4) Onóxido de carbono: "))
                        except:
                            print("Só numeros por favor!")
                            print("Tente novamente!")
                        else:
                            correcoes=False
                            break
                elif resp2==5:
                    while True:
                        try:
                            CO=float(input("Digite o valor: 5) Dióxido de nitrogênio: "))
                        except:
                            print("Só números por favor!")
                            print("Tente novamente!")
                        else:
                            correcoes=False
                            break
                elif resp2==6:
                    while True:
                        try:
                            NO2=float(input("Digite o valor: 6) Dióxido de enxofre: "))
                        except:
                            print("Só numeros por favor!")
                            print("Tente novamente!")
                        else:
                            correcoes=False
                            break
                else:
                    print("Não existe uma alternativa com esse número!")
                    correcoes=False
                resp3=input("Você gostaria de corrigir mais algum valor? (S/N): ")
                while True:
                    if resp3 not in ["s","S","n","N"]:
                        print("A resposta tem que ser S ou N!") 
                        print("Tente novamente!")
                    else:
                        break
                if resp3 in ["n","N"]:
                    break
        
        verificarClassificacao(MP10, MP25, O3, CO, NO2, SO2)
        comando = f"insert into Amostras values ({MP10}, {MP25},  {O3}, {CO}, {NO2}, {SO2});"
        executarComando(comando)

        resp4=input("Deseja incluir novas amostras? Responda com S ou N: ")
        while True:
            if resp4 not in ["s","S","n","N"]:
                print("A resposta tem que ser S ou N!") 
                print("Tente novamente!")
            else:
                break
        if resp4 in ["n","N"]:
            fim_do_programa=True
print("Obrigada por usar esse programa!")