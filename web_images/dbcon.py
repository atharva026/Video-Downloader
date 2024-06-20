import psycopg2

a="aa"
b="bb"
d="26-8-2003"
g="Male"
e="aabb@gmail.com"

con = psycopg2.connect(host="localhost",port="5432",database="videodownloader",user="postgres",password="atharva")

cursor = con.cursor()



sql = "insert into register values(%s, %s, %s, %s, %s)"
val = (a, b, d, g, e)
cursor.execute(sql,val)

# commit the transaction
con.commit()

# print a message indicating the number of records inserted
print( "record inserted.")
#create table register(name varchar(20),username varchar(15) primary key,dateofbirth varchar(12),email varchar(50),password varchar(50));
