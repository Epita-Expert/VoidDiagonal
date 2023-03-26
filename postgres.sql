-- docker exec -it 4bacb14e172c psql -U myuser -d mydatabase --password

DROP TABLE IF EXISTS medecin;
CREATE TABLE medecin (
  id SERIAL PRIMARY KEY,
  gender VARCHAR(10) NOT NULL,
  job VARCHAR(100) NOT NULL,
  lon NUMERIC NOT NULL,
  lat NUMERIC NOT NULL,
  city VARCHAR(100) NOT NULL,
  name VARCHAR(100) NOT NULL,
  department VARCHAR(100) NOT NULL,
  region VARCHAR(100) NOT NULL
);

