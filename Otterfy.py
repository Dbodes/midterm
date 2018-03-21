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
  return target

otterFile = pickAFile()
otter = makePicture(otterFile)
file = pickAFile()
pic = makePicture(file)
pic = otterCopy(Otter, pic, 0, 0)
repaint(pic)