from pymongo import MongoClient
import matplotlib.pyplot as plt

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

# 1. Connect to data base via link above (copy link from mongodb.com)

client = MongoClient(mongo_uri)

# 2. Get / Create database

database = client.get_database() 
# 3. Get / Create collection

customers = database["customers"]
count_cus = customers.count()
# 4. Read / Find list of customers group by ref

customers_ads = customers.find({"ref" : "ads"}).count()
customers_wom = customers.find({"ref" : "wom"}).count()
customers_events = customers.find({"ref" : "events"}).count()

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Ads', 'Wom', 'Events'
sizes = [customers_ads/count_cus, customers_wom/count_cus, customers_events/count_cus]
explode = (0, 0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()

