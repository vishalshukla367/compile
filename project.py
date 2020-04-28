from flask import Flask,render_template,request
import os
import subprocess as sb
import sys
app=Flask(__name__)

@app.route('/')
def index():
	
	return render_template("file1.html",message='')

def removedocker():
	os.system("docker rm -f $(docker ps -aq)")

def launchdocker():
	os.system("docker container run -dit --name code3 compileros:1")

def permission(filename):
	strng="chmod 777 "+filename
	os.system(strng)

def writeintofile(filename,writethis):
	abspath="/mydockerproject/"+filename
	out=open(abspath,"w+")
	out.write(writethis)
	out.close()

def copyfiletodocker(filename):	
	strng="docker cp /mydockerproject/"+filename+" code3:/"
	os.system(strng)

@app.route('/profile1/' , methods=['post','get'])
def profile1():
	option=request.form["option"]
	if option == "java":
		code=request.form["code"]
		inpt=request.form["testcase"]
		removedocker()
		launchdocker()	
		writeintofile("main.java",code)
		writeintofile("input.txt",inpt)
		permission("main.java")		
		permission("input.txt")	
		copyfiletodocker("main.java")
		copyfiletodocker("input.txt")
		os.system("docker container exec code3 javac main.java 2> compilerror.txt")
		error=open("compilerror.txt","r")
		err=error.read()
		if err is not '':
			f=open("compilerror.txt","r")
			lines=f.readlines()
			strng=""
			for line in lines:
				strng=strng+line+"\n"
			return render_template('file1.html',message=strng,code=code,inpt=inpt)
		os.system("docker exec code3 sh -c 'java main < input.txt' > output.txt")
		f=open("output.txt","r")
		lines=f.readlines()
		strng=""
		for line in lines:
			strng=strng+line+"\n"
		return render_template('file1.html',message=strng,code=code,inpt=inpt)
	elif option == "c":
		code=request.form["code"]
		inpt=request.form["testcase"]
		removedocker()
		launchdocker()
		writeintofile("main.c",code)
		permission("main.c")
		writeintofile("input.txt",inpt)
		permission("input.txt")
		copyfiletodocker("main.c")
		copyfiletodocker("input.txt")
		os.system("docker container exec code3 gcc main.c -o main")
		error=open("compilerror.txt","r")
		err=error.read()
		if err is not '':
			f=open("compilerror.txt","r")
			lines=f.readlines()
			strng=""
			for line in lines:
				strng=strng+line+"\n"
			return render_template('file1.html',message=strng,code=code,inpt=inpt)
		os.system("docker container exec code3 sh -c './main < input.txt' > output.txt")
		f=open("output.txt","r")
		lines=f.readlines()
		strng=""
		for line in lines:
			strng=strng+line+"\n"
		return render_template('file1.html',message=strng,code=code,inpt=inpt)
	else:
		code=request.form["code"]
		inpt=request.form["testcase"]
		removedocker()
		launchdocker()
		writeintofile("main.py",code)
		permission("main.py")
		writeintofile("input.txt",inpt)
		permission("input.txt")
		copyfiletodocker("main.py")
		copyfiletodocker("input.txt")
		os.system("docker exec code3 python main.py 2>compilerror.txt")
		error=open("compilerror.txt","r")
		err=error.read()
		if err is not '':
			f=open("compilerror.txt","r")
			lines=f.readlines()
			strng=""
			for line in lines:
				strng=strng+line+"\n"
			return render_template('file1.html',message=strng,code=code,inpt=inpt)
		os.system("docker exec code3 sh -c 'python main.py < input.txt' > output.txt")
		f=open("output.txt","r")
		lines=f.readlines()
		strng=""
		for line in lines:
			strng=strng+line+"\n"
		return render_template('file1.html',message=strng,code=code,inpt=inpt)

if __name__=="__main__":
	app.run(debug=True)

	 
