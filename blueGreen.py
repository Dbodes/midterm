# Possible additions for alteration functions

# make it blue-green
def blueGreen(pic):
  pixels = getPixels(pic)
  for p in pixels:
    blu = getBlue(p)
    re = getRed(p)
    gree = getGreen(p)
    otterColors = makeColor(re*0.4, gree*0.85, blu*0.85)
    setColor(p, otterColors)
  repaint(pic)
  return pic
  
# make the image square
def isSquare(pic):
  width = getWidth(pic)
  height = getHeight(pic)
  height = width
  newPic = makeEmptyPicture(width, height)
  for x in range(0, width):
    for y in range(0, height):
      pixel = getPixel(pic, x, y)
      color = getColor(pixel)
      setColor(pixel, color)
      
  repaint(pic)
#  show(pic)
    