def bigger(num1, num2):
    reversed_num1 = int(str(num1)[::-1])
    reversed_num2 = int(str(num2)[::-1])
    if reversed_num1 >= reversed_num2:
        return reversed_num1
    else:
        return reversed_num2

def main():
    num1, num2 = input().split(' ')
    print(bigger(num1, num2))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
