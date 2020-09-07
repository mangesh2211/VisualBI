 #Start the init script first and then run the sqlservr command from original entrypoint.sh 
 #so that it will continue to run as daemom
 /init_script.sh & /opt/mssql/bin/sqlservr
