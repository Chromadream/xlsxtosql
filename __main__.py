from excelimport import importfromexcel
from sql import send_sql

if __name__=='__main__':
    db = importfromexcel(filename = 'pricelist.xlsx', worksheet = 'Barang',rowsize=693,colsize=4)
    send_sql(hostname="test-server",db="GEMILANG",user="chroma",passwd="unspecified",li=db)