class Student: 
  def __init__(self, name, gradeOne, gradeTwo):
    self.name = name
    self.gradeOne = gradeOne
    self.gradeTwo = gradeTwo
    self.average = 0.0

  def calc_average(self):
    self.average = (self.gradeOne + self.gradeTwo) / 2
    return self.average

  def show_data(self):
    print('------Student data------')
    print('Name: ', self.name)
    print('Grade one: ', self.gradeOne)
    print('Grade two: ', self.gradeTwo)
    print('Average: ', self.calc_average())
    print(self.result())

  def result(self):
    status = 'Status: '

    if(self.average >= 6.0):
      status += 'Approved'
    else:
      status += 'Disapproved'
    
    return status
  
def createNewStudentAverage():
    studentName = input('Name: ')
    firstGrade = float(input('First grade: '))
    secondGrade = float(input('Second grade: '))

    return Student(studentName, firstGrade, secondGrade)

someStudent = createNewStudentAverage()
someStudent.show_data()
