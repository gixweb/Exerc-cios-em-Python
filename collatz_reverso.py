num = int(input("informe o número: "))

while num != 1:
    if(num%2 == 0):
        num = (num*3)+1
        print(num)
    else: 
        num = num//2
        print(num)

'''
5
10
'''