import sys
import os
from PIL import Image

# grab the first and second arg
img_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if new/ exists, if not create
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# loop through Pokedex,
# convert images to png
# save to the new folder
for filename in os.listdir(img_folder):
    img = Image.open(f'{img_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('all done')