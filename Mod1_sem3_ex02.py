def recursao(num):
    print(num)
    num -= 1
    if num == (0-1):
        return
    else:
        recursao(num)


#Programa Principal:
recursao(20)