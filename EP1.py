from os import system , name
def limpaTela():
    """
    Essa função limpa o terminal.
    """
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def cardapio():
    """
    Essa função é o inicio do programa e exibe os jogos disponíveis e seus respectivos valores.
	"""
    RESET   = '\033[39m'
    MAGENTA = '\033[35m'
    print("\n--- MOBILE GAMES STORE ---")
    print(MAGENTA)
    print("| 1 - Subway Surfers.................R$ 80,00 |")
    print("| 2 - Pou............................R$ 50,00 |")
    print("| 3 - Candy Crush....................R$ 10,00 |")
    print("| 4 - Angry Birds...................R$ 100,00 |")
    print("| 5 - Pokémon GO.....................R$ 20,00 |")
    print(RESET)

def escolha(v):
    """
    Essa função retorna o valor de cada jogo consoante a escolha do usuário da máquina. "V" é a escolha do usuário.
    """
    if v == 1:
        return float(80)
    if v == 2:
        return float(50)
    if v == 3:
        return float(10)
    if v == 4:
        return float(100)
    if v == 5:
        return float(20)

def compra(p):
    """
    Essa função faz toda a operação de compra e retorna o valor do troco. 
    Caso o "d" (Dinheiro pago) seja menor que  "p" (Preço do produto) o programa exibe 
    uma mensagem e retorna para o inicio do processo de compra.
    """
    RESET   = '\033[39m'
    MAGENTA = '\033[35m'
    d = float(input("Digite seu pagamento:"))
    troco = float(d - p)
    if d < p:
        print(MAGENTA)
        print("Dinheiro insuficiente, tente novamente.")
        print(RESET)
        return compra(p)
    if troco >= 0:
        print(f"Seu troco é: {troco:.2f}")
        return round(troco,2)


def troco(t):
    """
    Essa função recebe o valor do troco o qual foi retornado na função "compra()" e divide 
    no número mínimo de notas e moedas (sem “roubar” nem mesmo 1 centavo!).
    """
    t = round(t,2) #Arredondamento feito para que a máquina não roube ou dê um centavo
    if t >= 0.01:
        if t >= 100:
            print("R$100,00")
            return troco(t-100)
        elif 100 > t >= 50:
            print("R$50,00")
            return troco(t-50)
        elif 50 > t >= 20:
            print("R$20,00")
            return troco(t-20)
        elif 20 > t >= 10:
            print("R$10,00")
            return troco(t-10)
        elif 10 > t >= 5:
            print("R$5,00")
            return troco(t-5)
        elif 5 > t >= 2:
            print("R$2,00")
            return troco(t-2)
        elif 2 > t >= 1:
            print("R$1,00")
            return troco(t-1)
        elif 1 > t >= 0.50:
            print("R$0,50")
            return troco(t-0.50)
        elif 0.50 > t >= 0.25:
            print("R$0,25")
            return troco(t-0.25)
        elif 0.25 > t >= 0.10:
            print("R$0,10")
            return troco(t-0.10)
        elif 0.10 > t >= 0.05:
            print("R$0,05")
            return troco(t-0.05)
        elif 0.05 > t >= 0.01:
            print("R$0,01")
            return troco(t-0.01)


def main(subSurf = 5, pou = 5, candyCrush = 5, angryBirds = 5, pokemon = 5):
    """
    A função main tem como parâmetro a quantidade de cada produto, ou seja, o estoque. Além de trabalhar
    como estoque, a função main contém os inputs necessários para a coleta dos dados no
    processo de execução da compra.
    """
    RESET   = '\033[39m'
    MAGENTA = '\033[35m'
    if subSurf <=0 and pou <= 0 and candyCrush <= 0 and angryBirds <= 0 and pokemon <= 0: #Condição para exibir a mensagem de fim do estoque de todos os games
        print(MAGENTA)
        print("Fim do estoque geral")
        print(RESET)
    else:
        cardapio()
        v = int(input("Digite sua escolha:")) #Só aceita números inteiros
        if v != 1 and v != 2 and v != 3 and v != 4 and v != 5:
            print("Escolha não reconhecida, tente novamente")
            _ = input("--> Enter para continuar...")
            return main(subSurf, pou, candyCrush, angryBirds, pokemon)
        if subSurf <=0 and pou <= 0 and candyCrush <= 0 and angryBirds <= 0 and pokemon <= 0:
            print("Fim do estoque geral")
        #Consoante a escolha, é diminuido uma unidade do estoque.
        if v == 1:
            subSurf -= 1
        if v == 2:
            pou -= 1
        if v == 3:
            candyCrush -= 1
        if v == 4:
            angryBirds -= 1
        if v == 5:
            pokemon -= 1
        #Mensagem de erro que é exibida quando há excassez de um dos produtos
        if v == 1 and subSurf <= -1:
            print(MAGENTA)
            print("Produto não disponível. Que tal dar uma olhada no resto do nosso catálogo?")
            print(RESET)
            _ = input("--> Enter para continuar...")
            limpaTela()
            return main(subSurf, pou, candyCrush, angryBirds, pokemon)
        if v == 2 and pou <= -1:
            print(MAGENTA)
            print("Produto não disponível. Que tal dar uma olhada no resto do nosso catálogo?")
            print(RESET)
            _ = input("--> Enter para continuar...")
            limpaTela()
            return main(subSurf, pou, candyCrush, angryBirds, pokemon)
        if v == 3 and candyCrush <= -1:
            print(MAGENTA)
            print("Produto não disponível. Que tal dar uma olhada no resto do nosso catálogo?")
            print(RESET)
            _ = input("--> Enter para continuar...")
            limpaTela()
            return main(subSurf, pou, candyCrush, angryBirds, pokemon)
        if v == 4 and angryBirds <= -1:
            print(MAGENTA)
            print("Produto não disponível.Que tal dar uma olhada no resto do nosso catálogo?")
            print(RESET)
            _ = input("--> Enter para continuar...")
            limpaTela()
            return main(subSurf, pou, candyCrush, angryBirds, pokemon)
        if v == 5 and pokemon <= -1:
            print(MAGENTA)
            print("Produto não disponível.Que tal dar uma olhada no resto do nosso catálogo?")
            print(RESET)
            _ = input("--> Enter para continuar...")
            limpaTela()
            return main(subSurf, pou, candyCrush, angryBirds, pokemon)
        p = escolha(v)
        t = compra(p)
        troco(t)
        #Fim da compra, com opções de finalizar o uso da máquina ou executar outra compra.
        volta = input("Deseja comprar novamente?(s/n)")
        while volta !="s" and volta !="S" and volta != "n" and volta != "N":
            limpaTela()
            print("Escolha não reconhecida, tente novamente")
            volta = input("Deseja comprar novamente?(s/n)")
        if volta == "s" or volta == "S":
            limpaTela()
            return main(subSurf, pou, candyCrush, angryBirds, pokemon)
        elif volta == "n" or volta == "N":
            print(MAGENTA)
            print("Obrigado por usar nossa máquina!")
            print(RESET)
            _ = input("--> Enter para continuar...")
            exit()

main()