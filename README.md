# Off_Site_Backup

[中文](./README-zh_cn.md)

## Before Use
 - QuickBackM Verssion >= 1.7.0
 - Install Aligo
 - ```pip install Aligo```
 - ```pip install -i https://pypi.tuna.tsinghua.edu.cn aligo```
 - Creat the Folder in Aliyun
 - When UsePort = True scane the QR Code on ```yourip:8080``` for login
 - When UsePort = False Scane the QR Code on Console
 - Remember open the port when you login

#### [QuickBackM](https://github.com/TISUnion/QuickBackupM)
#### [Aligo](https://github.com/foyoux/aligo)

## config.json

```
{
    "permission_need": 3,           //As u see
    "AliPath": "Minecraft_Backup",  //Folder Name in Aliyun CREAT IT ON ALIYUN!!!
    "UsePort": true,                //true = scane the code on website  false = scane the code on console
    "Port": 8080                    //Port of website
}
```
