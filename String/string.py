def reverse_str(str1):
    if len(str1)==1:
        return str1
    else:
        return reverse_str(str1[1:]) + str1[0]

str1 = input("Eneter Sting")
print(str1[1::])
string= reverse_str(str1)
print(string)

def loop(n):
    # print("hai")
    for i in range(n,0,-1):
        print(i,end=" ")

loop(10)