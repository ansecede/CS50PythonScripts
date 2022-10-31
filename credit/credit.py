# Task description: https://cs50.harvard.edu/x/2022/psets/6/credit/


from cs50 import get_string
# TODO


cc_number = get_string("Number: ").strip()
cc_length = len(cc_number)
checkSum = 0
cc_start = int(cc_number[:2])


for i in range(cc_length):
    # The card is read from right to left, thats why th char taken is: cc_length - i - 1
    current_digit = int(cc_number[cc_length - i - 1])
    # If statement to calculate the checksum. Every two iterations the current digit gets multiplied by 2
    # and the ones that not are directly added to the checksum
    if (i % 2 != 0):
        # In case the current digit is grater than 4, the result is a two-digit number,
        # which must be added together. So, since the first digit is always 1, we add it.
        # Then just take the second one and add it directly to the checksum
        if current_digit > 4:
            current_digit *= 2
            current_digit = current_digit % 10
            checkSum += 1 + current_digit
        else:
            checkSum += current_digit * 2
    else:
        checkSum += current_digit


# Checks if checksum meets the condition
if (checkSum % 10 == 0):
    # Create an if chain because the card can only be one type or Invalid
    # MASTERCARD (uses 16-digit numbers, they start with 51, 52, 53, 54, or 55)
    if (cc_length == 16) and (cc_start >= 51 and cc_start <= 55):
        print("MASTERCARD")
    # AMEX (uses 15-digit numbers, they start with 34 or 37)
    elif (cc_length == 15) and (cc_start == 34 or cc_start == 37):
        print("AMEX")
    # VISA (uses 13- and 16-digit numbers. they start with 4.)
    elif (cc_length == 13 or cc_length == 16) and (cc_start >= 40 and cc_start <= 49):
        print("VISA")
    else:
        print("INVALID")
else:
    print("INVALID")