from bs4 import BeautifulSoup
import requests
import os
import re

class Course:
			
	def	__init__(self, courseId = ""):
		self.courseId = courseId

	def get_file_content(self, filename):
		file = open(filename, 'r')
		result = file.read()
		file.close()
		return result

	def save_file_content(self, filename, file_content):
		file = open(filename, 'w')
		file.write(file_content)
		file.close()

	def requestHeaders(self):
		headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
		'Accept-Encoding': 'none',
		'Accept-Language': 'en-US,en;q=0.8',
		'Connection': 'keep-alive'}
		return headers

	def extract_course_detail(self, tag, opt_num = 0):
		cols = tag.find_all("td")
		detail = []
		#exit if the col (td tag) does not have any data
		if len(cols) <= 1:
			return None

		if cols[0] is not None and cols[0].find("a") is not None:
			detail.append(cols[0].find("a")["href"])
			# print("col 1: " + cols[0].find("a")["href"])
		
		# if cols[1].find("p") is not None or cols[1].string is not None:
		# 	detail.append(cols[1].find("p").string)
		# 	# print("col 2: " + cols[1].find("p").string)
		
		if cols[1] is not None and cols[1].get_text() is not None:
			detail.append(cols[1].get_text().strip())
			# print("col 2: " + cols[1].find("p").string)

		# if cols[2].find("span") is not None:
		# 	detail.append(cols[2].find("span").string)
		# 	# print("col 3: " + cols[2].find("span").string)	
		
		if cols[2] is not None and cols[2].get_text() is not None:
			detail.append(cols[2].get_text().strip())
			# print("col 3: " + cols[2].find("span").s

		if len(detail) > 0:
			detail.append(opt_num)

		return detail

	@staticmethod
	def run():
		stream1 = []
		stream2 = []
		course = Course()		
		# url = "https://www.douglascollege.ca/programs-courses/catalogue/programs/PBDCIS"
		# result = requests.get(url, headers=course.requestHeaders())		
		current_path = os.path.dirname(os.path.realpath(__file__))		
		# course.save_file_content(current_path + "/data.txt", result.text)
		result = course.get_file_content(current_path + "/data.txt")
		soup = BeautifulSoup(result, "html.parser")
		course_table = soup.find(id='curriculum').find("table")
		year1 = "Year I Coursework" 
		year2 = "Year II Coursework"
		sel_option = "Select one of the following 2 options:"
		require_courses = "Required courses" 
		total_year1 = "Total Year I Credits"
		year2_op1 = "Option 1 - Emerging Technology Stream"
		year2_op2 = "Option 2 - Data Analytics Stream" 
		mini_stream = "Choose one of the following mini-streams" 
		mini1 = "Business" 
		mini2 = "CSIS " 
		mini3 = "Marketing"
		total_year2 = "Total Year II Credits"

		course_year = 1
		course_type = 1
		course_opt = 1
		mini_opt = 1
		index = 0
		row_tags = course_table.find_all("tr")

		#step to "Year I Coursework" - "Select one of the following 2 options:""
		while (index < len(row_tags) and not re.search(sel_option, str(row_tags[index]))):
			index += 1				

		index += 1

		# #step to the second "Select one of the following 2 options:", this is option 1 of year 1
		while (index < len(row_tags) and not re.search(sel_option, str(row_tags[index]))):
			stream1.append(course.extract_course_detail(row_tags[index], 1))			
			stream2.append(course.extract_course_detail(row_tags[index], 1))						
			index += 1
		
		index += 1		

		#option 2 of year 1
		while (index < len(row_tags) and not re.search(require_courses, str(row_tags[index]))):
			stream1.append(course.extract_course_detail(row_tags[index], 2))			
			stream2.append(course.extract_course_detail(row_tags[index], 2))						
			index += 1

		index += 1

		#required courses of year 1, this will end at "Total Year I Credits"
		while (index < len(row_tags) and not re.search(total_year1, str(row_tags[index]))):
			stream1.append(course.extract_course_detail(row_tags[index], 0))			
			stream2.append(course.extract_course_detail(row_tags[index], 0))						
			index += 1

		#move to year 2, stream 1, option 1
		while (index < len(row_tags) and not re.search(sel_option, str(row_tags[index]))):
			index += 1				

		index += 1

		#append 2 option of year 2, stream 1
		while (index < len(row_tags) and not re.search(require_courses, str(row_tags[index]))):			
			stream1.append(course.extract_course_detail(row_tags[index], 1))
			index += 1

		index += 1

		#all required courses of year 2, stream 1
		while (index < len(row_tags) and not re.search(year2_op2, str(row_tags[index]))):			
			stream1.append(course.extract_course_detail(row_tags[index], 0))
			index += 1

		#move to 1st option of year 2, stream 2
		while (index < len(row_tags) and not re.search(sel_option, str(row_tags[index]))):						
			index += 1

		index += 1

		#2 options of year 2, stream 2
		while (index < len(row_tags) and not re.search(require_courses, str(row_tags[index]))):			
			stream2.append(course.extract_course_detail(row_tags[index], 1))
			index += 1

		index += 1

		#all required courses of year 2, stream 2
		while (index < len(row_tags) and not re.search(mini_stream, str(row_tags[index]))):			
			stream2.append(course.extract_course_detail(row_tags[index], 0))
			index += 1

		index += 1

		#skip to 1st mini stream
		while (index < len(row_tags) and not re.search(mini1, str(row_tags[index]))):						
			index += 1

		# 1st mini stream - Business
		while (index < len(row_tags) and not re.search(mini2, str(row_tags[index]))):			
			stream2.append(course.extract_course_detail(row_tags[index], 11))
			index += 1

		index += 1

		# 2nd mini stream - CSIS
		while (index < len(row_tags) and not re.search(mini2, str(row_tags[index]))):			
			stream2.append(course.extract_course_detail(row_tags[index], 11))
			index += 1

		index += 1
		
		# 2nd mini stream - CSIS
		while (index < len(row_tags) and not re.search(mini3, str(row_tags[index]))):			
			stream2.append(course.extract_course_detail(row_tags[index], 12))
			index += 1

		index += 1

		# 2nd mini stream - CSIS
		while (index < len(row_tags) and not re.search(total_year2, str(row_tags[index]))):			
			stream2.append(course.extract_course_detail(row_tags[index], 13))
			index += 1

		
