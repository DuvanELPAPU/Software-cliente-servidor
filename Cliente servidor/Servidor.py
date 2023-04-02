import socket

# se crea el socket del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# se enlaza el socket a una dirección IP y puerto específicos
server_address = ('localhost', 8000)
server_socket.bind(server_address)

# se espera a que el cliente se conecte
server_socket.listen(1)

print('Esperando conexiones...')

# se acepta la conexión del cliente
client_socket, client_address = server_socket.accept()

# se abre el archivo y se lee su contenido
with open('archivo.txt', 'rb') as file:
    file_data = file.read()

# se envía el contenido del archivo al cliente
client_socket.send(file_data)

# se cierra la conexión
client_socket.close()
server_socket.close()