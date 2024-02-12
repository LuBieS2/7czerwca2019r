def sum(number):
    n_list = []
    number=str(number)
    s = 0
    for i in number:
        n_list.append(i)
    for i in n_list:
        ii = int(i)
        s += ii
    return s
def loaddata(file):
    content=open(file)
    data=list(map(str.strip, content.readlines()))
    return data
def backwards(number):
    num = ""
    for i in range(len(number)):
        num += number[len(number) - 1 - i]
    return num
def is_prime(a):
    for i in range(int(a**(1/2)+1)):
        if i!=1 and i!=0 and i!=a:
            if a%i==0:
                return False
    return True
def zadanie1():
    numbers=loaddata("liczby_przyklad.txt")
    prime_n=[]
    for n in numbers:
        n=int(n)
        if 100 <= n <= 5000 and is_prime(n):
            prime_n.append(n)
    print(prime_n)
zadanie1()
def zadanie2():
    numbers=loaddata("pierwsze_przyklad.txt")
    numbers1=[]

    for n in numbers:
        i=backwards(n)
        numbers1.append(i)
    primes=[]
    for i in range(len(numbers)):
        i=int(i)
        if is_prime(int(numbers[i])) and is_prime(int(numbers1[i])):
            primes.append(numbers[i])
    print(primes)
def zadanie3():
    numbers=loaddata("pierwsze.txt")
    w=[]
    for number in numbers:
        s=sum(number)
        while s>9:
            s=sum(s)
        if s==1:
            w.append(number)
    print(w)
zadanie3()