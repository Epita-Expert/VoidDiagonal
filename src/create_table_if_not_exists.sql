
CREATE TABLE IF NOT EXISTS finess_geo (
    id SERIAL PRIMARY KEY,
    nofinesset VARCHAR(255), nofinessej VARCHAR(255), rs VARCHAR(255), rslongue VARCHAR(255), complrs VARCHAR(255), compldistrib VARCHAR(255), numvoie VARCHAR(255), typvoie VARCHAR(255), voie VARCHAR(255), compvoie VARCHAR(255), lieuditbp VARCHAR(255), commune VARCHAR(255), departement VARCHAR(255), libdepartement VARCHAR(255), ligneacheminement VARCHAR(255), telephone VARCHAR(255), telecopie VARCHAR(255), categetab VARCHAR(255), libcategetab VARCHAR(255), categagretab VARCHAR(255), libcategagretab VARCHAR(255), siret VARCHAR(255), codeape VARCHAR(255), codemft VARCHAR(255), libmft VARCHAR(255), codesph VARCHAR(255), libsph VARCHAR(255), dateouv VARCHAR(255), dateautor VARCHAR(255), maj VARCHAR(255), numuai VARCHAR(255), coordxet VARCHAR(255), coordyet VARCHAR(255), sourcecoordet VARCHAR(255), datemaj VARCHAR(255),
    latitude NUMERIC(9,6),
    longitude NUMERIC(9,6)
);
    