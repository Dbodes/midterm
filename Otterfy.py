#otterfy
#----------------------------------------------------------------------------------------------------------------------

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
  
def addWords(pic):
  x = getWidth(pic)
  y = getHeight(pic)
  style = makeStyle(serif, bold, 14)
  addTextWithStyle(pic, x-(x/4), y/2, "It's Otter-ific!", style, white)
  repaint(pic)
  return pic

# make the image square
def isSquare(pic):
  width = getWidth(pic)
  height = getHeight(pic)
  if height > width:
    side = width
  else:
    side = height
  newPic = makeEmptyPicture(side, side)
  for x in range(0, side):
    for y in range(0, side):
      newPixel = getPixel(newPic, x, y) 
      xOriginal = width/2-side/2+x
      yOriginal = height/2-side/2+y
      pOriginal = getPixel(pic, xOriginal, yOriginal )
      
      color = getColor(pOriginal)
      setColor(newPixel, color)
      # sort pixels
  repaint(newPic)
  return newPic
#  show(pic)


def pyCopy(source, target, targetX, targetY):
  height = getHeight(source)
  width = getWidth(source)
  heightTarget = getHeight(target)
  widthTarget = getWidth(target)
  for x in range (0, width):
    if (x+targetX<widthTarget):#prevents going over right edge
      for y in range (0,height):
        p = getPixel(source,x,y)
        color = getColor(p)
        if (y+targetY<heightTarget):#prevents going over bottom edge
          setColor(getPixel(target, x+targetX, y+targetY), color)
  return target

def otterCopy(source, target, targetX, targetY):
  height = getHeight(source)
  width = getWidth(source)
  heightTarget = getHeight(target)
  widthTarget = getWidth(target)
  Bcolor = makeColor(76,105,113)
  for x in range (0, width):
    if (x+targetX<widthTarget):#prevents going over right edge
      for y in range (0,height):
        p = getPixel(source,x,y)
        color = getColor(p)
        if (y+targetY<heightTarget and color != Bcolor):#prevents going over bottom edge and filters out background
          setColor(getPixel(target, x+targetX, y+targetY), color)
  repaint(target)
  return target

def shrink(picture):
  height = getHeight(picture)
  width = getWidth(picture)
  newHeight = height/2
  newWidth = width/2
  newPicture = makeEmptyPicture(newWidth,newHeight)
  for x in range (0, newWidth):
    for y in range (0, newHeight):
      p = getPixel(picture,x*2,y*2)
      color = getColor(p)
      setColor(getPixel(newPicture,x,y), color)
  return newPicture

def shrinkOtter(otter,pic):
  otterH=getHeight(otter)
  otterW=getWidth(otter)
  H=getHeight(pic)
  W=getWidth(pic)
  while (otterH*4>H and otterW*4>W):
    otter = shrink(otter)
    otterH=getHeight(otter)
    otterW=getWidth(otter)
  return otter

def makeOtterBorder(otter,pic):
  otter = shrinkOtter(otter,pic)

  otterH=getHeight(otter)
  otterW=getWidth(otter)
  H=getHeight(pic)
  W=getWidth(pic)    
  
  otters = H/otterH
  buffer=(H%otterH)/(otters-1)# the buffer is equal to the left over divided by the number of gaps
  
  for x in range (0,otters):
    pic = otterCopy(otter, pic, x*(buffer+otterH), 0)
  for y in range (1,otters):
    pic = otterCopy(otter, pic, 0, y*(buffer+otterH))
  for x in range (1,otters):
    pic = otterCopy(otter, pic, x*(buffer+otterH), H-otterH)
  for y in range (1,otters-1):
    pic = otterCopy(otter, pic, W-otterW, y*(buffer+otterH))
  repaint(pic)
  
def otterfy():
  otterFile = pickAFile()
  otter = makePicture(otterFile)
  file = pickAFile()
  pic = makePicture(file)
  
  pic = isSquare(pic)
  repaint(pic)
  pic = blueGreen(pic)
  pic = addWords(pic)
  
  makeOtterBorder(otter,pic)
  