def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)):
        min_num = phone_book[i]
        split_list = [k[:len(min_num)] for k in phone_book[i:]]
        if split_list.count(min_num) > 1:
            answer = False
            break
    return answer
