import csv
import matplotlib.pyplot as plt

lst_lcornea_loaded = []
lst_rcornea_loaded = []

with open('lockEBR.csv', mode='r', newline='') as file:
    reader = csv.reader(file)
    next(reader)  
    for row in reader:
        lst_rcornea_loaded.append(float(row[1]))
        lst_lcornea_loaded.append(float(row[2]))

# creates subplots
fig, axs = plt.subplots(2, 1, figsize=(18, 12), sharex=True)  # 2 rows, 1 column, shared x-axis

# plot lcornea on first plot
axs[0].plot(lst_lcornea_loaded, label='Left Cornea')
axs[0].set_ylabel('Mask Area')  
axs[0].legend()

# plot rcornea on second plot
axs[1].plot(lst_rcornea_loaded, label='Right Cornea', color='darkorange')
axs[1].set_xlabel('Files Processed') 
axs[1].set_ylabel('Mask Area') 
axs[1].legend()

fig.suptitle('Cornea Mask Areas Over Files')

plt.tight_layout()
plt.savefig('cornea_mask_areas_stacked.png', dpi=300)
plt.show()
plt.close(fig)