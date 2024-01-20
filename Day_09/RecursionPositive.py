# Write a recursive function to find the sum of digits of a positive integer
def sumdigits(number):
  if number==0:
    return 0
  if number!=0:
    return (number%10) + (number//10)
def main():
    number=int(input("Enter a number :"))
    print(sumdigits(number))
main()
