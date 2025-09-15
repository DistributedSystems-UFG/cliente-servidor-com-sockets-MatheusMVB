import socket
import os

def client(host="127.0.0.1", port=8081): # Cria client

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_add = (host, port)
    print("Conectando ao add %s port %s" % server_add)
    sock.connect(server_add)

    while True:

        os.system('clear')
        print("############# Calculadora Cliente-Servidor ##################")
        print("1) Digite sua operação(+, -, *, /, **, =, ==): ")
        print("2) Digite 'q' para sair:")
        mensage = input()
        if(mensage == 'q'):
            print("Closing connection to the server")
            sock.sendall(mensage.encode())
            sock.close() 
            break
        
        sock.sendall(mensage.encode('utf-8'))
        response = sock.recv(2048).decode()
        print("O resultado da operação %s é %s" % (mensage, response))
 
        input("Pressione 'Enter' para continuar...") 



client()

