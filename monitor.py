import time
from mailjet_rest import Client
import psutil

# Replace these with your actual Mailjet API credentials
api_key = "38c4d0d153510bbace5175d9227615b7"
api_secret = "d6a79706524ce4b4072b61c1de0c4fab"

#Define system time
current_time = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S",current_time)

# Thresholds for alerts
CPU_THRESHOLD = 2
RAM_THRESHOLD = 10
DISK_THRESHOLD = 50

def send_alert(subject, message):
    try:
        # Instantiate Mailjet client
        mailjet = Client(auth=(api_key, api_secret), version='v3.1')
        data = {
            'Messages': [
                {
                    "From": {
                        "Email": "gideon.adjei@amalitechtraining.org",
                        "Name": "Gideon"
                    },
                    "To": [
                        {
                            "Email": "adjeigideon911@gmail.com",
                            "Name": "Admin"
                        }
                    ],
                    "Subject": subject,
                    "HTMLPart": f"<h3>{message}</h3>"
                }
            ]
        }

        result = mailjet.send.create(data=data)
        print(f"Email sent: {result.status_code}")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")


# Check system metrics
cpu_usage = psutil.cpu_percent(interval=1)
# print(cpu_usage)
ram_usage = psutil.virtual_memory().percent
# print(ram_usage)
disk_usage = psutil.disk_usage('/').percent
# print(disk_usage)

alert_message = "Succefully Initiated"

if cpu_usage > CPU_THRESHOLD:
 alert_message += f"CPU usage is high: {cpu_usage}% (Threshold: {CPU_THRESHOLD}%)\n"
if ram_usage > RAM_THRESHOLD:
 alert_message += f"RAM usage is high: {ram_usage}% (Threshold: {RAM_THRESHOLD}%)\n"

if disk_usage > DISK_THRESHOLD:
     alert_message += f"Disk space is low: {100 - disk_usage}% free (Threshold: {DISK_THRESHOLD}% free)\n"

if alert_message:
 send_alert(f"Python Monitoring Alert Alert-{formatted_time}", alert_message)
else:
 print("All system metrics are within normal limits.")
