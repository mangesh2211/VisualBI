# ETL Pipeline Script
## This script has following command line argument
#### Command line argument options
```

Script to execute etl scripts from a particular directory

positional arguments:
  path                  path of scripts to be executed

optional arguments:
  -h, --help            show this help message and exit
  --order {False,True}, -ord {False,True}
                        Order in which scripts are to be executed. Default:ascending(False)
  --file FILE, -f FILE  The exact file name to run. Default: all files
  --outfile OUTFILE, -o OUTFILE
                        Output file name. Default: console
```
#### output for the script
- there are two ways we can lock the output
1. Print on the console ( default)
2. take a file from the user where he/she wants it to be stored
```
C:\Users\mange\OneDrive\Desktop\Visual BI>python etl_pipline.py C:\Users\mange\OneDrive\Desktop\Scripts\arial
+----------------+-----------------------------------------------+---------+
|     output     |                    folder                     | scripts |
+----------------+-----------------------------------------------+---------+
| this is file a | C:\Users\mange\OneDrive\Desktop\Scripts\arial |  a.py   |
| This is file b | C:\Users\mange\OneDrive\Desktop\Scripts\arial |  b.py   |
| this is file c | C:\Users\mange\OneDrive\Desktop\Scripts\arial |  c.py   |
+----------------+-----------------------------------------------+---------+
```
