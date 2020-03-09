import socket
import random
import time

HOST = "irc.twitch.tv"
PORT = 6667
NICK = "carneirooo" #Host
NICK2 = "bot_cabrito"
PASS = 'oauth:6sbwuhm824kov7o3bfluz7p1i9ciqt'
resposta = ""
rec = ""
lista_game = []
list_perg_resp = ["Quem inventou a lâmpada?", "Quem inventou o celular?", "Qual é o nome do jogo online para adivinhar o desenho feito?",
                  "Qual é o nome do jogo em que Leon S. Kennedy resgata Ashley?", "Qual é meu apelido?", "Qual é o nome da série que os assaltantes roubam a casa da moeda da Espanha?",
                  "Qual é o nome da marca de peças de computador que tem como logo uma águia", "Quando foi inventado o ventilador? (apenas o ano)"]
list_resp = ["alkmsdngjkas9324@##$nsajdh1b230gh854903tkldsma0-12938jndskalmf--0","thomas edison", "martin cooper", "gartic", "resident evil 4", "carneiro",
             "la casa de papel", "aorus", "1882"]
list_pao = []

cont1 = 0 #contador
cont2 = 0 #contador
cont3 = 0 #contador
cont4 = 0 #contador
cont5 = 0 #contador
cont6 = 0 #contador
num1 = 0 #posição 0
num2 = 1 #posição 1
pos = 0 #posição na matriz
pos1 = 0
alt_num = 0 #numero aletório
alt_num4 = 0 #numero aleatório
pos_vet_game = 0
pos_vet_game1 = 0

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i+1][1]>alist[i][1]:
                temp = alist[i+1]
                alist[i+1] = alist[i]
                alist[i] = temp

def pontos_rec(alt_num): #quantos pontos a pessoa vai receber
    rec = "Quem acertar ganha ", alt_num, " pontos"
    rec = str(rec)
    a = "()',"
    for i in range(0, len(a)):
        rec = rec.replace(a[i], "")
    return rec

def send_message(message):
    s.send(bytes("PRIVMSG #" + NICK + " :" + message + "\r\n", "UTF-8"))

s = socket.socket()
s.connect((HOST, PORT))
s.send(bytes("PASS " + PASS + "\r\n", "UTF-8"))
s.send(bytes("NICK " + NICK2 + "\r\n", "UTF-8"))
s.send(bytes("JOIN #" + NICK + " \r\n", "UTF-8"))
while True:
    line = str(s.recv(1024))
    if "End of /NAMES list" in line:
        break

