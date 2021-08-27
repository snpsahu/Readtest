print("Ener first num")
inp1= input()
print("Enter second num")
inp2= input()
try:
    print("end result is" ,
          int(inp1)+int(inp2) )
except Exception as r:
    print(r)

print("Try and except is used for continuty of program")