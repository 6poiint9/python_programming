x = 42 

print(type(x))



def check_login(username, password):
    passw = "pass69" 
    user = "admin"

    if passw == password and user == username:
        return True 
    else: 
        return False 


u = input("Enter username: "); 

p = input("Enter password: "); 

is_login_successfull = check_login(u, p); 

if is_login_successfull:
    print("Login successful")
else:
    print("Login failed")
