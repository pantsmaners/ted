from PIL import Image
#Read the two images
def pad_number(number, length=6, fillchar='0'):
  return str(number).zfill(length)


for i in range(1,100):
    print(i)
    pad_number(i)
    image1 = Image.open("frame_"+pad_number(i)+'.jpg')
    image2 = Image.open('merge'+str(i)+'.jpg')
    #resize, first image
    image1_size = image1.size
    image2_size = image2.size
    new_image = Image.new('RGB',(2*image1_size[0], image1_size[1]), (250,250,250))
    new_image.paste(image1,(0,0))
    new_image.paste(image2,(image1_size[0],0))
    new_image.save("merge"+str(i+1)+".jpg","JPEG")