def main():
    word = list(input().upper())
    find = {}
    for w in word:
        if not w in find:
            find[w] = 1
        else:
            find[w] += 1

    max_ = [k for k, v in find.items() if max(find.values()) == v]
    if len(max_) > 1:
        print("?")
        exit()
    else:
        max_key = [key for key, value in find.items() if value == find[max_[0]]]
        print(max_key[0])
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
