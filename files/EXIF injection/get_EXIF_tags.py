import piexif
from PIL import Image
from PIL.ExifTags import TAGS

'''
This script reads EXIF tags from the file specified

USAGE:
1. Select the correct file name
2. Run this script
3. See output

'''

# path to the image
imagename = "out.jpg"

image = Image.open(imagename)
exifdata = image.getexif()
for tag_id in exifdata:
    tag = TAGS.get(tag_id, tag_id)
    data = exifdata.get(tag_id)
    if isinstance(data, bytes):
        data = data.decode()
    print(f"{tag_id} -- {tag:25}: {data}")



