import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import folium
from folium.plugins import HeatMap

# Load sample of data for quick processing
df = pd.read_csv(r'C:\Users\windows 10\Downloads\archive (1)\US_Accidents_March23.csv', nrows=100000)

# Convert time and extract hour
df['Start_Time'] = pd.to_datetime(df['Start_Time'])
df['Hour'] = df['Start_Time'].dt.hour

# Drop rows with missing key data
df.dropna(subset=['Start_Lat', 'Start_Lng', 'Weather_Condition'], inplace=True)

# Accidents by hour
sns.countplot(x='Hour', data=df)
plt.title('Accidents by Hour'); plt.show()

# Top 5 weather conditions
df['Weather_Condition'].value_counts().nlargest(5).plot(kind='bar', color='orange')
plt.title('Top Weather Conditions'); plt.show()

# Top 5 states
df['State'].value_counts().nlargest(5).plot(kind='bar', color='green')
plt.title('Top States by Accident Count'); plt.show()

# Hotspot Map using 1,000 sample points
sample = df[['Start_Lat', 'Start_Lng']].sample(1000)
m = folium.Map(location=[39.5, -98.35], zoom_start=4)
HeatMap(sample.values).add_to(m)
m.save('hotspots.html')
print("Hotspot map saved as 'hotspots.html'")
