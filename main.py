clients = 'pablo,ricardo, '

def create_client(client_name):
    global clients
    clients += client_name

def list_clients():
    global clients
    print(clients)

    clients += ','
def add_comma():
    global clients

    clients += ','
def print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today?')
    print('[D]elete Client')
    print('[C]reate client')

    clients += ','

if name == '__main__':
    client_name= input('What is the client name')
    create_client(client_name)
    list_clients()