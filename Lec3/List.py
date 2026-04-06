ll=[1,2,3,4,5]

# print(ll)

# print(ll[-1])

# print(len(ll))

# print(ll[2:])

ll.append(10)

print(ll)

print(ll.pop(),ll)
ll.append(3)

ll.append(3)
ll.append(3)
ll.append(3)
print(ll)
# it removes the first occurrence of the element
ll.remove(3)

print(ll)


if -2 in ll:
    print("yes")
else:
    print("no")



ll.insert(1,-2)

print(ll)



