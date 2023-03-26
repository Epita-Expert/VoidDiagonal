import csv
import psycopg2
from pyproj import Transformer
from tqdm import tqdm

# Création d'un objet transformateur de projection
# Projection Lambert 93
# Projection WGS84 (latitude, longitude)
transformer = Transformer.from_crs('epsg:2154','epsg:4326')

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host='localhost',
    port='5432',
    user='myuser',
    password='mypassword',
    database='mydatabase'
)

cur = conn.cursor()

# Define the SQL query to create the table if it does not exist

# Load the JSON data from file
with open('./datasets/3dc9b1d5-0157-440d-a7b5-c894fcfdfd45.csv', 'r') as f:
    reader = csv.reader(f)

    header = next(reader)
    # for row in reader:
    #     print(row)
        
    # Drop the table
    cur.execute("DROP TABLE IF EXISTS finess_geo")
    conn.commit()

    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS finess_geo (
        id SERIAL PRIMARY KEY,
        {', '.join(f"{col.strip()} VARCHAR(255)" for col in header if col.strip())},
        latitude NUMERIC(9,6),
        longitude NUMERIC(9,6)
    );
    """
    print(create_table_query)

    # Execute the SQL query to create the table
    cur.execute(create_table_query)

    # Truncate the table
    cur.execute("TRUNCATE finess_geo")


    query = "INSERT INTO finess_geo({}) VALUES ({})"
    columns = "id" + ",".join(header) + ", latitude, longitude"
    values = ", ".join(['%s' for _ in range(len(header)+2)])
    query = query.format(columns, values)

    # Print the generated query for testing purposes
    # print(query)

    # Execute the query
    print("Inserting data...")
    total_rows = sum(1 for row in reader)
    f.seek(0)  # Reset the file pointer to the beginning
    next(reader)  # Skip the header row
    with tqdm(total=total_rows) as pbar:
        for row in reader:
            # Conversion des coordonnées
            try:
                x, y = float(row[32]), float(row[33])
                lon, lat = transformer.transform(x, y)
                # print(x, y, lon, lat)
                row.append(str(lat))
                row.append(str(lon))
                cur.execute(query, row)
            except ValueError:
                continue

            # Update the progress bar
            pbar.update(1)


# Commit the changes and close the database connection
conn.commit()
cur.close()
conn.close()
