# xlsxtosql

A quick tool I build to convert Excel 2010/2013/2017 worksheet to MySQL database entries.

It's a tool I make for [Gemilang_POS](https://github.com/Chromadream/Gemilang_POS) migration process, as the old Point-of-Sale system used an Excel macro worksheet.

Will clean the source code more, but for now it'll do it work just fine.

Requirement:

* Python 3 (I used Python 3.6.4, but 3.x will do just fine)
* [openpyxl](https://openpyxl.readthedocs.io/)
* [MySQLdb](https://github.com/PyMySQL/mysqlclient-python)
* virtualenv (optional)