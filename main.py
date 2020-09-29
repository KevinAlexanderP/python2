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
def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today?')
    print('[D]elete Client')
    print('[C]reate client')

if __name__ == '__main__':
  _print_welcome()
  command = input()

  
elif command == 'D':
        pass
    