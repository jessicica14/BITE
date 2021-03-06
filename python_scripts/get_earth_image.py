#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Jessica Marshall
#ECE395 Senior Project
#import map image from google maps


from io import BytesIO
from PIL import Image

from urllib import request
import matplotlib.pyplot as plt # this is if you want to plot the map using pyplot
import geocoder

plt.close('all')

#The following list shows the approximate level of detail you can expect to see 
#at each zoom level:

#1: World
#5: Landmass/continent
#10: City
#15: Streets
#20: Buildings

address = '19 Kelly Rd Saugerties NY'
g = geocoder.google(address)

##IF YOU HAVE ADDRESS, COMMENT OUT COORDINATES!
latitude = g.lat
#latitude = 42.127315
longitude = g.lng
#longitude = -73.834235

zoom = 17
#do thing with distance/pixels

#http://wiki.openstreetmap.org/wiki/Slippy_map_tilenames#Resolution_and_Scale
meters_per_pixel = [156412, 78206, 39103, 19551, 9776, 4888, 2444, 1222, 610.984, 305.492, 152.746,  76.373, 38.187, 19.093, 9.547, 4.773, 2.387, 1.193, 0.596, 0.298]
x = meters_per_pixel[zoom]

url = "https://maps.googleapis.com/maps/api/staticmap?center=" + str(latitude) + "," + str(longitude) +"&size=800x800&zoom=" + str(zoom) + "&sensor=false&maptype=satellite"

buffer = BytesIO(request.urlopen(url).read())
image = Image.open(buffer)

# Show Using PIL
#image.show()

# Or using pyplot
plt.imshow(image)
plt.show()

imagename = address + '_zoom' + str(zoom)
imagename = 'POSTERTEST' + '_zoom' + str(zoom)
image.save("/Users/jessicamarshall/Desktop/SeniorProject/map_screenshots/" + imagename + ".png")

###################################################################################

#perform image processing on extracted map
#NEEDS WORK/USE MATLAB STUFF

#from skimage.filters import gabor
#from skimage import io
#from matplotlib import pyplot as plt 
#
## detecting edges in a coin image
#filt_real, filt_imag = gabor(image, frequency=0.75)
#plt.figure()            
#io.imshow(filt_real)
#io.show()
#io.imshow(filt_imag)    
#io.show()   

###################################################################################          

#shortest path algorithm
