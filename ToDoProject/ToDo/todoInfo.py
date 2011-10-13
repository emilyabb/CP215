class todoInfo:
	
	def __init__(self, person, date, file, line, text):
		self.person = person
		self.date = date
		self.file = file
		self.line = line
		self.text = text

	def __str__(self):
		result = self.person + ", "
		result += self.date + ", "
		result += self.file + ", "
		result += self.line + ", "
		result += self.text
		return result
