import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="6090", database="project")
my_cursor = mydb.cursor()

# my_cursor.execute("CREATE TABLE menu(id int AUTO_INCREMENT PRIMARY KEY,dish VARCHAR(255),price int)")
# my_cursor.execute("CREATE TABLE Order_detail(id int AUTO_INCREMENT PRIMARY KEY,dish VARCHAR(255),price int,quantity int,phone VARCHAR(15) NOT NULL,address VARCHAR(255))")
# my_cursor.execute("CREATE TABLE confirm_order(id int PRIMARY KEY,dish VARCHAR(255),price int,quantity int,phone VARCHAR(15) NOT NULL,address VARCHAR(255))")
# my_cursor.execute("CREATE TABLE reservations(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(100) NOT NULL,phone VARCHAR(15) NOT NULL,date DATE NOT NULL,time TIME NOT NULL,people INT NOT NULL)")
my_cursor.execute("SHOW TABLES")
for x in my_cursor:
    print(x)

# my_cursor.execute("DROP TABLE confirm_order")
# my_cursor.execute("DROP TABLE order_1")
# my_cursor.execute("DROP TABLE order_2")
# my_cursor.execute("kDROP TABLE reservations")
# my_cursor.execute("DROP TABLE Order_detail")




# my_cursor.execute("SELECT * FROM confirm_order")
# for x in my_cursor:
#     print(x)
# my_cursor.execute("SELECT * FROM reservations")
# for x in my_cursor:
#     print(x)
# my_cursor.execute("SELECT * FROM Order_detail")
# for x in my_cursor:
#     print(x)
