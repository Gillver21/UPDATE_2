#!/bin/bash
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y dist-upgrade
sudo apt-get -y install python2.7
sudo apt-get -y install python-pip
sudo pip install Flask


#User read -p to allow user to input data into variable
###sudo read -p "Please enter the port number within the range you opened in AWS Security Group Console:" port_aws
read -p "Please enter the port number within the range you opened in AWS Security Group Console:" port_aws



#Set the value user entered into environment variable for the prompt AWS_PROT
AWS_PORT=$port_aws



#Find file with an extension of ".py" and replace a specified string with the port number user entered
sudo find ../.. -name "*.py" -exec sed -i "s/port=\*\*\*\*/port=$AWS_PORT/g" {} + > /dev/null 2>&1
find ../.. -name "*.py" -exec sed -i "s/port=\*\*\*\*/port=$AWS_PORT/g" {} + > /dev/null 2>&1
###sudo find ../.. -name "*.py" -exec sed -i "s/port=\*\*\*\*/port=\[PORT_OPENED_IN_SECURITY_GROUP\]/g" {} + > /dev/null 2>&1
###find ../.. -name "*.py" -exec sed -i "s/port=\*\*\*\*/port=\[PORT_OPENED_IN_SECURITY_GROUP\]/g" {} + > /dev/null 2>&1



#Run test_harness
cd ../../tests/src
python test_harness.py