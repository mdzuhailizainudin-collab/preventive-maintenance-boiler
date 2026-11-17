import boto3
import random
import time
import os
from dotenv import load_dotenv


load_dotenv()

def stream_boiler_data():
  
    cw = boto3.client(
        'cloudwatch',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        region_name=os.getenv('AWS_REGION')
    )

    print(" BOILER TELEMETRY ONLINE")
    print("Streaming to 'Industrial/Boilers' namespace...")
    print("Press Ctrl+C to stop the stream anytime.\n")
    
    while True:
       
        cond = random.uniform(2485, 2515) 
        eff = random.uniform(89.0, 91.5)
        
        try:
   
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
            print(f" Connection Error: {e}")

 
        time.sleep(60) 

if __name__ == "__main__":
    stream_boiler_data()
