def pad_number(number, length=6, fillchar='0'):
  return str(number).zfill(length)

# Example usage
randomNumber = 12223
padded_number = pad_number(randomNumber)
print(padded_number)  # Output: 000123