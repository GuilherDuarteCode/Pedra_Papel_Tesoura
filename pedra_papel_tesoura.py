# Bibliotecas que usei
import random 
from time import sleep
# O menu de entrada
def menu():
    print(20*"☆")
    print("""   PEDRA, PAPEL E TESOURA 
 ---THE CHAMPIONSHIP--- """)
    print(20*"☆")
    resposta = input(str(" deseja jogar? ? ? S/N: "))
    match resposta:
        case "s":
            game()
        case "n":
            print("tem certeza?S/N")
            resp = input()
            if resp == "s":
                print(""" MAQUINA 1X0 HUMANO"
                   VOCE PERDEU !!!
                    """)
                sleep(3)
                print("Encerrando o jogo")
                exit()
            elif resp == "n":
                print("reiniciando o jogo, aguarde um pouco")
                sleep(3) 
                return menu()            
def game():
    jogada_usuario = str(input("""esolha sua sua jogada: 
    1 - pedra 
    2 - papel
    3 - tesoura 
    """))
                              
    jogada_computador = str(random.randint(1, 3))
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO")
    sleep(1)

    #caso computador jogue pedra 
    if jogada_computador == "1" and jogada_usuario == "1":
        print("os dois jogadores jogaram pedra, DEU EMPATE !!!") 

    elif jogada_computador == "1" and jogada_usuario == "2":
        print("o computador jogou pedra e voce jogou papel, USUARIO VENCE !!!"
              )
    elif jogada_computador == "1" and jogada_usuario == "3":
        print("o computador jogou pedra e voce jogou tesoura, COMPUTADOR VENCE !!!")

    #caso computador jogue papel    
    elif jogada_computador == "2" and jogada_usuario == "1":
        print("o computador jogou papel e voce jogou pedra, COMPUTADOR VENCEU !!!") 

    elif jogada_computador == "2" and jogada_usuario == "2":
        print("os dois jogaram papel, DEU EMPATE !!!")

    elif jogada_computador == "2" and jogada_usuario == "3":
        print("o computador jogou papel e voce jogou tesoura, COMPUTADOR VENCE !!!")

    #caso computador jogue tesoura
    elif jogada_computador == "3" and jogada_usuario == "1":
        print("o computador jogou tesoura e voce jogou pedra, USUARIO VENCE !!!")

    elif jogada_computador == "3" and jogada_usuario == "2":
        print("o computador jogou pedra e voce jogou papel, USUARIO VENCE !!!")

    elif jogada_computador == "3" and jogada_usuario == "3":
        print("os dois jogadores jogaram tesoura, DEU EMPATE !!!") 
    
    else:
        print("erro no sistema")
    
    sleep(3)
    
    recomecar = str(input("deseja jogar denovo?: s/n: "))
    if recomecar == "s":
        return game()
    else:
        print("fim do jogo")

menu()
 
