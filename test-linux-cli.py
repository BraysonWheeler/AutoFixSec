import os
x = os.system('./SSH.exp')

'''

expect -exact "\rroot@192.168.1.136's password: "

expect -exact "\rroot@192.168.1.136's password: "
send -- "owaspbwa\r"
expect eof

'''