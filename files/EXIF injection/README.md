make_own_EXIF_injection.py script creates black image (out.jpg) in which you can enter your own arbitary EXIF data

USAGE (Edit the script):
1. Enter wanted payload to "payload"
2. If you want to edit only one EXIF field:
	a. Comment out Single start and Single end
	b. Enter your wanted EXIF tag key
2. If you want to edit all of the fields from the "exifs" array:
	a. Comment out Multi start and Multi end
3. Run this script
4. Run "get_EXIF_tags.py" to verify that you have the EXIF fields filled.
