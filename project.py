from flask import Flask,render_template,request
import os
import subprocess as sb
import sys
app=Flask(__name__)

@app.route('/')
def index():
	return render_template("file1.html")

@app.route('/profile1/' , methods=['post','get'])
def profile1():
	option=request.form["option"]
	if option == "java":
		code=request.form["ta"]
		inpt=request.form["input"]
		os.system("docker rm -f $(docker ps -aq)")
		os.system("docker container run -dit --name code3 compileros:1")
		out=open("/mydockerproject/main.java","w+")
		os.system("chmod 777 main.java")
		out.write(code)
		out.close()
		obj=open("/mydockerproject/input.txt","w+")
		os.system("chmod 777 input.txt")
		obj.write(inpt)
		obj.close()
		os.system("docker cp /mydockerproject/main.java code3:/")
		os.system("docker cp /mydockerproject/input.txt code3:/")
		os.system("docker container exec code3 javac main.java")
		os.system("docker exec code3 sh -c 'java main < input.txt' > output.txt")
		#os.system("docker exec code3 cat main.java >> output.txt ")
		#os.system("docker cp code1:abc.txt/ /mydockerproject/")
		f=open("output.txt","r")
		lines=f.readlines()
		strng=""
		for line in lines:
			strng=strng+line+"<br>"
		#os.system("docker exec code3 cal > abc.txt")
		
		#return out.stdout.decode()
		return strng
	elif option == "c":
		code=request.form["ta"]
		os.system("docker rm -f $(docker ps -aq)")
		os.system("docker container run -dit --name code1 compileros:1")
		out=open("/mydockerproject/main.c","w+")
		os.system("chmod 777 /mydockerproject/main.c")
		out.write(code)
		out.close()
		os.system("docker cp /mydockerproject/main.c code1:/")
		os.system("docker container exec code1 gcc main.c -o main")
		os.system("docker container exec code1 ./main > output.txt")
		f=open("output.txt")
		lines=f.readlines()
		strng=""
		for line in lines:
			strng=strng+line+"<br>"
	else:
		code=request.form["ta"]
		os.system("docker rm -f $(docker ps -aq)")
		os.system("docker container run -dit --name code1 compileros:1")
		out=open("/mydockerproject/main.py","w+")
		os.system("chmod 777 /mydockerproject/main.py")
		out.write(code)
		out.close()
		os.system("docker cp /mydockerproject/main.py code1:/")
		os.system("docker container exec code1 python main.py > output.txt")
		f=open("output.txt")
		lines=f.readlines()
		strng=""
		for line in lines:
			strng=strng+line+"<br>"

if __name__=="__main__":
	app.run(debug=True)

	 
