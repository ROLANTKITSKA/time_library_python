#using the time library to calculate the time of execution if a function

from timeit import default_timer as timer


print("This is a simple calculator")

start=timer()
def calculator(x,y,z):
  if (z=="a"):
    print(x+y)
  elif (z=="s"):
    print(x-y)
end=timer()

x=int(input("Type a number: "))
y=int(input("Type a number: "))
z=input("Type a for additon or s for substraction: ")

calculator(x,y,z)
print(end-start) #printing the time the function needed to be executed
