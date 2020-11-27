# Gunicorn service

## Install debian dependences
```bash
sudo su;
apt update -y;
apt install -y python3 python3-pip;
```
## Install python libraries
```bash
sudo su;
pip3 install -r requirements.txt;
gunicorn --workers=3 --timeout=30 --bind "0.0.0.0:5000" main:app;
```
## enable service
```bash
sudo su;
mkdir /opt/myapp;
cp * /opt/myapp/;
cp gunicorn.service /etc/systemd/system/;

systemctl start gunicorn;
systemctl enable gunicorn;
systemctl daemon-reload
```
