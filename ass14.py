'''
1.What does RGBA stand for?
Ans.An RGBA color value is an extension of RGB with an Alpha channel (opacity).

2.From the Pillow module, how do you get the RGBA value of any images?
Ans.
pip instal Pillow
from PIL import Image
img = Image.open(‘image.png’)
rgba = img.convert(“RGBA”)
datas = rgba.getdata()

3.What is a box tuple, and how does it work?
Ans.The crop() method on Image objects takes a box tuple,
and returns an Image object representing the cropped image.

4.Use your image and load in notebook then, How can you find out the width and height of an
Image object?
Ans.
# import required module
from PIL import Image

# get image
filepath = "image.png"
img = Image.open(filepath)

# get width and height
width = img.width
height = img.height

# display width and height
print("The height of the image is: ", height)
print("The width of the image is: ", width)

5.What method would you call to get Image object for a 100×100 image, excluding the lower-left
quarter of it?
Ans.
from PIL import Image

img = Image.open(r'C:\Users\Admin\Desktop\a.jpg')
img_info = img.size
print(img_info)
#img_s = img.show()
img_crop = img.crop((265,265,555,555))
img_crp = img_crop.show()

6.After making changes to an Image object, how could you save it as an image file?
Ans.
image_crop.save('data/dst/astronaut_pillow_crop.jpg', quality=95)

7.What module contains Pillow’s shape-drawing code?
Ans.The 'ImageDraw' module.

8. Image objects do not have drawing methods. What kind of object does? How do you get this kind
of object?
Ans.

'''

