
numero_id = []
defeito_lista = []
consulta_lista = []
defeito_scroll = 0
defeito_limpeza = 0
defeito_cabo = 0
defeito_quebrado = 0
sem_defeitos = 0

tracinho = "-" * 25

print()
print("Bem vindo(a)! Aqui você irá conseguir realizar o levantamento de mouses do deposito.")

def tabelaDefeitos():
    print()
    print(tracinho.center(50))
    print("Há 4 tipos de defeitos cadastrados:".center(50))
    print(tracinho.center(50))
    print("a -> Problemas no scroll")
    print("b -> necessita de limpeza")
    print("c -> Problemas no cabo ou conector")
    print("d -> totalmente quebrado")
    print()
    print("Para mouses sem nenhum defeito digite -> e")
    print()
    print(tracinho.center(50))
    print()
    print("Comece digitando o número de identificação do mouse, depois quando solicitado informe o código correspondente ao defeito")
    print("Para encerrar a entrada de dados digite '0'(número zero) no número de identificação do mouse")
    print()
    
tabelaDefeitos()

while True:
    mouse= int(input("Digite o número de identificação do mouse: "))
    if mouse != 0:
        numero_id.append(mouse)
        defeito= input("digite o defeito: ")
        consulta_lista.append(defeito)
        if defeito == "a":
            defeito = "Problemas no scroll"
            defeito_lista.append(defeito)
            defeito_scroll += 1
        elif defeito == "b":
            defeito = "necessita de limpeza"
            defeito_lista.append(defeito)
            defeito_limpeza += 1
        elif defeito == "c":
            defeito = "Problemas no cabo ou conector"
            defeito_lista.append(defeito)
            defeito_cabo += 1
        elif defeito == "d":
            defeito = "totalmente quebrado"
            defeito_lista.append(defeito)
            defeito_quebrado += 1
        elif defeito == "e":
            defeito = "sem defeitos"
            defeito_lista.append(defeito)
            sem_defeitos += 1
    else:
        break
            
def consultar():
    while True:
        print()
        perguntaConsulta = (input("Deseja fazer alguma consulta em relação aos mouses? ['s' para sim e 'n' para não] "))
        print()
        if perguntaConsulta == "s":
            escolha = input("Se deseja fazer a pesquisa pelo numero de identificação digite 'id', caso queira fazer a pesquisa para descobrir quais mouses estão com o defeito pensado digite 'def': ")
            if escolha == "id":
                print()
                consultaID = int(input("Qual id quer consultar? "))
                for i in range(0,len(numero_id)):
                    if numero_id[i] == consultaID:
                        print()
                        print(consultaID, "-", defeito_lista[i])
            elif escolha == "def":
                print()
                consultaDefeito = input("Qual defeito quer consultar? ")
                for i in range(0,len(consulta_lista)):
                    if  consulta_lista[i] == consultaDefeito:
                        print()
                        print(consultaDefeito,"      ", "->", "     ", numero_id[i])
            else:
                print()
                print("!!comando inválido!!")
                break
        else:
            break
        
def imprimirResultados():
    print(tracinho.center(50))
    print("Quantidade total de mouses = ", len(numero_id))
    print(tracinho.center(50))
    print("SITUAÇÃO", "             ","      ", "QUANTIDADE", "  ", "PERCENTUAL")
    print("a - Problemas no scroll", "         ", defeito_scroll, "         ",round((defeito_scroll/len(numero_id)* 100), 1), "%")
    print("b - Necessita de limpeza", "        ",defeito_limpeza,"         ", round((defeito_limpeza/len(numero_id)* 100), 1), "%")
    print("c - Problemas no cabo ou conector", defeito_cabo,"         ", round((defeito_cabo/len(numero_id)* 100), 1), "%")
    print("d - Totalmente quebrado", "         ", defeito_quebrado,"         ",round((defeito_quebrado/len(numero_id)* 100), 1), "%")
    print("e - Sem defeitos", "                ", sem_defeitos,"         ",round((sem_defeitos/len(numero_id)* 100), 1), "%")
    print(tracinho.center(50))

consultar()
print()
imprimirResultados()

while True:
    print()
    pergunta2 = input("Deseja pesquisar mais algum id ou encerrar o programa? [digite 's' para pesquisar e 'n' para encerrar] " )
    if pergunta2 == "s":
        consultar()
    else:
        print()
        print(tracinho.center(50))
        print("Ok, até mais!".center(50))
        print(tracinho.center(50))
        break




    
