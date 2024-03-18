import os

# docker-compose down with remove-orphans
os.chdir('snmp')
os.system("echo $PWD")
os.system("docker-compose down --remove-orphans")

# remove all realted container images
os.system("docker rmi $(docker images --filter=reference='bhartford419/snmp_container' --filter=reference='snmp*' -q) -f")

os.chdir('..')
# remove directories
os.system("sudo rm -r ./snmp/tcpdump")
os.system("sudo rm -r ./parsed_yaml")
os.system("sudo rm -r ./snmp/data/mocksnmp.snmprec")

# OS specific commands to modify files
if os.name == 'posix':
    if os.uname().sysname == 'Darwin': # macOS
        os.system("sed -E -i '' '37,$d' ./snmp/docker-compose.yaml")
        os.system("sed -E -i '' '2808,$d' ./snmp/data/mocksnmp.snmprec")
    elif os.uname().sysname == 'Linux': # Linux
        os.system("sed -i '37,$d' ./snmp/docker-compose.yaml")
        os.system("sed -i '2808,$d' ./snmp/data/mocksnmp.snmprec")
else:
    print("\nUnable to detect OS...skipping sed substitution\n")
