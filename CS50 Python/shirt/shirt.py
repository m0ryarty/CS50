import sys
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit('Too few command-line argumwents')
if len(sys.argv) > 3:
    sys.exit('Too many command-line argumwents')

ext1 = sys.argv[1].split('.')[1]
ext2 = sys.argv[2].split('.')[1]

if (ext1 != ext2):
    sys.exit('Input and output have different extensions')


if (ext2 == 'png') or (ext2 == 'jpg') or (ext2 == 'jpeg'):
    pass
else:
    sys.exit('Invalid output')
try:
    if ext1 == 'png' or ext1 == 'jpg' or ext1 == 'jpeg':

        with Image.open(sys.argv[1]) as image:
            image = ImageOps.fit(image, (600, 600))
            shirt = Image.open("shirt.png")
            image.paste(shirt, shirt)

            image.save(f'{sys.argv[2]}')

    else:
        sys.exit('Invalid input')
except FileNotFoundError:
    sys.exit('File not found')
