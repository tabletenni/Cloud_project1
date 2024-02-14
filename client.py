from socket import *

serverName = '10.31.0.100'
serverPort = 12000

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

client_socket = socket(AF_INET, SOCK_STREAM)

client_socket.connect((serverName, serverPort))
print('---------------------------------')
print("Connected to server. 200, 'OK'")

while True:
    message = input("Enter your message (type 'exit' to close): ")

    client_socket.send(message.encode())

    if message.lower() == 'exit':
        message = "Closing connection..."
        print("Closing connection...")
        client_socket.close()
        break

    encrypted_response = client_socket.recv(1024).decode()

    response = decrypt_message(encrypted_response)
    print(f"Received from server (encrypted): {encrypted_response}")
    print(f"Decrypted response: {response}")

client_socket.close()
