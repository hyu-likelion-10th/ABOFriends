s = input().upper()
freq = [0 for x in range(26)]
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(len(alphabet)):
    for j in range(len(s)):
        if s[j] == alphabet[i]:
            freq[i] += 1
n = max(freq)
cnt = 0
for f in freq:
    if f == n:
        cnt += 1
if cnt == 1:
    print(alphabet[freq.index(max(freq))])
else:
    print('?')
