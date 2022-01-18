
# import block
import time
import os

# global variables
remote_uptime_file = ["/home/","/autopoweroff/uptime"]

# for now user changeable
local_copy_remote_uptime_file = "/home/boo/auto_poweroff/aux_file"

hosts = ["foo@192.168.0.2", "goo@192.168.0.16"]
# for now passwords are recorded in plain text
# not required if logging in with certificate, but for now, not supported
passwords = ["passWd1", "admin24"]

# auxiliary functions
def get_uptime():
	with open('/proc/uptime', 'r') as f:
		uptime_seconds = float(f.readline().split()[0])
	return uptime_seconds

def get_uptime_from_copy():
	with open(local_copy_remote_uptime_file, 'r') as f:
		uptime_seconds = float(f.readline().split()[0])
	return uptime_seconds

def get_remote_uptime_file(remote_host, remote_pass):
    # cant copy directly from /proc/uptime from remote to local
    os.system("sshpass -p " + remote_pass + " ssh " + remote_host + ' "sshpass -p '+ remote_pass +' sudo cp /proc/uptime '+ remote_uptime_file[0] + remote_host.split('@')[0] + remote_uptime_file[1] +' "')
    time.sleep(3)
    os.system("sshpass -p " + remote_pass + " scp " + remote_host + ":"+ remote_uptime_file[0] + remote_host.split('@')[0] + remote_uptime_file[1] +" "+ local_copy_remote_uptime_file)

def send_remote_shutdown_signal(remote_host, remote_pass):
	os.system("sshpass -p " + remote_pass + " ssh " + remote_host + ' "sshpass -p '+ remote_pass +' sudo poweroff"')

def if_uptime_difference_s_lower_than_poweroff(secs, remote_hosts, remote_passs):
    #allow for all the targeted systems to boot up
    time.sleep(secs)

    #get own local uptime
    local_uptime = get_uptime()
	
    for i in range(0, len(remote_hosts)):
        get_remote_uptime_file(remote_hosts[i], remote_passs[i])
        remote_uptime = get_uptime_from_copy()
        
        if abs( local_uptime - remote_uptime ) < secs :
            #send_remote_shutdown_signal(remote_host, remote_pass)
            send_remote_shutdown_signal(remote_host, remote_pass)


