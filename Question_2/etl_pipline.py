import sys, os, argparse
from tabulate import tabulate
from io import StringIO

def init_arguments():
    """
    Initialize arguments using argparse and return processed arguments
    """
    # Create the parser
    def strtobool(value):
        if isinstance(value, bool):
            return value
        if value.lower() in ('yes', 'true', 't', 'y', '1'):
            return True
        elif value.lower() in ('no', 'false', 'f', 'n', '0'):
            return False
        else:
            raise argparse.ArgumentTypeError('Boolean value expected.')
    parser=argparse.ArgumentParser(prog="etl.py",usage="%(prog)s path [options]",description="Script to execute etl scripts from a particular directory")
    
    # Add the argument
    parser.add_argument("path",metavar="path",help="path of scripts to be executed")
    parser.add_argument("--order","-ord",default=False,help="Order in which scripts are to be executed. Default:ascending(False)",choices=[False,True],type=strtobool)
    parser.add_argument("--file","-f",default="all",help="The exact file name to run. Default: all files")
    parser.add_argument("--outfile","-o",default="console",help="Output file name. Default: console")
    return parser.parse_args()

def get_execution_order(path,order):
    """
    Create a execution order as a dictionary and return it
    path:Path of scripts folder
    order:order in which scripts are executed Default:False=ascending
    """
    path=path if os.path.isabs(path) else os.path.abspath(path)
    file_dict=dict()

    # normal directory structure without any order
    for root,dirs,file in os.walk(path):
        file_dict[root]=sorted(file,reverse=order)
    return file_dict

def execute_scripts(file_dic,file):
    """
    execute scripts from file_tree dict
    file_dic: directionary of file got from os.walk
    file:particular file to be executed
    """
    output=dict()
    file_list=file_dic[list(file_dic.keys())[0]]
    file_path_list=[list(file_dic.keys())[0]+'/'+file for file in file_list]
    folder=[]
    script=[]
    if file=="all":
        console_output=[]
        for index,file in enumerate(file_path_list):
            folder.append(list(file_dic.keys())[0])
            script.append(file_list[index])
            old_stdout=sys.stdout
            redirect_stdout=sys.stdout=StringIO()
            exec(open(file).read())
            console_output.append(redirect_stdout.getvalue())
            sys.stdout=old_stdout

            output['output']=console_output
            output['folder']=folder
            output['scripts']=script
    else:
        output['folder']=list(file_dic.keys())[0]
        output['script']=file
        execution_file=list(file.keys())[0]+'/'+file
        output['output']=exec(open(execution_file).read())

    return output

def pretty_print(output,outfile):
    """
    print the output in a tabular format
    outfile:log output to a file default is console"
    """
    output_str=tabulate(output,headers=['output','folder','scripts'],tablefmt="pretty")
    if outfile=="console":
        print(output_str)
    else:
        output_file=open(outfile,"w")
        output_file.write(output_str)
        output_file.close()

if __name__=="__main__":
    args=init_arguments()
    execution_order=get_execution_order(args.path,args.order)
    output=execute_scripts(execution_order,args.file)
    pretty_print(output,args.outfile)
