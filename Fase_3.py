from getpass import getpass
from mysql.connector import connect, Error

#função para conectar as informações no banco de dados
def executarComando(query):
    try:
        with connect(
            host="us-cdbr-east-06.cleardb.net", #host do bd
            user="be7a3aeaebea72",              #user do bd
            password="ae18ab90",                #senha do bd
            database="heroku_4bf3deb1366252e"   #database  do bd
        ) as connection:
            with connection.cursor(buffered=True) as cursor:        
                cursor.execute(query)
                connection.commit()
                result = cursor.fetchall() #retorna os resultados do bd
                return result
    except Error as e:
        print(e)

#função para retornar a seguinte amostra pelo id
def retornaAmostraPeloId(id):
    comando = f"select * from amostras where id = {id};"
    amostra = executarComando(comando)
    return amostra
    
#função feita para selecionar a opção decidida pelo usuário
def selecionarOpcao():
    print("1 - Cadastro de Amostras")
    print("2 - Alteração de Amostras")
    print("3 - Exclusão de Amostras")
    print("4 - Classificação de Amostras")
    print("5 - Sair")
    opcao = int(input("Digite a opção desejada: "))
    try:
        if opcao == 1:
            cadastroAmostras()      #se selecionar o 1 retornará o cadastroAmostras
        elif opcao == 2:
            alteracaoAmostras()     #se selecionar o 2 retornará o alteracaoAmostras
        elif opcao == 3:
            exclusaoAmostras()      #se selecionar o 3 retornará o exclusaoAmostras
        elif opcao == 4:
            classificarAmostras()   #se selecionar o 4 retornará o classificarAmostras
        elif opcao == 5:            
            quit()                  #se selecionar o 5 sairá do programa
        else:
            print("Não existe a opção digitada")
    except:
        ValueError

#função dedicada para guardar cada amostra que for inserida
def cadastroAmostras():
    print("Digite o valor das amostras para cadastro")
    MP10=float(input("Digite o valor: 1) Partículas inaláveis: "))
    MP25=float(input("Digite o valor: 2) Partículas inaláveis finas: "))
    O3=float(input("Digite o valor: 3) Ozônio: "))
    CO=float(input("Digite o valor: 4) Onóxido de carbono: "))
    NO2=float(input("Digite o valor: 5) Dióxido de nitrogênio: "))
    SO2=float(input("Digite o valor: 6) Dióxido de enxofre: "))
    
    #linha responsável para guardar cada amostra no banco de dados
    comando = f"insert into Amostras values (DEFAULT, {MP10}, {MP25},  {O3}, {CO}, {NO2}, {SO2});" 
    executarComando(comando)            #executa o comando
    print("Amostra cadastrada!")
    selecionarOpcao()

#funcao destinada a exclusao de cada amostra selecionada pelo ID
def exclusaoAmostras():
    comando = "select * from amostras;" #exibe todas as amostras cadastradas
    amostras = executarComando(comando)
    for i in amostras:
        print(i)                        #print das amostras              
    
    idAmostra = input("Digite o ID da amostra na qual você quer excluir: ")
    comandoExcluir = f"delete from amostras where id = {idAmostra};" #exclui a amostra selecionada pelo id
    executarComando(comandoExcluir)                                  #executa o comando
    print(f"Amostra com o id {idAmostra} excluída!")
    selecionarOpcao()
    
#função feita para a alteracao de amostras cadastradas no banco
def alteracaoAmostras():
    comando = "select * from amostras;" #exibe as amostras
    amostras = executarComando(comando)

    for i in amostras:
        print(i)                        #print das amostras

    idAmostra = input("Selecione o id da amostra que deseja alterar: ")
    while True:
        print("Qual resposta você gostaria de alterar?")
        print("1) Partículas inaláveis (MP10)") 
        print("2) Partículas inaláveis finas (MP2,5)")
        print("3) Ozônio (O3)") 
        print("4) Onóxido de carbono (CO)") 
        print("5) Dióxido de nitrogênio (NO2)") 
        print("6) Dióxido de enxofre (SO2)") 
                    
        while True:
            try:   
                resp2=int(input("Digite a opção: ")) 
                if resp2 <1 or resp2 >6:
                    print("Opção inválida. Tente novamente!")
                    continue
                elif resp2 == 1:
                    MP10 = input("Digite o novo valor de MP10: ")
                    comando = f"update amostras set MP10 = {MP10} where id = {idAmostra};"
                elif resp2 == 2:
                    MP25 = input("Digite o novo valor de MP25: ")
                    comando = f"update amostras set MP25 = {MP25} where id = {idAmostra};"    
                elif resp2 == 3:
                    O3 = input("Digite o novo valor de O3: ")
                    comando = f"update amostras set O3 = {O3} where id = {idAmostra};"
                elif resp2 == 4:
                    CO = input("Digite o novo valor de CO: ")
                    comando = f"update amostras set CO = {CO} where id = {idAmostra};"
                elif resp2 == 5:
                    NO2 = input("Digite o novo valor de NO2: ")
                    comando = f"update amostras set NO2 = {NO2} where id = {idAmostra};"
                elif resp2 == 6:
                    SO2 = input("Digite o novo valor de SO2: ")
                    comando = f"update amostras set SO2 = {SO2} where id = {idAmostra};"
                    
                executarComando(comando)
                print("Valores corrigidos!")
                break
            except:ValueError
            print("APENAS NÚMEROS SÃO PERMITIDOS! TENTE NOVAMENTE.")

        alteracao = input("você gostaria de corrigir mais algum valor? (S/N)")
        if alteracao.upper() == "N":
            quit()
        selecionarOpcao()

#função feita para classificar todas as amostras salvas no banco de dados 
def classificarAmostras():
    comando = "select avg(MP10), avg(MP25), avg(O3), avg(CO), avg(NO2), avg(SO2) from amostras;"    #seleciona as amostras que estao inseridas no banco de dados
    mediaAmostras = executarComando(comando)
    
    #tupla responsavel para organizar as amostras no banco de dados
    MP10 = int(mediaAmostras[0][0])
    MP25 = int(mediaAmostras[0][1])
    O3 = int(mediaAmostras[0][2])
    CO = int(mediaAmostras[0][3])
    NO2 = int(mediaAmostras[0][4])
    SO2 = int(mediaAmostras[0][5])
    
    print(f"MP10 = {MP10}, MP25 = {MP25}, O3 = {O3}, CO = {CO}, NO2 = {NO2}, SO2 = {SO2}")
    verificarClassificacao(MP10, MP25, O3, CO, NO2, SO2)
    selecionarOpcao()

#faz a mesma coisa que a definição    
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


#função resonsavel para verificar a classificação das amostras inseridas no banco de dados
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


#menu para o usuário digitar qual função ele quer executar

print("Programa Para Calcular A Qualidade Do Ar!")

selecionarOpcao()

print("Obrigada por usar esse programa!")