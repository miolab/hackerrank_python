# Enter your code here. Read input from STDIN. Print output to STDOUT
_ = int(input())
arr = input().split(" ")
print(all(int(i) >= 0 for i in arr) and any(i == i[::-1] for i in arr))