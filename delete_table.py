import sqlite3

conn = sqlite3.connect('blog.dv')

cursor = conn.cursor()
TABLE1 = "blog_posts"
TABLE2 = "User"
TABLE3 = "comments"

cursor.execute(f"DROP TABLE {TABLE1}")
print(f"Dropped Table {TABLE1}")

cursor.execute(f"DROP TABLE {TABLE2}")
print(f"Dropped Table {TABLE2}")

cursor.execute(f"DROP TABLE {TABLE3}")
print(f"Dropped Table {TABLE3}")

conn.commit()

conn.close()