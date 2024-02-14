from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
key = 4

def encrypt_message(message):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            en = ord(char) + key
            if char.islower():
                if en > ord('z'):
                    en -= 26
            elif char.isupper():
                if en > ord('Z'):
                    en -= 26
            encrypted_message += chr(en)
        else:
            encrypted_message += char
    return encrypted_message

def decrypt_message(encrypted_message):
    decrypted_message = ""
    for char in encrypted_message:
        if char.isalpha():
            de = ord(char) - key
            if char.islower():
                if de < ord('a'):
                    de += 26
            elif char.isupper():
                if de < ord('A'):
                    de += 26
            decrypted_message += chr(de)
        else:
            decrypted_message += char
    return decrypted_message

print("Server is listening for incoming connections...")

connection_socket, client_address = serverSocket.accept()
print('---------------------------------')
print(f"Connection established with {client_address}")

while True:
    encrypted_message = connection_socket.recv(1024).decode()
    decrypted_message = decrypt_message(encrypted_message)
    
    if decrypted_message.strip().lower() == 'exit':
        print("Client has closed the connection.")
   
    
    print(f"Received from client : {decrypt_message}")
    print(f"Encrypted message : {encrypted_message}")

    response = input("Enter your response: ")
    encrypted_response = encrypt_message(response)
    connection_socket.send(encrypted_response.encode())

