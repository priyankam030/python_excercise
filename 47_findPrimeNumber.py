# write 

n = int(input("Enter a number: "))

for i in range(2, int(n/2)):
    if(n%i) == 0:
        print(str(n) + " Number is not prime")
        break

print(f"{n} is Number is prime")    
    # break