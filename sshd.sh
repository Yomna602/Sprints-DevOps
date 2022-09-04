#!/bin/bash

echo "Your Default SSH Port Number is 22, "
echo "Enter another Number in between the Range 1024-32767 to change it  "

read SSH_PortNo

if [[ "$SSH_PortNo" -ge 1024 && "$SSH_PortNo" -le 32767  ]];
then
        sed -i -e "/Port /c\Port $SSH_PortNo" /etc/ssh/sshd_config
        echo "Your SSH Port Number has been Sucessfully changed to $SSH_PortNo"

elif ! [[ "$SSH_PortNo" =~ ^[0-9]+$ ]];
then
    	echo -e "The SSH Port Number must be an Integer Number."
else
        echo -e "The Port Number is not in the Accebtable Range"
fi

sed -i -e "/PermitRootLogin /c\PermitRootLogin no" /etc/ssh/sshd_config
echo "The Root Login has been Disabled to System"

#Adding Sudo Privileges to Multiple Users
while [[ -n $1 ]];
do
    	echo "$1 ALL=(ALL:ALL) ALL" >> /etc/sudoers;
    	shift
done 