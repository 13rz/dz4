#Завдання №1
# .2f-це для друку 2 знаків після коми
print("Нуль знак завершення работи програми")
while True:
     s = input("Знак (+,-,*,/,x2): ")
     if s == '0':
         break
     if s in ('+', '-', '*', '/','x2'):
         x = float(input("x="))
         y = float(input("y (якщо x2, ввсети в яку степінь)= "))
         if s == '+':
             print("%.2f" % (x+y))
         elif s == '-':
             print("%.2f" % (x-y))
         elif s == '*':
             print("%.2f" % (x*y))
         elif s == 'x2':
             print("%.2f" % (x**y))
         elif s == '/':
             if y != 0:
              print("%.2f" % (x/y))
             else:
                 print("Ділення на ноль!")
     else:
         print("Невірний знак операції!")

# #Задання №2
N = int (input("Число: "))
i, a = 1, 1
while a <= N:
    print (a, end=" ")
    i=i+1
    a = i**2

# Завдання №3
k = int(input("Число: "))

if k > 1:
    for i in range(2, int(k/2)+1):
         if (k % i) == 0:
            print("Це просте число")
            break
    else:
        print("Це просте число")

else:
    print("Це не просте число")