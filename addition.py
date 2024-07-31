def addition(a,b):
    return a+b

def main():
    num1 = float(input('Enter first number: \n'))
    num2 = float(input('Enter second number: \n'))  

    #call the function
    result = addition(num1,num2)
    print('The sum of the two numbers is: ', result)

main()
     