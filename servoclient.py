import socket
import datetime

HOST = input('Enter Host: ')
PORT = input('PORT (8000): ')
if PORT == '':
    PORT = 8000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((HOST, int(PORT)))
count = server.recv(1048)
for i in range(int(count.decode())):
    name = server.recv(100).decode('utf-8')
    if name == '':
        name = str(datetime.datetime.now()).replace('-', '').replace('.', '').replace(':', '').replace(' ', '')
    print('File {} out of {}'.format(i+1, count.decode()))
    print('Transfering {}\r'.format(name), end='')
    file = open(name, 'wb')
    chunk = server.recv(2048)
    while chunk:
        if chunk.endswith('utdlinked-end'.encode("utf-8")):
            file.write(chunk.replace('utdlinked-end'.encode('utf-8'), ''.encode('utf-8'), 1))
            print('{}/{} {} has been Transfered Successfully'.format(i+1, count.decode(), name))
            name = 'Cleared'
            chunk = ''
            break
        file.write(chunk)
        chunk = server.recv(2048)
    file.close()
print('All {} File(s) are Transfered Successfully'.format(count.decode()))
server.close()