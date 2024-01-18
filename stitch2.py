import sys
from PIL import Image
import glob


import glob
from PIL import Image

filename_base = "frame_"  # Base part of the filename
count = 1
for i in range(1,4):
    start_index = i*50
    end_index = start_index+50
    filename_pattern = filename_base + "%06d.jpg"  # Combine base with index and extension

    images = []
    for i in range( start_index, end_index+ 1):
        filename = filename_pattern % i  # Generate filename string
        images.append(Image.open(filename))  # Open the image using the string filename



    #print(start_index, end_index)
    widths, heights = zip(*(i.size for i in images))

    total_width = sum(widths)
    max_height = max(heights)

    new_im = Image.new('RGB', (total_width, max_height))

    x_offset = 0
    for im in images:
        new_im.paste(im, (x_offset,0))
        x_offset += im.size[0]

    new_im.save("tedt" + str(count)+'.jpg')
    count +=1
    print(count)