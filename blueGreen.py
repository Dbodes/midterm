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
  
  x = y
  newPic = makeEmptyPicture(x, y)
  for x in range(0, getWidth(pic)):
    for y in range(0, getHeight(pic)):
      setColor(getPixel(pic, x, y), 
    # midterm
