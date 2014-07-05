# Usage: zip("Office\COMP1073 - Windows 7", "packages")

import os
import zipfile
import sys
import os
import comtypes.client

def zip(src, dst):

	code = src[src.find("\\") + 1:src.find("\\") + 9]

	scheduleFilename = "Schedule" + code +".pdf"
	assignmentsFilename = "Assignments" + code + ".pdf"
	assignmentsPath = os.path.join(src, "Assignments", assignmentsFilename);
	assignmentFilesPath = os.path.join(src, "Assignments", "AssignmentFiles" + code)

	dst = os.path.join(dst, code);

	zf = zipfile.ZipFile("%s.zip" % (dst), "w")

	zf.write(os.path.join(src, scheduleFilename), scheduleFilename)

	if not (os.path.exists(assignmentsPath)):
		docToPdf(assignmentsPath[:-4])

	zf.write(assignmentsPath, assignmentsFilename)

	for root, dirs, files in os.walk(assignmentFilesPath):
		for file in files:
			if root == assignmentFilesPath:
				dstPath = os.path.join("AssignmentFiles", file)
			else:
				dstPath = os.path.join("AssignmentFiles", root[root.rfind("\\") + 1:], file)
			zf.write(os.path.join(root, file), dstPath)

	zf.close()

def docToPdf(fileName):
	wdFormatPDF = 17

	in_file = os.getcwd() + "\\" + fileName + ".docx"
	out_file = os.getcwd() + "\\" + fileName + ".pdf"

	word = comtypes.client.CreateObject('Word.Application')
	doc = word.Documents.Open(in_file)
	doc.SaveAs(out_file, FileFormat=wdFormatPDF)
	doc.Close()
	word.Quit()


if len(sys.argv) < 3:
	print "Proper usage: mlpack.py <source> <destination>"
	sys.exit()

source = sys.argv[1]
dest = sys.argv[2]

for course in os.walk(source).next()[1]:
	zip(os.path.join(source, course), dest)