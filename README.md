#go_back_to_sleep

go_back_to_sleep (auto_poweroff) is a simple python utility that sends shutdown signals to computers over a network after a power outage (and subsequent restoration) would turn said computers on.
Intended to be run on a low power master server like a raspberry pi which boots automatically on power restore.

Older motherboards support WOL (wake on LAN) but only after the first power cycle (after an outage - which can be triggered by the boot-up on power restore setting in the BIOS - so is the case for one of my other servers.
This python script sends shutdown signals if the differences in OS uptimes are smaller than X (user adjustable because boot-up times may differ by quite a bit) - if the master and slave servers were powered on at the same time - by a power restore.

Prerequisites:

ssh servers on the remote hosts
constant IP addresses for the remote hosts (Look into the DHCP settings in your router)

sshpass on the shutdown server


To do:

add support for passwordless logins via ssh keys

add installation script 


Notes:

On systemd, the root user will be the one using ssh and the known hosts file is not the same as the regular user's, so make sure you ssh with root to a computer before adding it to the script