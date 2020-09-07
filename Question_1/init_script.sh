#!/bin/bash

#Infinite loop to check if the server is ready
while true
do
 /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P p@ssw0rd -Q "EXEC sp_databases;"
if [ $? -eq 0 ]
    then
        echo "Server is ready"
        break
    else
        echo "Server is not ready yet continuing the loop..."
        sleep 1
    fi
done

#loop to run sql script in ascending order from folder dbscripts
for i in `ls ./dbscripts | sort`;
do
    # Run the files from command line
    /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P p@ssw0rd -d master -i /dbscripts/$i
    #wc -l "./dbscripts/$i"
    if [ $? -eq 0 ]
    then
        echo "$i completed"
    else 
        echo "$i failed"
        sleep 1
    fi
    #echo $i;
done;
