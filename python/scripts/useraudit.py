# Mike Dreyfus
#purpose of script. Grab the output of /etc/home, print users who are still active
# and of those active users, print who has sudo access
from fabric.api import env, run, sudo, hide, settings, output
import csv

env.user = ''
env.password = ''
env.hosts = []

#declaring global variables
#one for the csvlist that we will export
#turn keeps track of how many times we've looped through
csvlist = []
turn = 0
hostnum = len(env.hosts)
title1 = ["Users below currently have access to the system"]
title2 = ["Users below currently have access to the system"]

#Prints users who have access to the system
def printusers():
    global turn
    global csvlist
    global hostnum
    global title1
    global title2
    output['everything'] = False
    host = [sudo("hostname").upper()]
    owner = (sudo(str("ls -l /home | awk '{print $3}'")))
    directory = (sudo(str("ls -l /home | awk '{print $9}'")))

#parses users into lists to be compared
    newowner = owner.splitlines()
    newdirectory = directory.splitlines()

#compares the lists. If the owner == the directory name then they are on the list
#logic here is that if the owner is root then they have been revoked from the System
#via puppet (user module will change ownership to root)
    list_common = []
    for name1, name2 in zip(newowner, newdirectory):
        if name1 == name2:
            list_common.append(name1)
    print ""
    print "Users with access to " + host[0]
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

    #Lastly, add the hostname, user list, and sudo list to the master CSV list
    csvlist.append(host)
    csvlist.append(title1)
    csvlist.append(list_common)
    csvlist.append(title2)
    csvlist.append(sortlist)

    turn += 1
    print turn
    #ones the number of turns is equal to the length of hosts in the list we will create the CSV
    if turn == hostnum:
        print "Exporting all to CSV"
        res = csvlist
        csvfile = "useradit.csv"
        with open(csvfile, "w") as writeout:
            writer = csv.writer(writeout, lineterminator='\n')
            writer.writerows(res)



