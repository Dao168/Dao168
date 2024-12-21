import socket

# ກໍານົດ IP ແລະ Port ທີ່ຈະຊື່ມຕອບ
server_ip = '127.0.0.1'  # IP ຂອງ server (ເຊິງມັກເປັນ 'localhost')
server_port = 12345      # Port ທີ່ກຳນົດທາງຂ້າງ Server

# ສ້າງ socket ແລະທຳການຊື່ມຕອບ
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ທຳການເຊື່ອມຕອບກັບ server
client_socket.connect((server_ip, server_port))

# ສົງຄຳຂໍຜ່ານ socket
message = "Hello, Server!"
client_socket.send(message.encode('utf-8'))

# ຮັບຄຳຕອບຈາກ Server
response = client_socket.recv(1024).decode('utf-8')
print(f"Received response from server: {response}")

# ປິດສະເກຣິບການທຳງານ
client_socket.close()
