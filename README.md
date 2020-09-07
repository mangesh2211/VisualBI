# MSSQL Docker Implementation
## How to use this repository?

#### Prerequisite
- docker engine up and running
- docker-compose cli installed

#### Step1: Git clone
```
root@mangesh-VirtualBox:~# git clone https://github.com/mangesh2211/VisualBI
Cloning into 'VisualBI'...

root@mangesh-VirtualBox:~# cd VisualBI/
root@mangesh-VirtualBox:~/VisualBI# ls -lrt
total 24
-rw-r--r-- 1 root root   30 Sep  4 23:27 README.md
-rw-r--r-- 1 root root  721 Sep  4 23:27 init_script.sh
-rw-r--r-- 1 root root  180 Sep  4 23:27 entrypoint.sh
-rw-r--r-- 1 root root  390 Sep  4 23:27 Dockerfile
-rw-r--r-- 1 root root  301 Sep  4 23:27 docker-compose.yml
drwxr-xr-x 2 root root 4096 Sep  4 23:27 dbscripts

```

#### Step2: Build Image and run container using docker-compose
```
root@mangesh-VirtualBox:~/VisualBI# docker-compose up -d

Creating mssql-dev ... done
``` 

#### Step3: Check the output
- To check the output, first, check if the container is running and whether port 1433 is mapped to 1433
```
root@mangesh-VirtualBox:~/VisualBI# docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED              STATUS              PORTS                    NAMES
770983d6881d        visualbi_mssql      "/bin/sh -c '/bin/ba…"   About a minute ago   Up About a minute   0.0.0.0:1433->1433/tcp   mssql-dev

```
- Grab the container id from above output and login to mssql shell
In this case the password is p@ssw0rd which is configured in docker-compose file.

```
$root@mangesh-VirtualBox:~/VisualBI# docker exec -it 770983d6881d /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P p@ssw0rd
1> USE testDB;
2> GO
Changed database context to 'testDB'.
1> SELECT * FROM Test;
2> GO;
3> GO
Msg 102, Level 15, State 1, Server mssql-dev, Line 2
Incorrect syntax near 'GO'.
1> SELECT * FROM Test;
2> GO
Id          Data                                              
----------- --------------------------------------------------
          1 A                                                 

```

