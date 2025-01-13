# Use the csv module to:
# Write product details (name, price, stock) into a CSV file.
# Read the file back and print the products sorted by price.

import csv

fields = ['name','price','stock']
rows = [['Milk',33,33],['Bread',45,31],['Mouse',330,3],['laptop',33000,21],['Phone',28000,12]]
with open('prodect_csv.csv','w+') as csvfile:
    csvwrite = csv.writer(csvfile)
    csvwrite.writerow(fields)
    csvwrite.writerows(rows)
    
    csvfile.seek(0)
    csvread = csv.reader(csvfile)
    print(next(csvread))
    products = sorted(csvread,key=lambda x: int(x[1]))
    for i in products:
        print(i)