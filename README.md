# Auto Push Miui Update Email
Designed by [NightstarSakura](https://github.com/NightstarSakura)  
[中文食用请看这里](https://github.com/NightstarSakura/Auto_MIUI_Update_Email/blob/main/README_CN.md)

# How to use it?
Stp.1 Fork this repositories  
Stp.2 Add your Email Address to *.github/workflows/GetUpdate.yml*  
Stp.3 Remove the *#* in front of the Device Code you need to get the Rom link in *GetUpdate.sh*  
Stp.4 If you need to get the other version's Rom link, please change *region = "cn"* in *GetUpdate.py*  
Stp.5 Go to *Actions* page and press *I understand my workflows, go ahead and enable them*  
Stp.6 It will get the Rom link and send to you every Friday.(UTC Time: 12 PM)

# Notice
It default get China MIUI, it support get any version if your Device have, like global, eea, ru.  
It your device's update is *None*, it's because Xiaomi Official not push the Rom to Server.  

# Thanks
[XiaomiFirmwareUpdater](https://github.com/XiaomiFirmwareUpdater)
