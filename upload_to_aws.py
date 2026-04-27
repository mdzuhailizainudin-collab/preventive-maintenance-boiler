import boto3
import pandas as pd
import os
import time
from dotenv import load_dotenv

# 1. Load your credentials from the .env file
load_dotenv()

def upload_data():
    print("--- ☁️ Connecting to AWS CloudWatch ---")
    
    # Check if the data file exists
    if not os.path.exists('boiler_data.csv'):
        print("❌ Error: boiler_data.csv not found! Run generate_data.py first.")
        return

    # 2. Setup the AWS Client
    try:
        cw = boto3.client(
            'cloudwatch',
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
            region_name=os.getenv('AWS_REGION')
        )
        
        # 3. Read the data we generated
        df = pd.read_csv('boiler_data.csv')
        
        print(f"🚀 Pushing the last 50 data points to the Cloud...")
        
        for index, row in df.tail(50).iterrows():
            cw.put_metric_data(
                Namespace='Industrial/Boilers',
                MetricData=[
                    {
                        'MetricName': 'Conductivity',
                        'Value': float(row['Conductivity']),
                        'Unit': 'None'
                    },
                    {
                        'MetricName': 'Efficiency',
                        'Value': float(row['Efficiency']),
                        'Unit': 'Percent'
                    }
                ]
            )
            print(f"Sent >> {row['Timestamp']} | Cond: {row['Conductivity']:.2f}")
            time.sleep(0.5) # Fast stream for demo

        print("\n✅ DEPLOYMENT COMPLETE!")
        print("Go to AWS Console > CloudWatch > Metrics > All Metrics.")

    except Exception as e:
        print(f"❌ AWS Error: {e}")

if __name__ == "__main__":
    upload_data()
