
def choosefiles():
    from tkinter import Tk, filedialog
    root = Tk()
    root.title('File Transfer')
    root.withdraw()
    root.attributes('-topmost', True)
    files = filedialog.askopenfilenames(title='Choose Files')
    return files
def connection():
    import socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    HOST = socket.gethostname()
    PORT = 8000
    print("""Information
        Host: {}
        Port: {}
    """.format(HOST, PORT))
    server.bind((HOST, PORT))
    print('Waiting For Connection')
    server.listen(5)
    client_socket, address = server.accept()
    print("""Connected
        Address: {}
    """.format(address))
    files = choosefiles()
    client_socket.send(str(len(files)).encode('utf-8'))
    for file in files:
        i = 1
        filename = str(file).split('/')[-1]
        print("""Transfering
        Count: {}/{}
        Name: {}
        """.format(i, len(files), filename))
        client_socket.send(filename.encode('utf-8'))
        reading = open(file, 'rb')
        data_in_file = reading.read(2048)
        while data_in_file:
            client_socket.send(data_in_file)
            data_in_file = reading.read(2048)
        client_socket.send('utdlinked-end'.encode())
        reading.close()
        i += 1
        filename = ''
    client_socket.close()
if __name__ == '__main__':
    connection()