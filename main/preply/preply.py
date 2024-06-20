import re
def main():
    while True:
        expression= input('enter arithmatic terms: ')
        
        
        if expression.lower() == 'exit':
            print('goodbye')
            break
        
        match= re.match(r"(\d+)\s*([+/*-])\s*(\d+)",expression)

        if not match:
            print('try again')
            continue
        
        
        x,y,z= match.groups()
        
        x = int(x)
        y = int(y)
        result = 0.0

        if y=='+':
            result = x+z
        elif y=='-':
            result = x-z
        elif y=='*':
            result = x*z
        elif y=='/':
            result = x/z
        else:
            print('invalid')
        continue
        
        print(f"{result:.1f}")

if __name__ == "__main__":
    main()


        
        


        




