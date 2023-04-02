import socket

# se crea el socket del cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# se conecta al servidor
server_address = ('localhost', 8000)
client_socket.connect(server_address)

# se recibe el contenido del archivo del servidor
file_data = client_socket.recv(1024)

# se crea un nuevo archivo y se escribe el contenido recibido
with open('nuevo_archivo.txt', 'wb') as file:
    file.write(file_data)

# se cierra la conexión
client_socket.close()