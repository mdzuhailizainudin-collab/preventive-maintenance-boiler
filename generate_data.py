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
    # Simulate rising impurities
    conductivity += np.random.uniform(-1, 3.8) 
    
    # Efficiency logic: Scaling starts impacting at 2500 uS/cm
    efficiency = 85.0
    if conductivity > 2500:
        # Every unit over 2500 drops efficiency slightly
        efficiency = 85.0 - ((conductivity - 2500) * 0.005)
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

print("--- 🚀 Starting Boiler Simulation (Local) ---")

# 1. Setup Timeframe (14 Days)
intervals = 14 * 24 * 60 
start_time = datetime.now() - timedelta(days=14)
timestamps = [start_time + timedelta(minutes=i) for i in range(intervals)]

# 2. Simulation Variables
conductivity = 450.0
data = []

for i in range(intervals):
    # Simulate rising impurities
    conductivity += np.random.uniform(-1, 3.8) 
    
    # Efficiency logic: Scaling starts impacting at 2500 uS/cm
    efficiency = 85.0
    if conductivity > 2500:
        # Every unit over 2500 drops efficiency slightly
        efficiency = 85.0 - ((conductivity - 2500) * 0.005)
    
    data.append({
        'Timestamp': timestamps[i],
        'Conductivity': conductivity,
        'Efficiency': max(70, efficiency) # Floor it at 70%
    })

# 3. Create the CSV file
df = pd.DataFrame(data)
df.to_csv('boiler_data.csv', index=False)

print("✅ SUCCESS: 'boiler_data.csv' has been created on your MacBook.")
