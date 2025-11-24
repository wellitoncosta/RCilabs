#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

def cliente_tcp(host_servidor, porta_servidor, mensagem):
    # Cria socket TCP
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Conecta ao servidor
        print(f"Conectando a {host_servidor}:{porta_servidor}...")
        cliente_socket.connect((host_servidor, porta_servidor))
        print("Conectado!")

        # Envia mensagem
        print(f"Enviando: {mensagem}")
        cliente_socket.send(mensagem.encode())

        # Recebe resposta
        resposta = cliente_socket.recv(1024).decode()
        print(f"Resposta do servidor: {resposta}")

    except Exception as e:
        print(f"Erro: {e}")

    finally:
        # Fecha socket
        cliente_socket.close()
        print("Conexão fechada.")

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 4:
        print("Uso: python cliente.py <host> <porta> <mensagem>")
        print("Exemplo: python cliente.py 192.168.56.21 12345 'Olá servidor!'")
        sys.exit(1)

    host = sys.argv[1]
    porta = int(sys.argv[2])
    mensagem = sys.argv[3]

    cliente_tcp(host, porta, mensagem)
