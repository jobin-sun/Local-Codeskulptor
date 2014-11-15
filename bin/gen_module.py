import glob
import os
path="..\src"
def fun(path):
	if path != "":
		path = path + os.sep
	for file in glob.glob(path+'*'):
		print file
		if os.path.isdir(file):
			fun(file)
		elif file.endswith('.py'):
			fd = open(file,"r")
			cnt = fd.read()
			fd.close()
			cnt=cnt.replace("\r","")
			cnt=cnt.replace("\n","\\n")
			cnt=cnt.replace("\"","\\\"")
			modName=file.replace("\\","/")
			fdLib.write("myModule[\"src/lib/"+modName+"\"]=\""+cnt+"\";\n")
			
os.chdir(path)

fd = open("codeskulptor.py","r")
cnt = fd.read()
fd.close()
cnt=cnt.replace("\r","")
cnt=cnt.replace("\n","\\n")
cnt=cnt.replace("\"","\\\"")
fdMain = open("../Temp/main.js","w")
fdMain.write("prog=\""+cnt+"\"")
fdMain.close()
fdLib = open("../Temp/skulpt-mylib.js","w")
fdLib.write("myModule={};\n")
fun("")
fdLib.close()