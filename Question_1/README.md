# MSSQL docker setup
## how to use this repository?

#### step1: git clone
```
git clone https://github.com/mangesh2211/VisualBI
cd VisualBI/Question_1

root@mangesh-VirtualBox:~/VisualBI/Question_1# ls -lrt
total 20
-rw-r--r-- 1 root root  721 Sep  6 21:33 init_script.sh
-rw-r--r-- 1 root root  180 Sep  6 21:33 entrypoint.sh
-rw-r--r-- 1 root root  390 Sep  6 21:33 Dockerfile
-rw-r--r-- 1 root root  301 Sep  6 21:33 docker-compose.yml
drwxr-xr-x 2 root root 4096 Sep  6 21:33 dbscripts
```
#### step2: Build Image and run the container using docker-compose
```
root@mangesh-VirtualBox:~/VisualBI/Question_1# docker-compose up -d
Creating network "question1_default" with the default driver
Building mssql
Step 1/8 : FROM mcr.microsoft.com/mssql/server:2019-latest
2019-latest: Pulling from mssql/server
```

#### step 3: check the output
- First we can check if the container is running or not
```
root@mangesh-VirtualBox:~/VisualBI/Question_1# docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
b8f22e5a766e        question1_mssql     "/bin/sh -c '/bin/ba…"   3 minutes ago       Up 3 minutes        0.0.0.0:1433->1433/tcp   mssql-dev
```
- take the conatiner ID from the above output and login to mssql shell
In this case the password is p@ssw0rd which has been configured in docker-composoe file.
```
```
root@mangesh-VirtualBox:~/VisualBI/Question_1# docker exec -it b8f22e5a766e /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P p@ssw0rd
1> USE testDB;
2> GO
Changed database context to 'testDB'.
1> SELECT * FROM Test;
2> GO
Id          Data                                              
----------- --------------------------------------------------
          1 A                                                 

(1 rows affected)
1> 

Sqlcmd: Warning: The last operation was terminated because the user pressed CTRL+C.
```

