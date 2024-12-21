

import socket

# ກໍານົດ IP ແລະ Port ທີ່ Server ຈະຟັງ
host = '0.0.0.0'  # ເພື່ອຮັບຄຳຂໍຂອງທຸກ IP
port = 12345       # ກຳນົດ Port ທີ່ຈະຮັບ

# ສ້າງ socket ສໍາລັບການຕິດຕາມຜູ້ຮັບ
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ກໍານົດການເຊື່ອມຕອບ
server_socket.bind((host, port))

# ເຮັດໃຫ້ server ພິມຕົວພິມເວົ້າວເວົ້າ
server_socket.listen(5)  # ກຳນົດຄວາມສາມາດຮັບເວລາເທົາ

print(f"Server listening on {host}:{port}...")

# ຍອດຮັບທີ່ມາ
client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address} has been established!")

# ຮັບຄຳຂໍຂອງຜູ້ຮັບ
message = client_socket.recv(1024).decode('utf-8')
print(f"Received message: {message}")

# ສົງຄືນຄຳຕອບກັບ Client
response = "Message received!"
client_socket.send(response.encode('utf-8'))

# ປິດສະເກຣິບການທຳງານ
client_socket.close()
server_socket.close()
