how to run the code ?
you need to install python2.7 from here https://www.python.org/downloads/,
you need also to install scrapy framwork, installation guide is here https://doc.scrapy.org/en/latest/intro/install.html
then open a terminal, navigate to the project root directory, run this command (scrapy crwal danube -o outputfile.csv)
after the spider is done, you will need to convert the output csv file to xls sheet and fix the encoding problem as follow:
-open new blank excel sheet 
-choose data tab then press 'from text' button
-select the csv file
-choose delimited and unicode (UTF-8) then next
-select coma then next then finish then ok


output format:

1-output_data.xls format:
name_arabic
description
weight
name_english
price
barcode
image_urls: a list of images src urls
url: the url of the item details page
images: this field will have 3 information about each image downloaded (url, path, checksum)

2-images/full folder contains about 9300 images.
