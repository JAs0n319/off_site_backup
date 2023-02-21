from mcdreforged.api.all import *
from aligo import Aligo
from threading import Thread
from math import floor
import os
import zipfile
import time

DEFAULT_CONFIG = {
    "permission_need": 3,
    "AliPath": 'Minecraft_Backup',
    "UsePort": False,
    "Port": 8080
}

def compress():
    global out_name
    startdir = './qb_multi/slot1/world'
    out_name = time.strftime("ByPlayer-%Y-%m-%d-%H-%M",time.localtime())+'.zip'
    zip = zipfile.ZipFile(out_name,'w',zipfile.ZIP_DEFLATED)
    for dirpath,dirnames,filenames in os.walk(startdir):
        fpath = dirpath.replace(startdir,'')
        fpath = fpath and fpath + os.sep or ''
        for filename in filenames:
            zip.write(os.path.join(dirpath,filename),fpath+filename)
    zip.close()

def send():
    global ali
    if config['UsePort'] == True:
        ali = Aligo(port=config['Port'])
    else:
        ali = Aligo()
    user = ali.get_user()
    print('当前登录用户: '+user.user_name)
    local_file = './'+out_name
    remote_folder = ali.get_folder_by_path(config['AliPath'])
    ali.upload_file(local_file,parent_file_id=remote_folder.file_id)

def Main_Program():
    global time_taken,state
    time_taken = time.time()
    compress()
    send()
    os.remove('./'+out_name)
    state = False
    time_taken = str(round(time.time() - time_taken,3))

def Check(server:ServerInterface):
    global state
    if os.path.exists('./qb_multi/slot1/world'):
        if state == False:
            server.broadcast('开始上传备份至云盘')
            state = True
            T_Main = Thread(target=Main_Program)
            T_Main.start()
            T_Main.join()
            server.broadcast('备份上传完成, 总用时'+time_taken+'秒')
        else:
            server.broadcast('正在上传中, 请勿重复提交')
    else:
        server.broadcast('未找到有效备份')

def on_load(server:PluginServerInterface, old):
    global config,state
    config = server.load_config_simple('config.json',DEFAULT_CONFIG)
    state = False

    server.register_help_message('!!os_backup','§6!!os_backup §7将QB的最新备份压缩后上传到网盘')

    server.register_command(
        Literal('!!os_backup')
        .requires(lambda src: src.has_permission(config['permission_need']))
        .runs(lambda src: Check(server))
    )