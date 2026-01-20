#The show interfaces brief command listing 

switch(config)# show interfaces brief 

Theshowinterfacesconfigcommandlisting switch(config)# showinterfaces config

Core-Switch-1# config
Core-Switch-1(config)# interface 1/A1
Core-Switch-1(eth-1/A1)# name Web-Server
Core-Switch-1(eth-1/A1)# exit
Core-Switch-1(config)# write memory

switch(config)# show interfaces brief

switch(config)# showrunning-config

switch# show logging