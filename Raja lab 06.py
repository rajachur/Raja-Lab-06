import os
fileNameIndex={}
dirIndex={}
textIndex={}
def crawler():
	for dirname, dirnames, filenames in os.walk("F:/naat's/"):  #if i use / it will search my whole computer files .but now i am serching only my One folder on my PC
		# print path to all filenames.
		for filename in filenames:
			#print(filename)
			path=os.path.join(dirname, filename)
			if (os.path.splitext(filename)[1]=='.txt'):
				with open(path,'r') as f:
					for line in f:
						for word in line.split():
							if word not in textIndex:
								textIndex[word]=[]
							if path not in textIndex[word]:
								textIndex[word].append(path)
				
			wordList=os.path.splitext(filename)[0] 	#We'll remove the extension
			wordList=wordList.split(' ')
			for word in wordList:
				if word not in fileNameIndex:
					fileNameIndex[word]=[]
				fileNameIndex[word].append(path)
			#found[path] = os.stat(path).st_size # in bytes
			#os.path.join('root', filename)

		# print path to all subdirectories first.
		for subdirname in dirnames:
			wordList=subdirname.split(' ')
			for word in wordList:
				if word not in dirIndex:
					dirIndex[word]=[]
				dirIndex[word].append(path)
			#subDir.append(os.path.join(dirname, subdirname))
			#print("appending"+ subdirname)

print("Lab 06 spider")
crawler()
print(dirIndex)
inp=1
while(inp!=0):
	inp=raw_input(" Press 1 For Reading Files: ")
	if int(inp)==1:
		word=raw_input("Enter the word you want search: ")
		#temp=temp.lowers

		if word in textIndex:
			temp=textIndex[word]
			print("In readable files: ")
			for path in temp:
				print (path)
		if word in fileNameIndex:
			temp=fileNameIndex[word]
			print("In files names: ")
			for path in temp:
				print (path)
		if word in dirIndex:
			temp=dirIndex[word]
			print("In Directory names: ")
			for path in temp:
				print (path)
			
	elif int(inp)==0:
		exit()
		
