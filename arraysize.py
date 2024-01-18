

def pad_number(number, length=6, fillchar='0'):
  return str(number).zfill(length)


for i in range(1,200):
    print("frame_"+pad_number(i)+'.jpg')