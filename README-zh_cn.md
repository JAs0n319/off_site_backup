# Off_Site_Backup

[Eeglish](./README.md)

## 用前须知
 - QuickBackM 版本 >= 1.7.0
 - 安装 Aligo 库
 - ```pip install Aligo```
 - ```pip install -i https://pypi.tuna.tsinghua.edu.cn aligo```
 - 在网盘内创建相应文件夹
 - 当 UsePort 为 True 时 打开 ```yourip:8080``` 扫描二维码登录
 - 当 UsePort 为 False 时 扫描弹出的二维码
 - 假如服务端在异地记得在出入站策略中开放指定端口

#### [QuickBackM仓库](https://github.com/TISUnion/QuickBackupM)
#### [Aligo仓库](https://github.com/foyoux/aligo)

## config.json

```
{
    "permission_need": 3,           //使用指令的最低权限要求
    "AliPath": "Minecraft_Backup",  //目标目录的文件夹名
    "UsePort": true,                //true = 在网页扫描二维码登录  false = 命令行扫描二维码登录
    "Port": 8080                    //网页端口
}
```
