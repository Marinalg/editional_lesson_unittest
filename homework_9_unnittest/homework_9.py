def arithmetic(a,b, oper):
    if oper == "*":
        return a * b
    elif oper == "/":
        return a / b
    elif  oper == "+":
        return a+b
    elif oper == "-":
        return a - b
    else:
        print("Not know operation")
        return 0