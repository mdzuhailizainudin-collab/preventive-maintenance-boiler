import boto3
import random
import time
import os
from dotenv import load_dotenv

# 1. Load your credentials from the .env file
load_dotenv()

def stream_boiler_data():
    # 2. Initialize the CloudWatch client for the Singapore region
    cw = boto3.client(
        'cloudwatch',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        region_name=os.getenv('AWS_REGION')
    )

    print("🚀 BOILER TELEMETRY ONLINE")
    print("Streaming to 'Industrial/Boilers' namespace...")
    print("Press Ctrl+C to stop the stream anytime.\n")
    
    while True:
        # 3. Simulate realistic fluctuations
        # Conductivity: small jumps around 2500
        cond = random.uniform(2485, 2515) 
        # Efficiency: high performance with slight noise
        eff = random.uniform(89.0, 91.5)
        
        try:
            # 4. Push the data to the cloud
            cw.put_metric_data(
                Namespace='Industrial/Boilers',
                MetricData=[
                    {'MetricName': 'Conductivity', 'Value': cond, 'Unit': 'None'},
                    {'MetricName': 'Efficiency', 'Value': eff, 'Unit': 'Percent'}
                ]
            )
            timestamp = time.strftime('%H:%M:%S')
            print(f"[{timestamp}] Pushed >> Cond: {cond:.2f} | Eff: {eff:.2f}%")
        except Exception as e:
            print(f"❌ Connection Error: {e}")

        # 5. Wait 60 seconds before the next update
        time.sleep(60) 

if __name__ == "__main__":
    stream_boiler_data()
