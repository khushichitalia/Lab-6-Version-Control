def decoder(passcode):
    result = ''
    for digit in passcode:
        new_digit = str((int(digit) - 3) % 10)
        result += new_digit
    return result

print(decoder("45678888"))