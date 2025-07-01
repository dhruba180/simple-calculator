flag = "y" 
while  (flag=="Y" or flag=="y"):
    a=int(input("enter the 1st number = "))
    b=int(input("enter the 2nd number = "))
    print('1. Addition(+)')
    print('2. Multiplication(x)')
    print('3. Division(/)')
    print('4. Subtraction(-)')
    print('5. Persentage(%)')
    chose = int(input("chose ="))
    if chose == 1:             
        print (a+b)
    elif chose == 2:
        print (a*b)
    elif chose == 3:
        print (a/b)
    elif chose == 4:
        print(a-b)
    elif chose == 5:
        print(a/b*100)
    else:
     print("invalid oparation chose")
    flag=(input("Do you want to continue(y/n):"))
while not ( flag == "N" or flag == "n"):
     print("Invalid input! Please enter y or n.")
     flag = input("Do you want to continue? (y/n): ")
