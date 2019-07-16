# Sockets_Listener
A server Side Socket Listener



## Server Socket Listener for Login Packet 
 
### Make a Server Socket then read a login packet define below:
- Login packet is the information packet connecting the terminal and platform. It can send terminal information to the platform. 
- 	If a GPRS connection is established successfully, the terminal will send a first login message packet to the server and, within five seconds, if the terminal receives a data packet responded by the server, the connection is considered to be a normal connection; if not, the terminal will send login packet again. 
- If no packet returned by the server within 5 seconds, then the response of the login packet is a timeout. 
-	Terminal reboot automatically after 3 timeouts.

Example：78 78 11 01 07 52 53 36 78 90 02 42 70 00 32 01 00 05 12 79 0D 0A
And Login packet response like this 
Example：78 78 05 01 00 05 9F F8 0D 0A
Reference link:  https://www.sparkfun.com/tutorials/403  
 

![sockets](https://user-images.githubusercontent.com/31818185/61246696-15c4be80-a76d-11e9-960b-a29e186526ae.png)

## How to run
``` python
>> python server.py
```
> Log on to https://localhost:3000/login

### Dependencies
To install all the dependencies do the following step:
1. Create venv using virtualenv
``` cmd 
virtualenv [env_name]
```
Activate the env by 
``` cmd
cd [env_name]/scripts
```
And activate env using
```cmd
activate
```

2. use the requirement.txt provided and use the following command.
``` python
>> pip install -r requirement.txt
```


