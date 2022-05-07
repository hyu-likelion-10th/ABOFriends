def main():
    count = int(input())
    for i in range(count):
        sum = 0
        score = input().split(' ')
        number = int(score[0])
        for num in range(1, number+1):
            sum += int(score[num])
        average = sum/number
        student = 0
        for j in range(1, number+1):
            if int(score[j]) > average:
                student+=1
        print("{:.3f}%".format(round(student/number*100, 3)))
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
