'''
1.How do you distinguish between shutil.copy() and shutil.copytree()?
Ans. shutil.copy() will copy a single file,
    while shutil.copytree() will copy an entire folder and every folder and file contained in it.

2.What function is used to rename files?
Ans.  os.rename() method

3.What is the difference between the delete functions in the send2trash and shutil modules?
Ans.shutil functions will permanently delete files and folders.
and send2trash functions will move a file or folder to the recycle bin.

4.ZipFile objects have a close() method just like File objects’ close() method. What ZipFile method is
equivalent to File objects’ open() method?
Ans.yes, it is. the zipfile. ZipFile() function is equivalent to the open() function;
 the first argument is the filename,
 and the second argument is the mode to open the ZIP file in (read, write, or append).

5.Create a programme that searches a folder tree for files with a certain file extension (such as .pdf
or .jpg). Copy these files from whatever location they are in to a new folder.
Ans.

'''
#Ans1
import os, shutil


target = 'C:\\New folder'
report = open('new_file1.txt','w')

for root,dirnames,files in os.walk(target):
	for x in files:
		if x.endswith('.txt'):
			report.write(root + "\\" + x + "\n")

report.close()

#Ans2
import os,
import shutil

def copyfilesbyex (targetfolder, extensions, vFolder):
	targetfolder = os.path.abspath(targetfolder)
	vFolder = os.path.abspath(vFolder)
	print('Looking in', folder, 'for files with extensions of', ', '.join(extensions))
	for foldername, subfolders, filenames in os.walk(folder):
		for filename in filenames:
			name, extension = os.path.splitext(filename)
			if extension in extensions:
				fileAbsPath = foldername + os.path.sep + filename
				print('Coping', targetfolder, 'to', vFolder)
				shutil.copy(targetfolder, vFolder)

extensions = ['.txt', '.pdf']
folder = 'Folder'
destFolder = 'targetFolder'
copyfilesbyex (targetfolder, extensions, vFolder)