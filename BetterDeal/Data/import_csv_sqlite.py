import csv, sqlite3

con = sqlite3.connect("..\db.sqlite3")


cur = con.cursor()

#cur.execute("DROP TABLE product; ")
#cur.execute("CREATE TABLE product (product_name, price, supermarket, id);") 

cur.execute("DELETE FROM product;") # resets the table 

with open('tesco_discounts.csv','r') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['product_name'], i['price'], i['supermarket']) for i in dr]

cur.executemany("INSERT INTO product (product_name, price, supermarket) VALUES (?, ?, ?);", to_db)
con.commit()
con.close()