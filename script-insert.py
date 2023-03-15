import json
import psycopg2

# Load the JSON data from file
with open('./medecins-output.json', 'r') as f:
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
    INSERT INTO your_table (civilite, column_9, column_10, column_11, column_12, column_13, column_14, column_15,
        column_16, column_17, column_18, column_19, column_20, column_21, column_22, column_23, column_24, column_25,
        column_26, column_27, column_28, column_29, column_30, column_31, column_32, column_33, nom, adresse,
        libelle_profession, type_dacte_realise, nom_acte, coordonnees, commune, code_insee, nom_epci, nom_dep, nom_reg,
        code_epci, insee_reg, insee_dep, activite_principale, libelle_regroupement, libelle, tarif_2, tarif_1,
        tarif_base_de_remboursement_securite_sociale, libelle_acte_clinique, concat)
    VALUES (%(civilite)s, %(column_9)s, %(column_10)s, %(column_11)s, %(column_12)s, %(column_13)s, %(column_14)s,
        %(column_15)s, %(column_16)s, %(column_17)s, %(column_18)s, %(column_19)s, %(column_20)s, %(column_21)s,
        %(column_22)s, %(column_23)s, %(column_24)s, %(column_25)s, %(column_26)s, %(column_27)s, %(column_28)s,
        %(column_29)s, %(column_30)s, %(column_31)s, %(column_32)s, %(column_33)s, %(nom)s, %(adresse)s,
        %(libelle_profession)s, %(type_dacte_realise)s, %(nom_acte)s, %(coordonnees)s, %(commune)s, %(code_insee)s,
        %(nom_epci)s, %(nom_dep)s, %(nom_reg)s, %(code_epci)s, %(insee_reg)s, %(insee_dep)s, %(activite_principale)s,
        %(libelle_regroupement)s, %(libelle)s, %(tarif_2)s, %(tarif_1)s, %(tarif_base_de_remboursement_securite_sociale)s,
        %(libelle_acte_clinique)s, %(concat)s)
'''

# Execute the SQL query for each row of data
for row in data:
    cur.execute(query, row)

# Commit the changes and close the database connection
conn.commit()
cur.close()
conn.close()
