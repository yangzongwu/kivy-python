step1:  
pip3:  
sudo apt-get install python3-pip  

step2:   
https://kivy.org/doc/stable/installation/installation-linux.html  


step3:  
https://buildozer.readthedocs.io/en/latest/installation.html  


step4:  
buildozer init  
buildozer -v android debug  
buildozer android debug deploy run  



issue:  
1:aidl not found please install it  
sudo apt-get update  
sudo apt-get install build-essential  
sudo apt-get install libstdc++6  
sudo apt-get install aidl   
sudo apt-get update  


2.no module named _ctypes  
sudo apt install libffi-dev  
buildozer -v android clean  
buildozer -v android debug  




