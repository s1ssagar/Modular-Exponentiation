def modexp_lr(a, b, n):
    r = 1
    for bit in reversed(bits_of_n(b)):
        r = r * r % n
        if bit == 1:
            r = r * a % n
            print r
    print r

def bits_of_n(n):
    bits = []
    while n:
        bits.append(n % 2)
        n /= 2
    print bits
    return bits

def main():
    #to fid 10^10000000 % 7
    a = 100         #base
    b = 10000000    #exponent
    n = 7           #mod
    modexp_lr(a,b,n)

if __name__ == "__main__":
    main()