from sqlalchemy import Column, Integer, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker








if __name__ == "__main__":
    t = time.time() 

    db = 'db.db' #Database filename 
    file_name = "t.csv"

    data = Load_Data(file_name) #Get data from CSV

    Create_DB(db) #Create DB

    #For every record, format and insert to table
    for i in data:
        record = {
                'date' : i[0],
                'opn' : i[1],
                'hi' : i[2],
                'lo' : i[3],
                'close' : i[4],
                'vol' : i[5]
            }
        Add_Record(db, record)
