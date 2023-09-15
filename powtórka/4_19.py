#19.	Define a function that checks if the number is within the given range <x, y>. 
# The function returns boolean value. Then create a program and use the function you defined.

def fun(x, y, z):
    if z>x and z<y:
        return True
    else: return False
    
print(fun(1, 10, 4))