import socket

def welcome():  
    print("""Python DB Menu

    1. Find customer
    2. Add customer
    3. Delete customer
    4. Update customer age
    5. Update customer address
    6. Update customer phone
    7. Print report
    8. Exit

    Select:""")

#def find customer
def find_customer(message):
    name = input("What is the name of such customer: ")
    message = message + "|" + name
    return message

#def add_customer
def add_customer(message): 
    name = input("What is the name? ")
    while name == "":
        name = input("Please input a valid name: ")
    
    age = input("What is the age? ")
    address = input("What is the address? ")
    phone = input("What is the phone? ")

    value = name + "," + age + "," + address + "," + phone
    message = message + "|" + value

    return message

#def delete_customer
def delete_customer(message):
    name = input("What is the name? ")
    message = message + "|" + name

    return message

#def update_age
def update_age(message):
    name = input("What is the name? ")
    age = input("What is the age? ")

    value = name + "," + age
    message = message + "|" + value

    return message

#def update_address
def update_address(message):
    name = input("What is the name? ")
    address = input("What is the address? ")

    value = name + "," + address
    message = message + "|" + value

    return message

#def update_phone
def update_phone(message):
    name = input("What is the name? ")
    phone = input("What is the phone? ")

    value = name + "," + phone
    message = message + "|" + value

    return message

#def report
def report(message):
    return message

def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 1024  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    
    message = ""

    while True:
        welcome()
        message = input(" -> ")  # take input
        if message == '8':
            break

        #check what input is
        if message == '1':
            message = find_customer(message)
        elif message == '2':
            message = add_customer(message)   
        elif message == '3':
            message = delete_customer(message)
        elif message == '4':
            message = update_age(message)
        elif message == '5':
            message = update_address(message)
        elif message == '6':
            message = update_phone(message)
        elif message == '7':
            message == report(message)

        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data + "\n")  # show in terminal

    print("Thank you for using the program.")
    client_socket.close()  # close the connection

if __name__ == '__main__':
    client_program()