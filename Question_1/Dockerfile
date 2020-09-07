# Get the mssql server linux image
FROM mcr.microsoft.com/mssql/server:2019-latest  
# Change user to root to copy script and change the permissiom
USER root
COPY dbscripts dbscripts
COPY init_script.sh /
COPY entrypoint.sh /
# Make init script executable
RUN chmod +x /init_script.sh

# Change to original mssql 
USER mssql
# Run the custom entrypoint
ENTRYPOINT /bin/bash ./entrypoint.sh
