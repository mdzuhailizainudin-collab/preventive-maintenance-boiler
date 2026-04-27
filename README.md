# Industrial Boiler-to-Cloud Integration

This project demonstrates a technical pipeline for industrial asset monitoring. It generates simulated boiler conductivity data and integrates directly with AWS services for real-time tracking and automated alerting.

### Project Overview
* **Data Source:** Python script simulating boiler sensors (Conductivity/Fouling).
* **Cloud Integration:** Boto3 SDK pushing metrics to AWS CloudWatch.
* **Monitoring:** CloudWatch Alarms for threshold detection and SNS for email notifications.

### System Architecture
```text
[Local Workstation] --(boto3 PutMetricData API)--> [Amazon CloudWatch]
   (VSCode Environment)                                | (Industrial/Boilers)
   (generate_data.py)                                  |
                                                       v
                                            [Custom Dashboard / Alarms]
                                            (Conductivity & SNS Alerts)