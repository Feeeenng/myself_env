#!/usr/bin/env bash


echo "----------更新apt-get源----------"
cat << EOF >> /etc/apt/sources.list
deb http://mirrors.aliyun.com/ubuntu/ trusty main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-security main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-proposed main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-backports main restricted universe multiverse
EOF
echo "----------更新apt-get源结束----------"

echo "-----------基础环境软件包安装---------"
apt-get -y update && apt-get -y upgrade && apt-get -y install wget lsof   git  telnet \
libsystemd-journal0 libltdl7 gcc automake autoconf libtool make dos2unix fontconfig xfonts-utils nginx

#vim
#wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | sh
cp /usr/share/vim/vimrc ~/.vimrc
echo "syntax on" >> ~/.vimrc
echo "set nu!" >> ~/.vimrc

#system
echo "vm.max_map_count=262144" >> /etc/sysctl.conf
sysctl -p

echo "export HOST_IP=`ifconfig  eth0 | grep 'inet addr:' | awk -F ':' {'print $2'} |awk {'print $1'}`" >> /etc/profile
#echo "export HOST_DOMAIN=www.baidu.com" >> /etc/profile  #需要单独修改
source /etc/profile

cp /usr/share/zoneinfo/Asia/Shanghai  /etc/localtime
ntpdate time.windows.com

#font
mkdir -p /usr/share/fonts/win

#elasticsearch
mkdir -p /usr/local/elasticsearch/5.x
cp -r es/config/ /usr/local/elasticsearch/5.x/



echo "-----------基础环境配置结束----------"

echo "----------安装docker-ce----------"

dpkg -i other/docker-ce_17.06.0-ce-0-ubuntu_amd64.deb
#source /etc/profile

cat << EOF >> /etc/default/docker
DOCKER_OPTS="--registry-mirror=https://registry.docker-cn.com"
EOF

mkdir -p /etc/docker
touch /etc/docker/daemon.json
cat << EOF >> /etc/docker/daemon.json

EOF



/etc/init.d/docker restart

#docker login -u IP -p 密码
echo "----------安装docker-ce结束----------"


echo "----------安装mongodb----------------"
#安装mongodb
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6
echo "deb [ arch=amd64 ] http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list
apt-get update -y &&  apt-get install -y mongodb-org
sed -i 's/bindIp: 127.0.0.1/bindIp: 0.0.0.0/g' /etc/mongod.conf
sed -i 's/#processManagement:/processManagement:\n fork: true/g'  /etc/mongod.conf
#重启mongodb
pkill mongod
/usr/bin/mongod --config /etc/mongod.conf
echo "----------安装mongodb结束------------"

echo "----------安装redis-server-----------"
#安装redis-server
wget http://download.redis.io/releases/redis-3.2.11.tar.gz
tar xf redis-3.2.11.tar.gz && mv redis-3.2.11 /usr/local && rm -rf redis-3.2.11.tar.gz
cd /usr/local/redis-3.2.11
make -j2 && make install
ln -s /usr/local/redis-3.2.11/src/redis-cli /usr/bin/redis-cli
sed -i 's/bind 127.0.0.1/bind 0.0.0.0/g' redis.conf
sed -i 's/# requirepass foobared/requirepass Aash1234/g' redis.conf  #修改密码
sed -i 's/daemonize no/daemonize yes/g' redis.conf
#启动redis
pkill redis-server |xargs redis-server redis.conf
echo "----------安装redis-derver结束-----------"

echo "----------设置开机自启动-----------------"
#开机自启
sed -i '1s/#!\/bin\/sh -e/#!\/bin\/bash/g' /etc/rc.local
sed -i "13s/^/pkill mongod | xargs mongod --config \/etc\/mongod.conf \n \n /g" /etc/rc.local
sed -i "14s/^/\/usr\/local\/bin\/redis-server \/usr\/local\/redis-3.2.11\/redis.conf \n \n /g" /etc/rc.local
echo "----------设置结束------------------------"

