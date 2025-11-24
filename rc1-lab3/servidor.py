#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

def servidor_tcp():
    # Cria socket TCP
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define endereço e porta
    host = '0.0.0.0'  # Escuta em todas as interfaces
    porta = 12345

    # Vincula socket ao endereço
    servidor_socket.bind((host, porta))

    # Escuta por conexões (máx 5)
    servidor_socket.listen(5)
    print(f"Servidor TCP escutando em {host}:{porta}")

    try:
        while True:
            print("Aguardando conexão...")

            # Aceita conexão
            cliente_socket, endereco_cliente = servidor_socket.accept()
            print(f"Conexão estabelecida com {endereco_cliente}")

            # Recebe dados do cliente
            dados = cliente_socket.recv(1024).decode()
            print(f"Dados recebidos: {dados}")

            # Processa dados (eco de volta)
            resposta = f"ECO: {dados}"

            # Envia resposta
            cliente_socket.send(resposta.encode())
            print(f"Resposta enviada: {resposta}")

            # Fecha conexão com cliente
            cliente_socket.close()
            print(f"Conexão com {endereco_cliente} fechada\n")

    except KeyboardInterrupt:
        print("\nServidor encerrado.")
    finally:
        servidor_socket.close()

if __name__ == "__main__":
    servidor_tcp()
