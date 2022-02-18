# 自动推送MIUI每周更新
Designed by [NightstarSakura](https://github.com/NightstarSakura)  
[English Version](https://github.com/NightstarSakura/Auto_MIUI_Update_Email/blob/main/README.md)

# 使用方法
Stp.1 Fork 本仓库.
Stp.2 在 *.github/workflows/GetUpdate.yml* 里修改你的邮箱地址.  
Stp.3 删除 *GetUpdate.sh* 中你所需要获取的机型前的 *#*  
Stp.4 如果你不需要国内版的MIUI, 请更改 *GetUpdate.py* 内的 *region = "cn"* 中的 *cn*.  
Stp.5 前往 *Actions* 页面并点击 *I understand my workflows, go ahead and enable them*.  
Stp.6 本项目将在每周五晚推送更新到邮箱, 后续或将支持每日推送.(北京时间: 晚上8点)

# 注意事项
本项目默认获取中国版 MIUI, 如果您的设备存在其他版本, 本项目也支持获取, 例如: global、eea、ru等  
如果您的设备没有更新, 我们将会标明 *未更新* 或 *未推送*(一般存在于新发布的设备)

# 特别鸣谢
[XiaomiFirmwareUpdater](https://github.com/XiaomiFirmwareUpdater)
