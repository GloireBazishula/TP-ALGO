import numpy as np
import pandas as pd

# Exemple de données CDR (à remplacer par vos propres données)
cdr_data = [
    {'Identifiant': 1447, 'Type_call': 0, 'Duree': 60, 'Taxe': 0, 'Total_volume': 0},
    {'Identifiant': 1448, 'Type_call': 1, 'Duree': 0, 'Taxe': 0, 'Total_volume': 0},
    {'Identifiant': 1449, 'Type_call': 1, 'Duree': 0, 'Taxe': 2, 'Total_volume': 0},
    {'Identifiant': 1441, 'Type_call': 0, 'Duree': 63, 'Taxe': 2, 'Total_volume': 0},
    {'Identifiant': 1442, 'Type_call': 2, 'Duree': 0 , 'Taxe': 2, 'Total_volume': 100}, 
    {'Identifiant': 1451, 'Type_call': 2, 'Duree': 0 , 'Taxe': 2, 'Total_volume': 1231},
    {'Identifiant': 1452, 'Type_call': 2, 'Duree': 0 , 'Taxe': 2, 'Total_volume': 26},
    {'Identifiant': 1453, 'Type_call': 2, 'Duree': 0 , 'Taxe': 2, 'Total_volume': 123},
    {'Identifiant': 1454, 'Type_call': 2, 'Duree': 0 , 'Taxe': 2, 'Total_volume': 1024},
    {'Identifiant': 1455, 'Type_call': 1, 'Duree': 0 , 'Taxe': 2, 'Total_volume': 0},    {'Identifiant': 1456, 'Type_call': 0, 'Duree': 63 , 'Taxe': 2, 'Total_volume': 0},
    {'Identifiant': 1457, 'Type_call': 1, 'Duree': 0 , 'Taxe': 2, 'Total_volume': 0},
    {'Identifiant': 1458, 'Type_call': 1, 'Duree': 0 , 'Taxe': 2, 'Total_volume': 0},   
    {'Identifiant': 1459, 'Type_call': 1, 'Duree': 0 , 'Taxe': 2, 'Total_volume': 0},
    {'Identifiant': 1460, 'Type_call': 2, 'Duree': 0 , 'Taxe': 2, 'Total_volume': 1000}, 
    {'Identifiant': 1461, 'Type_call': 1, 'Duree': 0 , 'Taxe': 2, 'Total_volume': 0},
    {'Identifiant': 1462, 'Type_call': 1, 'Duree': 0 , 'Taxe': 2, 'Total_volume': 0}, 
    {'Identifiant': 1463, 'Type_call': 1, 'Duree': 0 , 'Taxe': 2, 'Total_volume': 0}, 
    {'Identifiant': 1464, 'Type_call': 1, 'Duree': 0 , 'Taxe': 2, 'Total_volume': 0}, 
    {'Identifiant': 1465, 'Type_call': 1, 'Duree': 0 , 'Taxe': 2, 'Total_volume': 0}, 
    {'Identifiant': 1466, 'Type_call': 1, 'Duree': 0 , 'Taxe': 2, 'Total_volume': 0}, 
    {'Identifiant': 1467, 'Type_call': 1, 'Duree': 0 , 'Taxe': 2, 'Total_volume': 0}, 
    {'Identifiant': 1468, 'Type_call': 2, 'Duree': 0 , 'Taxe': 2, 'Total_volume': 12},
    {'Identifiant': 1470, 'Type_call': 1, 'Duree': 0 , 'Taxe': 2, 'Total_volume': 0}, 
    {'Identifiant': 1471, 'Type_call': 0, 'Duree': 63 , 'Taxe': 2, 'Total_volume': 0}, 
    {'Identifiant': 1472, 'Type_call': 0, 'Duree': 63 , 'Taxe': 2, 'Total_volume': 0}, 
    {'Identifiant': 1473, 'Type_call': 0, 'Duree': 63 , 'Taxe': 2, 'Total_volume': 0},
    {'Identifiant': 1474, 'Type_call': 0, 'Duree': 63 , 'Taxe': 2, 'Total_volume': 0},
    {'Identifiant': 1475, 'Type_call': 1, 'Duree': 0 , 'Taxe': 2, 'Total_volume': 0},
    {'Identifiant': 1476, 'Type_call': 2, 'Duree': 0 , 'Taxe': 1, 'Total_volume': 550},
    {'Identifiant': 1477, 'Type_call': 2, 'Duree': 0 , 'Taxe': 0, 'Total_volume': 234},
    {'Identifiant': 1478, 'Type_call': 2, 'Duree': 0 , 'Taxe': 2, 'Total_volume': 10},
    {'Identifiant': 1479, 'Type_call': 2, 'Duree': 0 , 'Taxe': 2, 'Total_volume': 12},
    {'Identifiant': 1480, 'Type_call': 0, 'Duree': 0 , 'Taxe': 0, 'Total_volume': 4},
    {'Identifiant': 1481, 'Type_call': 2, 'Duree': 0 , 'Taxe': 0, 'Total_volume': 50},
    {'Identifiant': 1482, 'Type_call': 2, 'Duree': 0 , 'Taxe': 2, 'Total_volume': 55},
    {'Identifiant': 1483, 'Type_call': 2, 'Duree': 0 , 'Taxe': 2, 'Total_volume': 123},
    {'Identifiant': 1484, 'Type_call': 0, 'Duree': 63 , 'Taxe': 1, 'Total_volume': 0},
    {'Identifiant': 1485, 'Type_call': 0, 'Duree': 63 , 'Taxe': 2, 'Total_volume': 0},
    {'Identifiant': 1486, 'Type_call': 0, 'Duree': 12 , 'Taxe': 1, 'Total_volume': 0},
    {'Identifiant': 1487, 'Type_call': 1, 'Duree': 0 , 'Taxe': 1, 'Total_volume': 0},
    {'Identifiant': 1488, 'Type_call': 1, 'Duree': 0 , 'Taxe': 2, 'Total_volume': 0},
    {'Identifiant': 1489, 'Type_call': 1, 'Duree': 0 , 'Taxe': 2, 'Total_volume': 0},
    {'Identifiant': 1490, 'Type_call': 1, 'Duree': 0 , 'Taxe': 2, 'Total_volume': 0},
    
    
    
    # ... Ajoutez les autres enregistrements ici ...
]

