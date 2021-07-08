class Error(Exception):
	"""Base class for other exceptions."""
	pass

class SummationError(Error):
	"""Raised when category weights for a course do not sum to 100."""
	pass

class InvalidGrade(Error):
	"""Raised when grade violates [0,100] range."""
	pass

class Student:


	def __init__(self):
		self.name = ''
		self.course_schedule = ''
		self.course_dictionary = dict()
		self.grade_dictionary = dict()
		self.report_dictionary = dict()
		self.gpa = 0.
		self.filler1 = '---------------------------------------------------'
		self.filler2 = '==================================================='
	

	def create_course_dictionary(self):
		
		course_dictionary = dict()
		inquiry = ''
		
		while inquiry != 'q':
			
			try:
				for course in self.course_schedule:
					course = course.strip()
					course_dictionary[course] = []
					category_weights = input(f'|| {course} || Enter category:weight pairs: ')
					course_dictionary[course] = [cat_wg.split(':') for cat_wg in category_weights.split(',')]
				
				for value in course_dictionary.values():
					
					cat_sum = 0
					
					for cat_wt in value:

						cat_wt[0] = cat_wt[0].strip().title()
						cat_wt[1] = float(cat_wt[1].strip())
						
						cat_sum += cat_wt[1]
					if cat_sum != 100:
						raise SummationError
			
			except SummationError:
				print(self.filler1);print('## ERROR ## Weights do not sum to 100. Would you like to repeat? (y/n/q)');print(self.filler1)
				inquiry = input('> ')
			
			else:
				print(self.filler1);print('## SUCCESS ## Entered course information correctly.');print(self.filler1)
				inquiry = 'q'
			
		self.course_dictionary = course_dictionary


	def calculate_course_grade(self):
		
		grade_dictionary = {}
		inquiry = ''

		while inquiry != 'q':
			
			try:
				
				for course, category_weights in zip(self.course_dictionary.keys(), self.course_dictionary.values()):
					
					grade_dictionary[course] = 0
					
					for cat_wt in category_weights:
						points_total = float(input(f'|| {course} || << {cat_wt[0]} >> Enter points total: '))
						points_achvd = float(input(f'|| {course} || << {cat_wt[0]} >> Enter points achvd: '))
						current_grade = points_achvd / points_total
						grade_dictionary[course] += current_grade * cat_wt[1]
					
					if (grade_dictionary[course] > 100) | (grade_dictionary[course] < 0):
						raise InvalidGrade
			
			except InvalidGrade:
				print(self.filler1);print(f'## ERROR ## Grade outside possible range. Would you like to repeat? (y/n/q)');print(self.filler1)
				inquiry = input('> ')
			
			else:
				print(self.filler1);print('## SUCCESS ## Grades copmuted correctly.');print(self.filler1)
				inquiry = 'q'

		self.grade_dictionary = grade_dictionary


	def course_grade_letter(self):

		report_dictionary = {}

		for course in self.grade_dictionary:
			if float(self.grade_dictionary[course]) >= 97:
				report_dictionary[course] = ["A+", 4.00]
			if float(self.grade_dictionary[course]) >= 93 and float(self.grade_dictionary[course]) < 97:
				report_dictionary[course] = ["A", 4.00]
			if float(self.grade_dictionary[course]) >= 90 and float(self.grade_dictionary[course]) < 93:
				report_dictionary[course] = ["A-", 3.67]
			if float(self.grade_dictionary[course]) >= 87 and float(self.grade_dictionary[course]) < 90:
				report_dictionary[course] = ["B+", 3.33]
			if float(self.grade_dictionary[course]) >= 83 and float(self.grade_dictionary[course]) < 87:
				report_dictionary[course] = ["B", 3.00]
			if float(self.grade_dictionary[course]) >= 80 and float(self.grade_dictionary[course]) < 83:
				report_dictionary[course] = ["B-", 2.67]
			if float(self.grade_dictionary[course]) >= 77 and float(self.grade_dictionary[course]) < 80:
				report_dictionary[course] = ["C+", 2.33]
			if float(self.grade_dictionary[course]) >= 73 and float(self.grade_dictionary[course]) < 77:
				report_dictionary[course] = ["C", 2.00]
			if float(self.grade_dictionary[course]) >= 70 and float(self.grade_dictionary[course]) < 73:
				report_dictionary[course] = ["C-", 1.67]
			if float(self.grade_dictionary[course]) >= 67 and float(self.grade_dictionary[course]) < 70:
				report_dictionary[course] = ["D+", 1.33]
			if float(self.grade_dictionary[course]) >= 63 and float(self.grade_dictionary[course]) < 67:
				report_dictionary[course] = ["D", 1.00]
			if float(self.grade_dictionary[course]) >= 60 and float(self.grade_dictionary[course]) < 63:
				report_dictionary[course] = ["D-", 0.67]
			if float(self.grade_dictionary[course]) < 60:
				report_dictionary[course] = ["F", 0.00]
		
		self.report_dictionary = report_dictionary


	def point_gpa_conversion(self):

		for course, grade_numeric in zip(self.report_dictionary.keys(), self.report_dictionary.values()):

			credit_hours = float(input(f'|| {course} || Enter credit hours: '))
			self.report_dictionary[course].append(credit_hours)
			self.report_dictionary[course].append(grade_numeric[1] * credit_hours)

		print(self.filler1);print('## SUCCESS ## Point conversion completed.');print(self.filler1)


	def build_report(self):
		
		semester_credit_hours = 0
		semester_credit_point = 0

		for course, grade_details in zip(self.report_dictionary.keys(), self.report_dictionary.values()):
			semester_credit_hours += grade_details[2]
			semester_credit_point += grade_details[3]

		self.gpa = semester_credit_point / semester_credit_hours


		print(self.filler2 + '============')
		print('SEMESTER REPORT: {:>46}'.format(self.name.title()))
		print(self.filler2 + '============')
		
		column_headers = ["Course", "Final Grade", "Grade Point", "Credit Hours", "Credit Points"]
		print("{:<10} {:<12} {:<12} {:<12} {:<12}".format(*column_headers))
		print(self.filler1 + '------------')
		
		for course, grade_details in zip(self.report_dictionary.keys(), self.report_dictionary.values()):
			print("{:<10} {:>12} {:>12.2f} {:>12.2f} {:>12.2f}".format(course, grade_details[0], grade_details[1], grade_details[2], grade_details[3]))
		print(self.filler1 + '------------')
		print("{:52}GPA : {:.2f}".format('', self.gpa)); print(self.filler1 + '------------')


if __name__ == '__main__':
	student = Student()
	student.name = input("Enter name:\n> ").title()
	student.course_schedule = input("Enter course schedule, comma separated, no spaces:\n> ").split(',')
	student.create_course_dictionary()
	student.calculate_course_grade()
	student.course_grade_letter()
	student.point_gpa_conversion()
	student.build_report()