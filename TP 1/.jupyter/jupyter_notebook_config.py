import os

file_path="/opt/app-root/src/dav_passwd"
if not os.path.exists(file_path) and os.environ.get('JUPYTER_WEBDAV_PASSWORD'):
    f=open(file_path,"w")
    f.write(os.environ.get('JUPYTER_WEBDAV_PASSWORD','no_password_set'))
    f.close()