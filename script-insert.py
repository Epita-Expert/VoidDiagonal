import json
import psycopg2
# pip install psycopg2
# docker exec -it 4bacb14e172c psql -U myuser -d mydatabase --password

# Load the JSON data from file
with open('./medecins.json', 'r') as f:
    data = json.load(f)

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host='localhost',
    port='5432',
    user='myuser',
    password='mypassword',
    database='mydatabase'
)
cur = conn.cursor()

# Define the SQL query to insert a row
query = '''
    INSERT INTO medecin (gender, job, lon, lat, city, name, department, region) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
'''

# Execute the SQL query for each row of data
for row in data:
    cur.execute(query, (
        row['gender'],
        row['job'],
        row['lon'],
        row['lat'],
        row['city'],
        row['name'],
        row['department'],
        row['region']
    ))

# Commit the changes and close the database connection
conn.commit()
cur.close()
conn.close()
