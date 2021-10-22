import csv, sqlite3

con = sqlite3.connect("..\db.sqlite3")


cur = con.cursor()
cur.execute("DROP TABLE product; ")
cur.execute("CREATE TABLE product (product_name, price, supermarket, id);") 

with open('tesco_discounts.csv','r') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    list_dr=list(dr)
    to_db = [(list_dr[i]['product_name'], list_dr[i]['price'], list_dr[i]['supermarket'],i) for i in range(len(list_dr))]

cur.executemany("INSERT INTO product (product_name, price, supermarket, id) VALUES (?, ?, ?, ?);", to_db)
con.commit()
con.close()