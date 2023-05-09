class Triangle:
  def __init__(self, sideOne, sideTwo, sideThree):
    self.sideOne = sideOne
    self.sideTwo = sideTwo
    self.sideThree = sideThree

    self.showAllSides()
    self.showTriangleType()
  
  def showAllSides(self):
    print('Side one: ' + str(self.sideOne))
    print('Side two: ' + str(self.sideTwo))
    print('Side three: ' + str(self.sideThree))

  def showTriangleType(self):
    A = self.sideOne
    B = self.sideTwo
    C = self.sideThree

    if(not ((A < B + C) and (B < A + C) and (C < A + B))):
      print('Is not a triangle')
      return

    if(A == B == C):
      print('Equilateral')
    elif((A == B) and (A == C) or (C == B)):
      print('Isosceles')
    else:
      print('Scalene')
    
    print(10*'-')

firstTriangle = Triangle(10, 20, 20)
secondTriangle = Triangle(20, 20, 20)
thridTriangle = Triangle(3, 4, 5)
fourthTriangle = Triangle(50, 8, 5)