#!/bin/bash


#User read -p to allows user to input data into variable
###sudo read -p "Please enter the IP Address of the Remote Server: " ip_aws
read -p "Please enter the IP Address of the Remote Server: " ip_aws
###sudo read -p "Please enter the port number within the range you opened in AWS Security Group Console ( e.g. 5000 ): " open_port_aws
read -p "Please enter the port number within the range you opened in AWS Security Group Console ( e.g. 5000 ): " open_port_aws



#Set the value user entered into environment variable for the prompt AWS_PORT
IP_PORT_AWS=$ip_aws:$open_port_aws


#Find .sh files from downloaded Git repository and replace denoted string with IP of REMOTE Server
#NOTE: Redirects Output of sudo related command to dev/null to account for OSs like Windows which do no have sudo commands
sudo find .. -type f -exec sed -i "s/:\*\*\*\*/$IP_PORT_AWS/g" {} + > /dev/null 2>&1
find .. -type f -exec sed -i "s/:\*\*\*\*/$IP_PORT_AWS/g" {} +
sudo find .. -name "*.sh" -exec chmod a+x {} + > /dev/null 2>&1
find .. -name "*.sh" -exec chmod a+x {} +


#Run Test Case
cd ../RUN_TEST_CASES/dynamic/
./dynamic.sh