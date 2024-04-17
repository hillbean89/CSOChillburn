n = int(input())

list = [int(x) for x in input().split()]
alice = 0
bob = 0

while list:
    alice += max(list)
    list.remove(max(list))
    if list:
        bob += max(list)
        list.remove(max(list))

print (alice, bob)