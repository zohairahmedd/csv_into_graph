import csv
import matplotlib.pyplot as plt

lst_lcornea_loaded = []
lst_rcornea_loaded = []

with open('lockEBR_5000.csv', mode='r', newline='') as file:
    reader = csv.reader(file)
    next(reader)  
    for row in reader:
        lst_rcornea_loaded.append(float(row[1]))
        lst_lcornea_loaded.append(float(row[2]))

fig, ax = plt.subplots(figsize=(18, 12))

ax.plot(lst_lcornea_loaded, label='Left Cornea')

ax.plot(lst_rcornea_loaded, label='Right Cornea', color='darkorange')

ax.set_xlabel('Files Processed') 
ax.set_ylabel('Mask Area') 
ax.legend()

fig.suptitle('Cornea Mask Areas Over Files')

plt.tight_layout()
plt.show()
plt.close(fig)