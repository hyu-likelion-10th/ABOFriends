'''
a=int(input())

for x in range(a):
    globals()['b'+str(x)]=list[x]
'''


'''    
a=int(input())
arr=list(map(int,input().split()))
arr.sort()

print(arr[0],arr[len(arr)-1])
'''
a=int(input())
arr=list(map(int,input().split()))
print(min(arr),max(arr))
