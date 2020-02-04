import mysql.connector


con = mysql.connector.connect(
user = "",
password = "",
host = "",
database = ""
)


word = input("Enter word for definition: ")
cursor = con.cursor()
query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % word)
results = cursor.fetchall()
con.close()

if results:
    print(f'\n{word}\n')
    [print(f' - {line}') for word, line in results]
else:
    print("Sorry no word is found.")
