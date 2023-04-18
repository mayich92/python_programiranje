
def is_prime_num(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def main():
    print(is_prime_num(8))
    print(is_prime_num(13))


if __name__ == '__main__':
    main()