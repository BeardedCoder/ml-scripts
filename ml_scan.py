import shutil
import os
import glob

def scan(root):

	for course in os.walk(root).next()[1]:
		path = root + course + '/1Students/'
		if os.path.isdir(path):
			for student in os.walk(path).next()[1]:
				assignments = path + student + '/Assignments'
				for assignment in os.walk(assignments).next()[1]:
					files = os.listdir(assignments + '/' + assignment)

					if len(files) > 1 and len(glob.glob(assignments + '/' + assignment + '/*.pdf')) == 0:

						print course[:8] + ' -> ' + assignment + ' -> ' + student

				midterm = path + student + '/Midterm'
				files = os.listdir(midterm)

				if len(files) > 1 and len(glob.glob(midterm + '/*.pdf')) == 0:
					print course[:8] + ' -> Midterm -> ' + student

				final = path + student + '/Final'
				files = os.listdir(final)

				if len(files) > 1 and len(glob.glob(final + '/*.pdf')) == 0:
					print course[:8] + ' -> Final -> ' + student

print 'Office\n'
scan('./Office/')

print '\nProgramming\n'
scan('./Programming/')