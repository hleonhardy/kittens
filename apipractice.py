from urllib2 import urlopen
from PIL import Image
import os
import uuid

#Asks user for dimensions then shows a kitten photo

#making a unique id for this file name
#It doesn't really matter though because we delete it at the end
filename = "kittens-{}.jpeg".format(uuid.uuid4())

width = raw_input("Enter the width (in pixels): ")
height = raw_input("Enter the height (in pixels): ")

#opens a picture of a kitten with the given dimensions:
url = 'http://placekitten.com/{}/{}'.format(width,height)
kitten = urlopen(url)



#(200 is what it gives you when it works)
if kitten.getcode() != 200:
    quit()

else:
    #If the image doesn't exist then it returns an empty string (weird)
    kitten = kitten.read()
    if len(kitten) == 0:
        print "I'm sorry, no kitten picture exists for these dimensions."
        print "Please try again later. "
        quit()
    else:
        kitten_file = open(filename, "w")
        kitten_file.write(kitten)
        kitten_file.close()

        kittenpic = Image.open(filename)
        kittenpic.show()


#deleting the file because the kittens don't need to be saved on my computer.
os.remove(filename)

