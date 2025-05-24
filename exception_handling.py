def hello():
    try:
        a=int(input("Enetr a number"))
        print (a)
    except Exception as e:
        print("enter valid number")    
    finally:
        print("nooo")
        print(__name__)   #when we import this function in another page this shows the page containing the function

i=10