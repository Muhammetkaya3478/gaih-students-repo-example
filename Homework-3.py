def prime_first():
    for number in range(0,500):
        if number > 1:
            for i in range(2,number):
                if(number%i)==0:
                    break
            else:
                print(number)

def second_first():
    for number1 in range(500,1000):
        if number1>1:
            for i in range(2,number1):
                if(number1%i)==0:
                    break
            else:
                print(number1)

for i in range(1):
    prime_first()
for j in range(1):
    second_first()