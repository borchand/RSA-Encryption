import math as m
import utils

is_square_number = lambda i: round(m.sqrt(i))

def fermat(n):
    """
    The function uses Fermat's factorization method to find the prime factors of a given number.
    
    :param n: The parameter "n" is an integer that we want to factorize into its prime factors using
    Fermat's factorization method
    :return: a tuple of two integers, which are the factors of the input integer 'n' obtained using
    Fermat's factorization method.
    """
    k = is_square_number(n)
    counter = 0
    x = k + counter

    while is_square_number((x**2) - n) ** 2 != (x**2) - n:
        counter += 1
        x = k + counter
                
    s = is_square_number((x**2) - n)
    p = x + s
    q = x - s
        
    return p, q

def find_secret_key(n, e):
    """
    The function finds the secret key given the public keys using the Fermat
    factorization method and a helper function to find the private key.
    
    :param n: Public key
    :param e: Public key
    :return: three values: p, q, and d. These values are obtained by calling the fermat() function to
    find the prime factors of n, calculating k as (p-1)*(q-1), and then using the find_d() function from
    the utils module to find the private key d.
    """

    p, q = fermat(n)

    k = (p - 1) * (q - 1)
    d = utils.find_d(k, e)

    return p, q, d



if __name__ == "__main__":
    e = 7
    n = 43139
    
    p, q, d = find_secret_key(n, e)
    print("p:", p, "q:", q, "d:", d)