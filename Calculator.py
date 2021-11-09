while True:
    print("\n ----------------------------------- \n")

    input1 = input("Enter a 1st no or type STOP to stop the calculator:")
    #Now checking if user type stop or not
    if input1 in ("STOP" ,"Stop" ,"stop"):
        break
    elif not input1.isdigit():
        print("Only accept int values.")
        continue # This will go back to loop and continue
    else:
        number1 = int(input1)


    op = input("Enter Operation to perform:")


    input2 = input("Enter a 2nd no or type STOP to stop the calculator:")
    # Now checking if user type stop or not
    if input2 in ("STOP" ,"Stop" ,"stop"):
        break
    elif not input2.isdigit():
        print("Only accept int values.")
        continue  # This will go back to loop and continue
    else:
        number2 = int(input2)

    if op == "+" :
        output= int(input1) + int(input2)
        print(output)

    elif op == "-":
        output = int(input1) - int(input2)
        print(output)

    elif op == "*":
        output = int(input1) * int(input2)
        print(output)

    elif op == "/":
        output = int(input1) / int(input2)
        print(output)

    elif op == "%":
        output = int(input1) % int(input2)
        print(output)

    else:
        print("Please enter valid operation: ")
        continue

    print( int(input1), op , int(input2), "=", output)