#!/bin/sh

# iptables init

sudo iptables -P INPUT ACCEPT

#sudo iptables -F

echo "IPTABLES INIT SUCCESS"



BLOCK_LIST_FILE=./GeoIPCountryWhois.csv

echo "BLOCK LIST FILE = $BLOCK_LIST_FILE"



# ADD BLOCK TARGET LIST

ALLOW_TARGET_COUNTRY="Korea"



# REGIST BLOCK IP FOR LOOP

for IP_BANDWIDTH in `egrep -v $ALLOW_TARGET_COUNTRY $BLOCK_LIST_FILE | awk -F, '{print $1, $2}' | awk -F\" '{print $2"-"$4}'`



do

echo "STARTING!!"

sudo iptables -I INPUT -p all -m iprange --src-range $IP_BANDWIDTH -j DROP

done



sudo iptables -L
