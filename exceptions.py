


def symbol(input1,input2,input3):
    if(input2 == '+'):
        return input1 + input3
    elif(input2 == '-'):
        return input1 - input3
    elif(input2 == '*'):
        return input1 * input3
    elif(input2 == '/'):
        return input1 / input3
    else:
        print("Please input correct operand")



while True:
  try:
      input1 = int(input("Enter First Number: "))
      input2 = input("Enter an operand(+,-,*,/): ")
      input3 = int(input("Enter Second Number: "))
      result = symbol(input1,input2,input3)
      print(result)
      choice = input("Press 'enter' to countinue or 'q' to quit: ")
      if(choice == 'q'):
         break

  except ValueError:
      print("Enter correct number")
