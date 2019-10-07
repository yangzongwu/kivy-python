# step1:  pip3:  
``` 
sudo apt-get install python3-pip  
``` 

# step2: kivy Installation on Linux  
https://kivy.org/doc/stable/installation/installation-linux.html  
``` 
$ python -m pip install --upgrade --user pip setuptools virtualenv  
``` 
Then make and load the virtualenv. This is optional, but highly recommended:  
``` 
$ python -m virtualenv ~/kivy_venv  
$ source ~/kivy_venv/bin/activate  
``` 
Finally install the Kivy wheel and optionally the kivy-examples:  
``` 
$ python -m pip install kivy  
$ python -m pip install kivy_examples  
``` 

Gstreamer is not included, so if you would like to use media playback with kivy, you should install ffpyplayer like so  
``` 
$ python -m pip install ffpyplayer  
```   
Make sure to set KIVY_VIDEO=ffpyplayer env variable before running the app. Only Python 3.5+ is supported.  


Add one of the PPAs as you prefer  
stable builds:	  
``` $ sudo add-apt-repository ppa:kivy-team/kivy``` 
nightly builds:	  
``` $ sudo add-apt-repository ppa:kivy-team/kivy-daily``` 
Update your package list using your package manager  
``` $ sudo apt-get update``` 

### Install Kivy  

Python2 - python-kivy:  
``` 
 	$ sudo apt-get install python-kivy
``` 
Python3 - python3-kivy:
``` 
 	$ sudo apt-get install python3-kivy
``` 
optionally the gallery of Examples - kivy-examples:
``` 
 	$ sudo apt-get install kivy-examples
```

# step3:  buildozer
https://buildozer.readthedocs.io/en/latest/installation.html  
### Installation  
``` 
pip3 install --user --upgrade buildozer  
``` 
### Targeting Android  
Android on Ubuntu 18.04 (64bit)  
``` 
sudo apt update  
sudo apt install -y git zip unzip openjdk-8-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake   
pip3 install --user --upgrade cython virtualenv  # the --user should be removed if you do this in a venv   

# add the following line at the end of your ~/.bashrc file  
export PATH=$PATH:~/.local/bin/  
``` 

# step4:
``` 
buildozer init  
buildozer -v android debug  
buildozer android debug deploy run  
``` 


# issue:  
### aidl not found please install it  
``` 
sudo apt-get update  
sudo apt-get install build-essential  
sudo apt-get install libstdc++6  
sudo apt-get install aidl   
sudo apt-get update  
``` 

### no module named _ctypes  
``` 
sudo apt install libffi-dev  
buildozer -v android clean  
buildozer -v android debug  
``` 



