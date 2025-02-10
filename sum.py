import sys  # import sys module to handle command-line arguments

# check if exactly two numbers are passed
if len(sys.argv) != 3:
    print("please provide two numbers")
else:
    try:
        # convert command-line arguments to float
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        
        # calculate the sum
        sum_result = num1 + num2
        
        # print the sum
        print("sum:", sum_result)
    except ValueError:
        print("please provide valid numbers")
