import os 
from dotenv import load_dotenv
import psycopg2
import data_gen

load_dotenv()

def pgconnect():
    try :  
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        cur=conn.cursor()
        cur.execute("SET search_path TO private;") 
        print(f"successfully connected to database ")
        
        return conn,cur
        
    except Exception as e:
        print(f"the error is {e}")
        
            
def create_employee(table_name):
    conn, cur= pgconnect()
    query= f"""create table if not exists {table_name} (
        ID VARCHAR(255) PRIMARY KEY NOT NULL,
        FIRSTNAME VARCHAR(255),
        LASTNAME VARCHAR(255),
        DEPARTMENT VARCHAR(255),
        SALARY BIGINT);"""
    
    cur.execute(query)
    conn.commit()
    
    
def generate__and_load(table_name):
    conn, cur= pgconnect()
    query=f""" insert into  {table_name} (ID , FIRSTNAME , LASTNAME , DEPARTMENT , SALARY )
            VALUES(%s,%s,%s,%s,%s)
    """
    for i in range(20):
        first,last =data_gen.gen_name()
        deps=data_gen.gen_department()
        sala=data_gen.gen_salary()
        
        cur.execute(query,(i ,first,last,deps,sala))
    
    conn.commit()
    
    
    
        
def drop_table(table_name):
    conn, cur= pgconnect()
    query= f"""DROP TABLE if  exists {table_name} ;"""
    
    cur.execute(query)
    conn.commit()
   
    
             
           
def main():
    table_name = "employee"
    drop_table(table_name)
    create_employee(table_name)
    generate__and_load(table_name)
    
            
if __name__ == '__main__':
    main()