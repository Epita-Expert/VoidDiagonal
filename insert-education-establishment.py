import json
import psycopg2
# pip install psycopg2
# docker exec -it 4bacb14e172c psql -U myuser -d mydatabase --password

# Load the JSON data from file
with open('./educational-establishment.json', 'r') as f:
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

query = '''
    INSERT INTO EDUCATION_ESTABLISHMENT (name, denomination, lon, lat, sector, city, department, region, state) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
'''

# Execute the SQL query for each row of data
for row in data:
    cur.execute(query, (
        row['name'],
        row['denomination'],
        row['lon'],
        row['lat'],
        row['sector'],
        row['city'],
        row['department'],
        row['region'],
        row['state']
    ))

# Commit the changes and close the database connection
conn.commit()
cur.close()
conn.close()
