### step1:  
pip3:  
``` 
sudo apt-get install python3-pip  
``` 

### step2:   
https://kivy.org/doc/stable/installation/installation-linux.html  


### step3:  
https://buildozer.readthedocs.io/en/latest/installation.html  
###### Installation  
``` 
pip3 install --user --upgrade buildozer  
``` 
###### Targeting Android  
Android on Ubuntu 18.04 (64bit)  
``` 
sudo apt update  
sudo apt install -y git zip unzip openjdk-8-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake   
pip3 install --user --upgrade cython virtualenv  # the --user should be removed if you do this in a venv   

# add the following line at the end of your ~/.bashrc file  
export PATH=$PATH:~/.local/bin/  
``` 

### step4:
``` 
buildozer init  
buildozer -v android debug  
buildozer android debug deploy run  
``` 


### issue:  
###### aidl not found please install it  
``` 
sudo apt-get update  
sudo apt-get install build-essential  
sudo apt-get install libstdc++6  
sudo apt-get install aidl   
sudo apt-get update  
``` 

###### no module named _ctypes  
``` 
sudo apt install libffi-dev  
buildozer -v android clean  
buildozer -v android debug  
``` 



