#purpose of script. Grab the output of
from fabric.api import env, run, sudo, hide, settings, output

env.user = ''
env.password = ''
env.hosts = []
list_common =[]

#Prints users who have access to the system
def printusers ():
    output['everything'] = False
    host = sudo("hostname")
    owner = (sudo(str("ls -l /home | awk '{print $3}'")))
    directory = (sudo(str("ls -l /home | awk '{print $9}'")))

    newowner = owner.splitlines()
    newdirectory = directory.splitlines()

    list_common = [host]
    for a, b in zip(newowner, newdirectory):
        if a == b:
            list_common.append(a)
    print list_common



