import sys
import os
from pathlib import Path

PATH = str(Path.cwd())+"/root/"

def list_DB():
    for i in os.listdir(PATH):
        yield i

# This creates anonymous filename -> str(file_name)
# DATE : 16/03/2026

def create_untitled(db_name):
    count = 1
    while os.path.exists(PATH+"/"+db_name+f"/untitled{count}.csv"):
        count +=1
    
    
    return f"untitled{count+1}.csv"
    

# This creates anonymous dirname -> str(dirname)
# DATE : 16/03/2026

def create_untitled_dir():
    count = 1
    while os.path.exists(PATH+F"untitled{count}"):
        count +=1
    
    return f"untitled{count}"

# This create new file -> none
# DATE : 16/03/2026

def create_table(cmd_list:list):
    
    if cmd_list[1] == "INTO":
        path = PATH+cmd_list[2]
        file_name = create_untitled(cmd_list[2])
        
        file = open(path+"/"+file_name, "w")
        file.close()
       
    else:
        path = PATH+cmd_list[3]
        file_name = cmd_list[1]
        file = open(path + f"/{file_name}.csv", "w")
        file.close()


# this is root (entry point function) -> none
# date - 15-03-2026

def main():
    
    print("-"*75)
    message = "WELCOME TO OUR DATA BASE"
    print("|",22*" ",message,22*" ","|")

    if len(sys.argv) >= 2:
        if sys.argv[1] == "--h":
            print('''
                to create a new DB      : CREATE_DB <database_name>
                to create a table       : CREATE_TABLE <table_name> INTO <DB_name>
                to use perticular DB    : USE <db_name>
                to use perticular table : USE <table_name > FROM <DB_name>
                to fill data into table : 
                
                                          USE <table_name > FROM <DB_name>
                                            WRITE{
                                            <column_name>:<data>,....,<n_data>;
                                            <column_name>:<data>,....,<n_data>;
                                            .
                                            .
                                            .
                                            <column_name>:<data>,....,<n_data>;
                                        }
                                        
            to show elements in perticular coumn of particular table :
            
                                            USE <Table_name> FROM <DB_name>
                                            SHOW COLUMN
                                            
            to show all coumn of particular table :
            
                                            USE <Table_name> FROM <DB_name>
                                            SHOW COLUMN
            to show all from a table :
                                            USE <Table_name> FROM <DB_name>
                                            SHOW COLUMN
            to show all DB :
                                            SHOW DATA_BASES
                                            
            to search table name in all DB's:
                                            SEARCH <Table_Name>                
            
                ''')
            
    terminate = False
    while terminate == False:
        cmd = input(">>> ")
        splited_cmd = cmd.split(" ")
        
        if cmd=="exit":
            break
        
        if splited_cmd[0] == "CREATE_DB":
            if len(splited_cmd) < 2:
                db_name = create_untitled_dir()
            else:
                db_name = splited_cmd[1]
                
            os.makedirs(PATH + db_name)
            
        elif splited_cmd[0] == "CREATE_TABLE":
            create_table(splited_cmd)
            print("-"*75,"\nTABLE CREATED IN THE DATABASE\n"+"-"*75)
                
        elif splited_cmd[0] == "SHOW_ALL_DB":
            num = 0
            print()
            for db in list_DB():
                num += 1
                print(num," " +db)
            
            print("-"*75)
                

if __name__ == "__main__":
    main()