#!/bin/bash


#POST Text 1
echo -e "\n\n\n\nBecky sending text \"Orange Juice\" to API\n"
sleep 2
#Printing echo of command so user informed
echo -e curl -i -H \"Content-Type: application/json\" -X POST -d '{"text":"Orange Juice", "timeout":170}' http://:****/chat/Becky/meh
sleep 1.5
echo -e "\n"
sleep .8
#Sending curl request to API
curl -i -H "Content-Type: application/json" -X POST -d '{"text":"Orange Juice", "timeout":170}' http://:****/chat/Becky/meh
#Sleep
sleep 2



#POST Text 2
echo -e "\n\n\n\nHershel sending text \"Red\" to API\n"
sleep 2
#Printing echo of command so user informed
echo curl -i -H "Content-Type: application/json" -X POST -d '{"text":"Red"}' http://:****/chat/Hershel/whatever
sleep 1.5
echo -e "\n"
sleep .8
#Sending curl request to API
curl -i -H "Content-Type: application/json" -X POST -d '{"text":"Red"}' http://:****/chat/Hershel/whatever
#Sleep
sleep 2



#POST Text 3
echo -e "\n\n\n\nErwin sending text \"Green\" to API\n"
sleep 2
#Printing echo of command so user informed
echo curl -i -H "Content-Type: application/json" -X POST -d '{"text":"Green", "timeout":170}' http://:****/chat/Erwin/blah
sleep 1.5
echo -e "\n"
sleep .8
#Sending curl request to API
curl -i -H "Content-Type: application/json" -X POST -d '{"text":"Green", "timeout":170}' http://:****/chat/Erwin/blah
#Sleep
sleep 2



#Post Text 4
echo -e "\n\n\n\nBecky sending text \"Diamond\" to API\n"
sleep 2
#Printing echo of command so user informed
echo curl -i -H "Content-Type: application/json" -X POST -d '{"text":"Diamond", "timeout":100}' http://:****/chat/Becky/meadow
sleep 1.5
echo -e "\n"
sleep .8
#Sending curl request to API
curl -i -H "Content-Type: application/json" -X POST -d '{"text":"Diamond", "timeout":100}' http://:****/chat/Becky/meadow
#Sleep
sleep 2



#Post Text 5
echo -e "\n\n\n\nBecky sending text \"Blue Ridge\" to API\n"
sleep 2
#Printing echo of command so user informed
echo curl -i -H "Content-Type: application/json" -X POST -d '{"text":"Blue Ridge", "timeout":40}' http://:****/chat/Becky/number
sleep 1.5
echo -e "\n"
sleep .8
#Sending curl request to API
curl -i -H "Content-Type: application/json" -X POST -d '{"text":"Blue Ridge", "timeout":40}' http://:****/chat/Becky/number
#Sleep
sleep 2



#Post Text 6
echo -e "\n\n\n\nBecky sending text \"Yellow\" to API\n"
sleep 2
#Printing echo of command so user informed
echo curl -i -H "Content-Type: application/json" -X POST -d '{"text":"Yellow"}' http://:****/chat/Becky/blah
sleep 1.5
echo -e "\n"
sleep .8
#Sending curl request to API
curl -i -H "Content-Type: application/json" -X POST -d '{"text":"Yellow"}' http://:****/chat/Becky/blah
#Sleep
sleep 2



#Post Text 7
echo -e "\n\n\n\nHershel sending text \"Purple Haze\" to API\n"
sleep 2
echo curl -i -H "Content-Type: application/json" -X POST -d '{"text":"Purple haze", "timeout":170}' http://:****/chat/Hershel/play
sleep 1.5
echo -e "\n"
sleep .8
curl -i -H "Content-Type: application/json" -X POST -d '{"text":"Purple haze", "timeout":170}' http://:****/chat/Hershel/play