while True:
    for line in str(s.recv(1024)).split('\\r\\n'):
        parts = line.split(':')
        if len(parts) < 3:
            continue

        if "QUIT" not in parts[1] and "JOIN" not in parts[1] and "PART" not in parts[1]:
            message = (parts[2][:len(parts[2])]).lower()

        usernamesplit = parts[1].split("!")
        username = usernamesplit[0]

        print(username + ": " + message)
        if message == "!comandos" or cont1 == 50:
            send_message("Os comandos disponíveis são: !uptime, !followage, !loots, !discord, !loot, !tt, !pontos, !rank e !loja")
            cont2 += 1
            cont3 += 1
            cont4 += 1
            cont5 += 1
            if cont1 == 50:
                cont1 -= cont1

        elif message == "!discord" or cont2 == 60:
            send_message("https://discord.gg/qPyyZ2j")
            cont1 += 1
            cont3 += 1
            cont4 += 1
            cont5 += 1
            if cont2 == 60:
                cont2 -= cont2

        elif message ==  "!loot" or cont3 == 70:
            send_message("Me ajude acessando meu link no loots e completando a missão xd: https://loots.com/carneirooo")
            cont1 += 1
            cont2 += 1
            cont4 += 1
            cont5 += 1
            if cont3 == 70:
                cont3 -= cont3

        elif message == "!tt" or cont4 == 80:
            send_message("Me siga no twitter: www.twitter.com/Carneiiroooo")
            cont1 += 1
            cont2 += 1
            cont3 += 1
            cont5 += 1
            if cont4 == 80:
                cont4 -= cont4

        elif message == "!pontos":
            for i in range(len(lista_game)):
                if username in lista_game[i][num1]:
                    pos = i
                else:
                    pos_vet_game += 1
            if pos_vet_game == len(lista_game):
                send_message("Você ainda não tem pontos")
                pos_vet_game -= pos_vet_game
            else:
                por = username, " tem ", lista_game[pos][num2], " pontos"
                por = str(por)
                a = "()',"
                for i in range(0, len(a)):
                    por = por.replace(a[i], "")
                send_message(str(por))
                pos_vet_game -= pos_vet_game

        elif message == "!rank":
            if not lista_game:
                send_message("Ainda não existe um ranking")
            else:
                xlen = len(lista_game)
                for i in range(xlen):
                    por = lista_game[i][num1], " tem ", lista_game[i][num2], " pontos"
                    por = str(por)
                    a = "()',"
                    for i in range(0, len(a)):
                        por = por.replace(a[i], "")
                    send_message(str(por))

        elif message == "!loja":
            if not lista_game:
                send_message("Ninguém tem pontos para comprar itens")
                break
            for i in range(len(lista_game)):
                if username in lista_game[i][num1]:
                    pos = i
                else:
                    pos_vet_game += 1
            if pos_vet_game == len(lista_game):
                npontos = "Você ainda não tem pontos", username
                npontos = str(npontos)
                a = "()',"
                for i in range(0, len(a)):
                    npontos = npontos.replace(a[i], "")
                send_message(str(npontos))
                pos_vet_game -= pos_vet_game
            else:
                send_message("LOJINHA")
                send_message("Digite !loja e o numero do item ex: !loja 1")
                send_message("1 - Pão || Valor 5 pontos")


        elif message == "!loja 1":
            if not lista_game:
                send_message("Ninguém tem pontos para comprar itens")
                break
            for i in range(len(lista_game)):
                if username in lista_game[i][num1]:
                    pos = i
                else:
                    pos_vet_game += 1
            if pos_vet_game == len(lista_game):
                npontos = "Você ainda não tem pontos", username
                npontos = str(npontos)
                a = "()',"
                for i in range(0, len(a)):
                    npontos = npontos.replace(a[i], "")
                send_message(str(npontos))
            else:
                pos_vet_game -= pos_vet_game
                if lista_game [pos][num2] >= 5:
                    lista_game [pos][num2] -= 5
                    send_message("Você comprou um pão")
                    if not list_pao:
                        list_pao.insert(len(list_pao), [username,1])
                        break
                    for i in range(len(list_pao)):
                        if username in list_pao[i][num1]:
                            pos = i
                        else:
                            pos_vet_game += 1
                    if pos_vet_game == len(list_pao):
                        list_pao.insert(len(list_pao), [username, 1])
                        print("asdasd")
                    else:
                        list_pao[pos][num2] = list_pao[pos][num2] + 1
                else:
                    send_message("Você não tem pontos suficientes para comprar esse item")
                pos_vet_game -= pos_vet_game

        elif message == "!itens":
            if not lista_game:
                send_message("Ninguém possi itens ainda")
                break
            for i in range(len(list_pao)):
                if username in list_pao[i][num1]:
                    pos1 = i
                else:
                    pos_vet_game1 += 1
            if username == list_pao[pos1][num1]:
                nitens = username, " tem ", list_pao[pos1][num2], "pães"
                nitens = str(nitens)
                a = "()',"
                for i in range(0, len(a)):
                    nitens = nitens.replace(a[i], "")
                send_message(str(nitens))
                pos_vet_game -= pos_vet_game
            else:
                send_message("Você não tem itens")
                pos_vet_game -= pos_vet_game

        elif cont5 == 8:
            alt_num = random.randint(2, 20)  # numero aleatório pra quantidade de pontos que vão ganhar
            alt_num2 = random.randint(0, 2)  # numero aleatório pra falar que vem pergunta
            alt_num3 = random.randint(5, 15)  # numero aleatório pro tempo
            alt_num4 = random.randint(0, 7)  #numero aleatório pra pergunta e resposta
            list_perg = ["Lá vem pergunta", "Estou tirando um desafio do forno", "Vou fazer um desafio"]
            send_message(list_perg[alt_num2])
            time.sleep(2)
            send_message(pontos_rec(alt_num))
            time.sleep(alt_num3)
            send_message(list_perg_resp[alt_num4])
            cont5 -= cont5

        elif message == list_resp[alt_num4+1]:
            send_message("Acertou!!")
            for i in range(len(lista_game)):
                if username in lista_game[i][num1]:
                    pos = i
            if not lista_game:
                lista_game.insert(len(lista_game), [username, alt_num])
                por = lista_game[num1][num1], " fez ", lista_game[num1][num2], " pontos"
                por = str(por)
                a = "()',"
                for i in range(0, len(a)):
                    por = por.replace(a[i], "")
                send_message(str(por))
            elif username in lista_game[pos][num1]:
                lista_game[pos][num2] = lista_game[pos][num2] + alt_num
                por = username, " tem ", lista_game[pos][num2], " pontos"
                por = str(por)
                a = "()',"
                for i in range(0, len(a)):
                    por = por.replace(a[i], "")
                send_message(str(por))
            else:
                lista_game.insert(len(lista_game), [username, alt_num])
                xlen = len(lista_game)
                por = username, " fez ", lista_game[xlen-1][num2], " pontos"
                por = str(por)
                a = "()',"
                for i in range(0, len(a)):
                    por = por.replace(a[i], "")
                send_message(str(por))
            alt_num4 = 0
            bubbleSort(lista_game)

        else:
            cont1 += 1
            cont2 += 1
            cont3 += 1
            cont4 += 1
            cont5 += 1