import socket

#opens the file for reading
dbt = open("data.txt", 'r')

#creating the entries array
entries = []

#removes stores each entry and removes the whitespaces correctly, also error checks
for line in dbt:
    line = line.strip()
    if len(line.strip()) == 0:
        continue
    name, age, address, phone = line.split('|')
    if name == '':
        continue
    else:
        entries.append((name.strip(), age.strip(), address.strip(), phone.strip()))

#finds the customer in the database
def find_customer(value):
    for e in entries:
        if e[0] == value:
            return e[0] + "|" + e[1] + "|" + e[2] + "|" + e[3]
    
    return value + " not found in databse"

#adds a new customer       
def add_customer(value):
    name, age, address, phone = value.split(",")
    for e in entries:
        if e[0] == name:
            return "Customer already exists"
    
    entries.append((name.strip(), age.strip(), address.strip(), phone.strip()))
    return "Customer has been added"

#deletes a customer
def delete_customer(value):
    for e in entries:
        if e[0] == value:
            entries.remove(e)
            return "Customer has been removed"    
    
    return "Customer does not exist"

#updates the customer age
def update_age(value):
    name,age = value.split(",")
    for e in entries:
        if e[0] == name:
            age = (age,)
            e = e[:1] + age + e[2:]  
            entries.append(e)
            delete_customer(name)
            return "Customer age has been updated successfully"
    
    return "Customer does not exist"
        
#updates the customer address  
def update_address(value):
    name,address = value.split(",")
    for e in entries:
        if e[0] == name:
            address = (address,)
            new = e[:2] + address + e[3:]  
            entries.append(new)
            delete_customer(name)
            return "Customer address updated successfully"
    
    return "Customer does not exist"

#updates the customer phone number
def update_phone(value):
    name,phone = value.split(",")
    for e in entries:
        if e[0] == name:
            phone = (phone,)
            new = e[:3] + phone
            entries.append(new)
            delete_customer(name)
            return "Customer phone updates successfully"
    
    return "Customer does not exist"

#sorts the list
def report(entries):
    entries.sort(key=lambda x:x[0])

    message = "\n** Python DB contents **\n"

    for e in entries:
        message += (e[0] + "|" + e[1] + "|" + e[2] + "|" + e[3] + '\n')

    return message


def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 1024  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    server_socket.close()

    while True:
        try:
            # receive data stream. it won't accept data packet greater than 1024 bytes
            data = conn.recv(1024).decode()

            #to handle null data
            if not data:
                continue

            #modify data
            if data == "7":
                option = "7"
                value = None
            else:
                option, value = data.split("|")
            
            #check what input is
            if option == '1':
                data = find_customer(value)
            elif option == '2':
                data = add_customer(value)   
            elif option == '3':
                data = delete_customer(value)
            elif option == '4':
                data = update_age(value)
            elif option == '5':
                data = update_address(value)
            elif option == '6':
                data = update_phone(value)
            elif option == '7':
                data = report(entries)

            conn.send(data.encode())  # send data to the client
        except KeyboardInterrupt:
            break

if __name__ == '__main__':
    server_program()