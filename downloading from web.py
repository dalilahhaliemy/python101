import random                     # need functions in both of these files
import urllib.request             # same as from 'urllib import request'


# downloading image from web
def download_web_image(url):
    name = random.randrange(1, 1000)     # store the name of the image in numbers
    full_name = str(name) + ".jpg"       # store in jpeg format as the file name
    urllib.request.urlretrieve(url, full_name,)     # function to download the file and set the full name as the file name


download_web_image("https://images.unsplash.com/photo-1533450718592-29d45635f0a9?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80")

# since we don't specify the path the file would be downloaded in the same path


# downloading file from web

goog_url = "https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1546419121&period2=1577955121&interval=1d&events=history&crumb=/FgzLYE8ORn"

def download_csv_file(csv_url):
    response = urllib.request.urlopen(csv_url)  # open the url
    csv = response.read()                       # read all the data from the url and store in variable csv
    csv_str = str(csv)                          # convert all data to string
    lines = csv_str.split("\\n")                # break the data in lines
    dest_url = r"goog.csv"                      # make new file on our computer
    fx = open(dest_url, "w")                    # write into the file
    for line in lines:                          # printing the lines one by one
        fx.write(line + "\n")
    fx.close()

download_csv_file(goog_url)

