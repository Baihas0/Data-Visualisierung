import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


file_path = 'C:\\Users\\kreny\\Downloads\\data.csv'
data = pd.read_csv(file_path)


selected_countries = ['Austria', 'Germany', 'Italy', 'France']
filtered_data = data[data['country'].isin(selected_countries)]
grouped_data = filtered_data.groupby(['country', 'year_week']).agg({'new_cases': 'sum'}).reset_index()
grouped_data['new_cases_millions'] = grouped_data['new_cases'] / 1_000_000

plt.figure(figsize=(15, 8))
sns.lineplot(data=grouped_data, x='year_week', y='new_cases_millions', hue='country', marker='o')

plt.title('Entwicklung der COVID-19-Fallzahlen im Ländervergleich (in Millionen)')
plt.xlabel('Jahr und Woche')
plt.ylabel('Anzahl neuer Fälle (in Mio.)')


every_nth = 10
weeks = grouped_data['year_week'].unique()
plt.xticks(ticks=[i for i in range(len(weeks)) if i % every_nth == 0], 
           labels=[weeks[i] for i in range(len(weeks)) if i % every_nth == 0], 
           rotation=90)
plt.grid(True, which='major', axis='both', linestyle='-', linewidth=0.5)
plt.gca().xaxis.grid(True, which='major', linestyle='-', linewidth=0.5)

plt.gca().ticklabel_format(style='plain', axis='y')

plt.legend(title='Land')
plt.tight_layout()
plt.show()
