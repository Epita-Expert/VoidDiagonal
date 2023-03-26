# Split file into multiple files of 50MB each
split -b 50M medecins-output.json ./medecins-splitted/edecins-splitted-output-

# Read the first 100 lines of a file
head -n 100 medecins-output.json

# Format json file
jq -r '.' medecins.json > formatted_medecins.json

# Remove fields from json file
jq 'del(.column_22, .column_23, .column_24, .column_25, .column_26, .column_27, .column_28, .column_29, .column_30, .column_31, .column_32, .column_33, .adresse, .nom, .column_9, .concat, .libelle_acte_clinique, .libelle, .libelle_regroupement, .activite_principale, .libelle_acte_clinique, .nom_acte, .type_dacte_realise, .column_10, .column_9)' medecins.json > medecins_minimized.json

# select only some fields from json file
jq '.[] | {gender: .civilite, job: .libelle_profession, lon: .coordonnees.lon, lat: .coordonnees.lat, city: .commune, name: .nom, department: .nom_dep, region: .nom_reg}' medecins-output.json > medecins_minimized.json
