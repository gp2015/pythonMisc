def collatz(number):
    num_mod = number % 2
    if (num_mod == 0):
        return print(num_mod)
    else:
        return print(3 * number + 1)
        
while (user != 1):
    user = collatz(input())