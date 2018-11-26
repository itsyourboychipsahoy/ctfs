# Notes
# Going to bed since its midnight, i've found the password winter
# And i just need a username to go along with it
# Thinking of parsing the output from find / with a script
# and trying to uncover user files
# more likely its super easy to find a valid username and i'm just retarded
# Oh one more thing, its running vsftp 2.0.1-6 got this from
# cat /etc/vsftpd/vsftpd_conf_migrate.sh
# okay i should really go to bed now

PORT      STATE SERVICE
# Got one flag, and a strange directory with nothing in it.
21/tcp    open  ftp
# ssh 2.0, maybe vulnarable to something?
22/tcp    open  ssh

# found remote command execution in the form at
# http://192.168.254.68/cgi-bin/tracertool.cgi
# and wrote a python script to give me kinda reverse shell
# once i got the virtual path working i explored and found
# http://192.168.254.68/passwords (folder)
# inside was FLAG.txt and passwords.html
# in a comment in passwords.html i found the password "winter"
80/tcp    open  http

# just found a flag on the homepage, prolly exploitable somewhere
9090/tcp  open  zeus-admin

# connected with ncat, got me a flag
13337/tcp open  unknown

# seems to be ssh over another port, don't know anything else though
22222/tcp open  easyengine

# got me a broken reverse shell, and one flag
60000/tcp open  unknown

# Flags
FLAG:{Flip the pickle Morty!}          - 10 Points
FLAG:{TheyFoundMyBackDoorMorty}        - 10 Points
FLAG:{Whoa this is unexpected}         - 10 Points
FLAG:{There is no Zeus, in your face!} - 10 Points
FLAG{Yeah d- just don't do it.}        - 10 Points
