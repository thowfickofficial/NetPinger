import ping3
import schedule
import subprocess
import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="network_monitor.log",
)

def send_email(subject, body, attachment=None):
    # TODO: Add your email sending logic here
    pass

def ping_device(device):
    # TODO: Add your ping device logic here
    pass

def monitor_devices(devices):
    for device in devices:
        ping_device(device)

def get_user_input():
    devices = []
    print("\nNetPinger - Network Device Monitoring Tool")
    print("==========================================")
    print("This tool allows you to monitor the status of network devices by periodically pinging them.")
    print("Enter the details of the devices you want to monitor.")
    
    while True:
        name = input("Enter the device name (or 'done' if finished): ")
        if name.lower() == 'done':
            break
        address = input(f"Enter the IP address or hostname for '{name}': ")
        devices.append({"name": name, "address": address})
    return devices

def get_email_config():
    smtp_server = input("Enter the SMTP server: ")
    smtp_port = input("Enter the SMTP port: ")
    sender_email = input("Enter your email address: ")
    sender_password = input("Enter your email password: ")
    receiver_email = input("Enter the receiver's email address: ")

    return {
        "smtp_server": smtp_server,
        "smtp_port": smtp_port,
        "sender_email": sender_email,
        "sender_password": sender_password,
        "receiver_email": receiver_email,
    }

if __name__ == "__main__":
    # Display the tool name in figlet style
    subprocess.run(["figlet", "NetPinger"])
    devices_to_monitor = get_user_input()
    email_config = get_email_config()

    # Schedule the monitoring task to run every 5 minutes
    schedule.every(5).minutes.do(monitor_devices, devices=devices_to_monitor)

    # Run the monitoring task immediately
    monitor_devices(devices_to_monitor)

    # Start the scheduled monitoring
    print("\nNetPinger is now monitoring your network devices.")
    print("Press Ctrl+C to stop monitoring.")
    
    while True:
        schedule.run_pending()
