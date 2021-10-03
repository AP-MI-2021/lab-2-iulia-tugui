'''
Problema 5: Determina daca un nr dat este palindrom
returneaza True daca numarul este palindrom sau False in caz contrar
'''
def is_palindrome(n):
    copie_n = n
    #fac o copie a numarului n pentru a-l putea compara cu inversul sau
    invers_n = 0
    #calculez in variabila "invers_n" inversul numarului n
    while(n>0):
        ultima_cifra = n%10
        invers_n = invers_n*10 + ultima_cifra
        n = n//10
    if copie_n == invers_n:
        return True
    return False
def test_is_palindrome():
    assert is_palindrome(7) is True
    assert is_palindrome(122) is False
    assert is_palindrome(292) is True
    assert is_palindrome(2972) is False
'''
Problema 6: Determină dacă un număr este superprim: dacă toate prefixele sale sunt prime. De exemplu, 233 este superprim, deoarece 2, 23 și 233 sunt toate prime, dar 237 nu este superprim, deoarece 237 nu este prim.
returneaza True daca numarul este superprim sau False in caz contrar
'''
def is_superprime(n):
    if n<2:
        return False
    else:
        while (n>0):
            for i in range (2,n//2+1):
                if n%i==0:
                    return False
            n = n//10
        return True



def main():
    print(is_palindrome(1))
    print(is_superprime(237))

if __name__ == "__main__":
    main()

