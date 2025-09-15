## Readme - Calculadora Cliente-Servidor

Uma calculadora que em que o cliente envia uma operacao no formato "Número Operação Número" para o servidor que processa e manda de volta um float transformado em string.

### Operações Válidas

As operações válidas são:

* '+' Soma: Soma os dois números.
* '-' Subtração: Subtrai o segundo número do primeiro número.
* '*' Multiplicação: Multiplica os dois números.
* '/' Divisão: Divide o primeiro número pelo o segundo número.
* '**' Potência: Eleva o primeiro número pelo segundo número.
* '==', '=': Verifica se o primeiro número é igual ao segundo.


Em caso de operação inválida, o servidor é encerrado.

### Execução


Para executar rode o servidor com o comando:

$ python3 Server.py

e o cliente com o comando:

$ python3 Client.py

O código padrão está configurado para funcionar em local host com a porta 8081. Para utilizar entre computadores distintos, o ipv4 do servidor deve ser colocado na variável host, em ambos os códigos "Client.py" e "Server.py".

### Funções Princípais do Servidor.
No servidor a função calcular(expr); Calcula o resultado da expressão expr. A função verifica se a operação encontrada é uma operação válida, se for realiza a operação e retorna o resultado, se não imprime 'Operação inválida' e encerra o programa.

A função Server(host, port); Cria um socket com o endereço host e a porta port associada a ele. Deixa o socket disponível para conexão. E roda um loop, enquanto espera por conexões. Ao conectar aguarda por uma mensagem do cliente, processa a mensagem e retorna o resultado se for uma operação válida e se mantém no loop até que a conexão seja encerrada.