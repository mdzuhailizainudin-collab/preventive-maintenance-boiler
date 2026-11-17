import pandas as pd
import numpy as np
from datetime import datetime, timedelta
print("---  Starting Boiler Simulation (Local) ---")
intervals = 14 * 24 * 60 
start_time = datetime.now() - timedelta(days=14)
timestamps = [start_time + timedelta(minutes=i) for i in range(intervals)]
conductivity = 450.0
data = []

for i in range(intervals):
   
    conductivity += np.random.uniform(-1, 3.8) 
    
    
    efficiency = 85.0
    if conductivity > 2500:
        
        efficiency = 85.0 - ((conductivity - 2500) * 0.005)
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

print("--- 🚀 Starting Boiler Simulation (Local) ---")


intervals = 14 * 24 * 60 
start_time = datetime.now() - timedelta(days=14)
timestamps = [start_time + timedelta(minutes=i) for i in range(intervals)]


conductivity = 450.0
data = []

for i in range(intervals):
    conductivity += np.random.uniform(-1, 3.8) 
    

    efficiency = 85.0
    if conductivity > 2500:
        efficiency = 85.0 - ((conductivity - 2500) * 0.005)
    
    data.append({
        'Timestamp': timestamps[i],
        'Conductivity': conductivity,
        'Efficiency': max(70, efficiency) 
    })

df = pd.DataFrame(data)
df.to_csv('boiler_data.csv', index=False)

print("✅ SUCCESS: 'boiler_data.csv' has been created on your MacBook.")
