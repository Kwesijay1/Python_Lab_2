# Python System Monitoring Lab

## 📌 Introduction  
This lab demonstrates how to build a basic system monitoring tool using Python and the `psutil` library to track CPU usage, RAM usage, and disk space, set performance thresholds, and trigger automated email alerts using Mailjet when those thresholds are exceeded.

---

## ✅ Requirements  
- Python 3.6 or higher  
- Access to the Internet  
- A Mailjet account  
- An email inbox to receive alerts  
- Basic understanding of virtual environments and Python scripting

---

## 🎯 Lab Objectives  

- Monitor system metrics such as CPU usage, RAM usage, and disk space using Python’s `psutil` library.
- Define performance thresholds for key system resources.
- Configure and send automated email alerts using the Mailjet API.
- Integrate third-party libraries into Python scripts.
- Build and run a simple system monitoring script with alerting features.

---

## 🧪 Tasks Overview  

### ✅ Task 1: Sign Up for Mailjet Email API  
- Create a Mailjet account.
- Access the Mailjet Developer Portal and generate an API Key and Secret Key.

---

### ✅ Task 2: Python Environment Setup  
- Create a virtual environment using `venv`.
- Activate the environment.
- Install the necessary libraries: `psutil` and `mailjet_rest`.

---

### ✅ Task 3: Build the Monitoring Application  
- Create a new Python file named `monitor.py`.
- Import the required libraries.
- Define your Mailjet credentials either using environment variables or hardcoded.
- Get the current system time to timestamp alerts.
- Define thresholds for CPU, RAM, and disk space usage.
- Create a function that sends email alerts using the Mailjet API.
- Collect system metrics (CPU usage, RAM usage, disk space).
- Compose an alert message based on threshold violations.
- Send an email alert if any of the thresholds are exceeded.
- If no thresholds are exceeded, print a message indicating that system metrics are normal.

---

## 🚀 Running the Application  
- Run the monitoring script.
- Monitor the terminal output and verify email delivery.
- Check your email inbox or spam folder for alert notifications.

---

## 📩 Email Verification  
- Validate that your monitoring alert was successfully sent and received via Mailjet.
- Ensure that the email includes timestamped information about the exceeded system metrics.

---

## 📚 References  
- [psutil documentation](https://pypi.org/project/psutil/)  
- [Mailjet Send API v3.1 Documentation](https://dev.mailjet.com/email/guides/send-api-v31/)

---
