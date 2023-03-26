-- docker exec -it 4bacb14e172c psql -U myuser -d mydatabase --password

DROP TABLE IF EXISTS medecin;
CREATE TABLE medecin (
  id SERIAL PRIMARY KEY,
  gender VARCHAR(10),
  job VARCHAR(100),
  lon NUMERIC,
  lat NUMERIC,
  city VARCHAR(100),
  name VARCHAR(100),
  department VARCHAR(100),
  region VARCHAR(100)
);

DROP TABLE IF EXISTS EDUCATION_ESTABLISHMENT;
CREATE TABLE EDUCATION_ESTABLISHMENT (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  denomination VARCHAR(255),
  lon FLOAT,
  lat FLOAT,
  sector VARCHAR(255),
  city VARCHAR(255),
  department VARCHAR(255),
  region VARCHAR(255),
  state VARCHAR(255)
);

