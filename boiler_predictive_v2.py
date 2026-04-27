import boto3
import pandas as pd
import os
import time
import random
from dotenv import load_dotenv

# 1. Load credentials from .env
load_dotenv()

def run_demo():
    print("--- ☁️ Starting AI Predictive Maintenance Demo ---")
    
    # 2. Setup the AWS Client
    try:
        cw = boto3.client(
            'cloudwatch',
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
            region_name=os.getenv('AWS_REGION')
        )
        
        # 3. Read the existing CSV data
        if not os.path.exists('boiler_data.csv'):
            print("❌ Error: boiler_data.csv not found! Make sure it's in this folder.")
            return
        df = pd.read_csv('boiler_data.csv')

        print("🚀 Pushing data with Simulated Drift (Predictive Mode)...")
        
        drift = 0.0
        cycle = 0

        # We take the last 60 rows and send them 1-by-1
        for index, row in df.tail(60).iterrows():
            cycle += 1
            
            # THE DRIFT: After 20 seconds, start increasing the value
            if cycle > 20:
                drift += 2.5 # Jumps by 2.5 each time to hit the alarm fast
            
            # We add the drift to the original Conductivity value
            simulated_value = float(row['Conductivity']) + drift
            
            cw.put_metric_data(
                Namespace='Industrial/Boilers',
                MetricData=[
                    {
                        'MetricName': 'Conductivity',
                        'Value': simulated_value,
                        'Unit': 'None'
                    }
                ]
            )
            
            print(f"Cycle {cycle}/60 | Value: {simulated_value:.2f} | Drift: +{drift}")
            time.sleep(1) # Total demo time = 1 minute

        print("\n✅ DATA UPLOAD COMPLETE!")
        print("Now go to AWS CloudWatch to see your spike!")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    run_demo()