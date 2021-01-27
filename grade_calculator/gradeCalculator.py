import math

class Student:

	def __init__(self, name, course_schedule):
		self.name = name
		self.course_schedule = course_schedule

	def course_calc(self):
		course_total = {}

		for course in self.course_schedule:
			course_points = 0
			course_categories = input("Enter grading categories for {0}'x,y,z': \n".format(course))
			c_c_list = course_categories.split(",")
			for category in c_c_list:
				category_weight = float(input("Enter category weight for {0}'float': \n".format(category)))
				category_total = float(input("How many points possible for {0}'float': \n".format(category)))
				category_achieved = float(input("How many points achieved for {0}'float': \n".format(category)))
				course_points += (category_achieved / category_total) * (category_weight / 100)
			course_total[course] = round(course_points, 4) * 100

	#def course_gpa(self):
		course_grade = {}

		for course in course_total:
			if float(course_total[course]) >= 97:
				course_grade[course] = "A+"
			if float(course_total[course]) >= 93 and float(course_total[course]) < 97:
				course_grade[course] = "A"
			if float(course_total[course]) >= 90 and float(course_total[course]) < 93:
				course_grade[course] = "A-"
			if float(course_total[course]) >= 87 and float(course_total[course]) < 90:
				course_grade[course] = "B+"
			if float(course_total[course]) >= 83 and float(course_total[course]) < 87:
				course_grade[course] = "B"
			if float(course_total[course]) >= 80 and float(course_total[course]) < 83:
				course_grade[course] = "B-"
			if float(course_total[course]) >= 77 and float(course_total[course]) < 80:
				course_grade[course] = "C+"
			if float(course_total[course]) >= 73 and float(course_total[course]) < 77:
				course_grade[course] = "C"
			if float(course_total[course]) >= 70 and float(course_total[course]) < 73:
				course_grade[course] = "C-"
			if float(course_total[course]) >= 67 and float(course_total[course]) < 70:
				course_grade[course] = "D+"
			if float(course_total[course]) >= 63 and float(course_total[course]) < 67:
				course_grade[course] = "D"
			if float(course_total[course]) >= 60 and float(course_total[course]) < 63:
				course_grade[course] = "D-"
			if float(course_total[course]) < 60:
				course_grade[course] = "F"


	#def gpa_calc(self):
		total_points = 0
		total_ch = 0
		course_ch = {}

		for course in self.course_schedule:
			total_points += course_total[course]
			course_credit_hour = float(input("Enter credit hours for {0} 'float': ".format(course)))
			total_ch += course_credit_hour
			course_ch[course] = course_credit_hour

		gpa = total_points / total_ch

	#def build_report(self):
		report = []
		for course in self.course_schedule:
			course_report = [course, course_ch[course], course_total[course], course_grade[course]]
			report.append(course_report)
		#report.append(["TOTAL", (sum(course) for course in course_ch), (sum(course) for course in course_total), "yo mama"])


	#def print_report(self):
		print("--------------------------------------------------")
		print('{0} achieved the following GPA this semester: {1:.2f}'.format(self.name, gpa))
		print("--------------------------------------------------")
		column_headers = ["Course", "Credit Hours", "Points", "Grade"]
		print("{:<10} {:<15} {:<5} {:<5}".format(*column_headers))
		print("--------------------------------------------------")
		for course in report:
			print("{:<10} {:<15} {:<5} {:<5}".format(*course))



Lucas_fa18 = Student('Lucas_fa18', ['ECON 103', 'MATH 221', 'ASTR 122', 'FR 103', 'LAS 101'])
Lucas_fa18.course_calc()
Lucas_sp19 = Student('Lucas_sp19', ['ECON 198', 'MATH 231', 'FR 104', 'STAT 200', 'NPRE 101'])
Lucas_sp19.course_calc()
Lucas_fa19 = Student('Lucas_fa19', ['ECON 203', 'ECON 302', 'MATH 415', 'CS 105', 'ECON 199', 'KIN 104'])
Lucas_fa19.course_calc()
Lucas_sp20 = Student('Lucas_sp20', ['ECON 303', 'ECON 402', 'STAT 400', 'HIST 142', 'SOC 160'])
Lucas_sp20.course_calc()
Lucas_fa20 = Student('Lucas_fa20', ['MATH 213', 'ECON 437', 'ECON 440', 'STAT 385', 'STAT 410', 'STAT 425'])
Lucas_fa20.course_calc()
Lucas_sp21 = Student('Lucas_sp21', ['ECON 474', 'ECON 490', 'STAT 426', 'STAT 430', 'MATH 347', 'CS 199'])
Lucas_sp21.course_calc()
