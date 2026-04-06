
a="harsh"

a=a+"a"

print(a)

for i in a:
    print(i)


# String slicing

s="harshita"

print(s[5:])

print(s[1:5])

print(s[:5])

#repeatition

s1="harshita"

s1=s1*3
print(s1)

str1="   harsh   "

# print(str1.strip())

print(str1.lstrip())
print(str1.rstrip())



s="satyam is a nice person. satyam loves to eat momos. satyam is hardworking person."

s=s.replace("satyam","ritika")
print(s)

l=s.split(".")

print(l)

weight=70
name="harsh"

# s="hello, my name is {} and my weight is {} kg".format(name,weight)

# s="hello, my name is %s and my weight is %d kg" % (name,weight)

s=f"hello, my name is {name} and my weight is {weight} kg"

print(s)