# Convertir les données en un DataFrame pandas
df = pd.DataFrame(cdr_data)

# Calculer la durée totale des appels
duree_totale_appels = df[df['Type_call'] == 0]['Duree'].sum()

# Calculer le nombre total de SMS
nb_total_sms = df[df['Type_call'] == 1].shape[0]

# Calculer les gigaoctets utilisés pour Internet
gigabytes_utilises = df[df['Type_call'] == 2]['Total_volume'].sum() / 1024  # Convertir en Go

print(f"Durée totale des appels : {duree_totale_appels} secondes")
print(f"Nombre total de SMS : {nb_total_sms}")
print(f"Gigaoctets utilisés : {gigabytes_utilises:.2f} Go")
# Calculer le montant de facturation pour chaque enregistrement
def calculer_montant(row):
    if row['Type_call'] == 0:  # Appel
        return row['Duree'] * 0.025  # Coût par minute pour un appel
    elif row['Type_call'] == 1:  # SMS
        return 0.001 if row['Type_call'] == row['Type_call'] else 0.002  # Coût par SMS
    elif row['Type_call'] == 2:  # Internet
        return row['Total_volume'] * 0.03  # Coût par Mo

df['Montant'] = df.apply(calculer_montant, axis=1)

# Calculer le montant total dépensé par chaque client
montants_par_client = df.groupby('Identifiant')['Montant'].sum()

# Afficher les montants par client
for client_id, montant in montants_par_client.items():
    print(f"Client {client_id} : Montant total dépensé = ${montant:.2f}")
    
print("le montant de facturation totale est : ", sum(montants_par_client))
