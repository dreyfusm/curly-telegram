#purpose of script. Grab the output of
from fabric.api import env, run, sudo, hide, settings, output

env.user = ''
env.password = ''
env.hosts = []
list_common =[]

#Prints users who have access to the system
def printusers():
    output['everything'] = False
    host = sudo("hostname")
    owner = (sudo(str("ls -l /home | awk '{print $3}'")))
    directory = (sudo(str("ls -l /home | awk '{print $9}'")))

#parses users into lists to be compared
    newowner = owner.splitlines()
    newdirectory = directory.splitlines()

#compares the lists. If the owner == the directory name then they are on the list
#logic here is that if the owner is root then they have been revoked from the System
#via puppet (user module will change ownership to root)
    list_common = []
    for a, b in zip(newowner, newdirectory):
        if a == b:
            list_common.append(a)
    print ""
    print "Users with access to " + host
    print ', '.join(list_common)
    print ""
#now check to see who has root access on System
#since we have the users on the system, we will
#grab the users in the wheel group

    sudolist = sudo('cat /etc/group| grep wheel |cut -d: -f4')

    #print "debug after sudo list"
    #print sudolist


    sortlist = []
    for user in list_common:
        if user in sudolist:
            sortlist.append(user)
    print "Here are the current active users with sudo access:"
    print ""
    print ', '.join(sortlist)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"




