import sys
import shutil
import os

def cleanStudents(root):

	for course in os.walk(root).next()[1]:
		path = root + course + '/1Students/'
		if os.path.isdir(path):
			for student in os.walk(path).next()[1]:
				shutil.rmtree(path + student)

answer = raw_input('This will purge all student data from courses. Are you sure you know what you are doing? (Y/n)')
if answer.lower() != 'y':
	sys.exit()

cleanStudents('./Office/')
cleanStudents('./Programming/')