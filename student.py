from person import MITPerson


class Student(MITPerson):
  pass


class UG(Student):
  def __init__(self, name, classYear):
    super().__init__(name)
    self.year = classYear

  def getClass(self):
    return self.year

  def speak(self, utterance):
    return MITPerson.speak(self, 'Yo Bro, ' + utterance)


class Grad(Student):
  pass


class TransferStudent(Student):
  pass
