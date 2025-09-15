import socket

def soma(a, b): return a + b
def subtracao(a, b): return a - b
def multiplicacao(a, b): return a * b
def divisao(a, b): return a / b
def potencia(a, b): return a ** b
def igual(a, b): return a == b


ops = { # Defini as operações validas
    "+": soma,
    "-": subtracao,
    "*": multiplicacao,
    "/": divisao,
    "**": potencia,
    "=": igual,
    "==": igual
}

def calcular(expr): # Calacula a operação
    for op in sorted(ops.keys(), key=lambda x: -len(x)):  # trata ** antes de *
        if op in expr: # Verifica se a operação é valida
            esquerda, direita = expr.split(op, 1)
            return ops[op](float(esquerda), float(direita))
    raise ValueError("Operação inválida")



def server (host="127.0.0.1", port=8081): # Cria um servidor

    data_payload = 2048 # tamanho maximo do pacote a ser recebido de uma vez.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # define um socket com padrão de endereço ipv4 e protocolo tcp. 
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # permite a reutilização do mesmo endereço
    server_add = (host, port)
    print("Servidor inicializado add %s port %s" % server_add)
    sock.bind(server_add) # Associa o endereço do servidor ao socket
    sock.listen(1) # Deixe o socket esperando uma conexão, com no maximo 1 conexao.

    while True:
        print("Esperando por cliente...")
        client, add = sock.accept() # Conexão aceita
        while True:
            data = client.recv(data_payload).decode()
            if data:
                print("Data: %s" % data)
                if(data == 'q'): # Se o programa cliente for encerrado, encerra o loop e espera uma nova conexão
                    client.close()
                    break
                data = calcular(data)
                print("Data pos calcular: %s" %data) # Para verificar se a operação foi realizada com sucesso
                data = str(data).encode() # Transforma de float para string e depois codifica para ser enviado
                client.send(data)
                print("Send %s bytes back to %s" % (data, add)) # Para verificar se a mensagem certa realmente está sendo enviada, retirar depois
            
           


server()

