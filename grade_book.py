from student import Student, UG, Grad, TransferStudent


class Grades:
  ''' A mapping from students to a list of grades'''

  def __init__(self):
    '''Create empty grade book'''
    self.students = [] # a list of student objects
    self.grades = {}  # mpas IDNumber -> list of grades
    self.isSorted = True #true if self.students is sorted

  def addStudent(self, student):
    ''' Assumes: student is of type Student
    Add student to the grade book '''
    if not isinstance(student, Student):
      raise TypeError('Must be a Student instance!')

    if student in self.students:
      raise ValueError('Duplicate student')
    self.students.append(student)
    self.grades[student.getIDNumber()] = []
    self.isSorted = False

  def addGrade(self, student, grade):
    ''' Assumes: grade is a float, student is a Student obj
    Add grade to grades list of student
    '''
    try:
      self.grades[student.getIDNumber()].append(grade)
    except KeyError:
      raise ValueError('Student not in the grade book')

  def getGrades(self, student):
    '''Return a list of grades for student '''
    try:
      return (grade for grade in self.grades[student.getIDNumber()]) # a genexpr
    except KeyError:
      raise ValueError('Student not in the grade book')

  def allStudents(self):
    '''Return a list of the students in the grade book '''
    if not self.isSorted:
      self.students.sort()
      self.isSorted = True
    # return (student for student in self.students) # a genexpr
    for student in self.students:
      yield student


def gradeReport(course):
  ''' Assumes: course is of type grades '''
  assert isinstance(course, Grades), 'course must be a grade book!'

  report = []
  print(course.allStudents())
  for student in course.allStudents():
    student_name = str(student)
    grades = course.getGrades(student) # a genexpr
    total = 0.0
    num_grades = 0
    for grade in grades:
      total += grade
      num_grades += 1
    try:
      avg_grades = total / num_grades
    except ZeroDivisionError:
      # student has no grades, num_grades is zero
      msg = '{0}\'s has no grades'.format(student_name)
    else:
      msg = '{0}\'s mean grade is {1}'.format(student_name, avg_grades)
    report.append(msg)
  return '\n'.join(report)


if __name__ == '__main__':
  ug1 = UG('Matt Damon', 2017)
  ug2 = UG('Ben Affleck', 2017)
  ug3 = UG('Lin Manuel Miranda', 2018)
  ug4 = UG('Anna Johnson', 2020)
  g1 = Grad('Bill Gates')
  g2 = Grad('Steve Wozniak')

  six00 = Grades()
  six00.addStudent(g1)
  six00.addStudent(ug2)
  six00.addStudent(ug1)
  six00.addStudent(g2)
  six00.addStudent(ug3)
  six00.addStudent(ug4)


  six00.addGrade(g1, 100)
  six00.addGrade(g2, 25)
  six00.addGrade(ug1, 95)
  six00.addGrade(ug2, 85)
  six00.addGrade(ug3, 75)

  print()
  
  print(gradeReport(six00))

  six00.addGrade(g1, 90)
  six00.addGrade(g2, 45)
  six00.addGrade(ug1, 80)
  six00.addGrade(ug2, 75)

  print()
  print(gradeReport(six00))

