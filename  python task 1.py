class Rectangle:
   def __init__(self,len,wid):
    self.len=len
    self.wid=wid
   def area(self):
      return self.len*self.wid
   def perimeter(self):
      return 2*(self.len+self.wid)

smallRectangle=Rectangle(6,3)
largeRectangle=Rectangle(12,6)	

smallArea=smallRectangle.area()
smallPerimeter=smallRectangle.perimeter()

largeArea=largeRectangle.area()
largePerimeter=largeRectangle.perimeter()

print("Large Rectangle")
print("Area",largeArea)
print("perimeter",largePerimeter)

print("Small Rectangle")
print("Area",smallArea)
print("perimeter",smallPerimeter)