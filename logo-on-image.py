import os
from PIL import Image

#open folder
os.chdir('images')


# logo
logo = input('Enter Logo Name : ')
logo_img = Image.open(logo)
logo_width , logo_height = logo_img.size

sLogo = logo_img.resize((int(logo_width / 5), int(logo_height / 5)))
sLogoWidth, sLogoHeight = sLogo.size



# output folder
output_folder = input('Enter Folder Name : ')
os.makedirs(output_folder, exist_ok=True)

#loop over each image
for image in os.listdir('.'):
    if image.endswith(('.png','.jpg','.jpeg')):
        im = Image.open(image)
        width , height = im.size

  
        
        im.paste(sLogo,(width-sLogoWidth, height-sLogoHeight),sLogo)
        im.save(f"{output_folder}/{image}")

