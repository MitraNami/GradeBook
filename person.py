import datetime

class Person():

  def __init__(self, name):
    self.name = name
    self.birthday = None
    self.last_name = name.split(' ')[-1]

  def get_last_name(self):
    return self.last_name

  def __str__(self):
    return self.name

  def set_birthday(self, month, day, year):
    self.birthday = datetime.date(year, month, day)

  def get_age(self):
    if self.birthday is None:
      raise ValueError
    return (datetime.date.today() - self.birthday).days

  def __lt__(self, other):
    if self.last_name == other.last_name:
      return self.name < other.name
    return self.last_name < other.last_name


class MITPerson(Person):
  id = 0

  def __init__(self, name):
    Person.__init__(self, name)
    self.IDNumber = MITPerson.id
    MITPerson.id += 1

  def getIDNumber(self):
    return self.IDNumber

  def __lt__(self, other):
    return self.IDNumber < other.IDNumber

  def speak(self, utterance):
    return self.name + ' says: ' + utterance