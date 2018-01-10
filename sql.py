def send_sql(hostname,db,user,passwd,li):
    import MySQLdb
    conn = MySQLdb.connect(host=hostname,db=db,user=user,passwd=passwd)
    cursor = conn.cursor()
    default = 0
    stat = "Harga Regular"
    for _ in range(30):
        #print(li[_])
        cursor.execute("""INSERT INTO PRODUCT (product_name,product_purchase_price, product_sale_price, product_stock_unit) VALUES (%s,%s,%s,%s)""",(li[_][1],default,li[_][3],li[_][2]))
    conn.commit()
