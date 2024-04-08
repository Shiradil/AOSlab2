import platform, psutil, os, socket, time, getpass

# Functions to retrieve system information (from previous discussions)
def get_os_info():
    return platform.system(), platform.release()

def get_processor_info():
    return platform.processor()

def get_memory_info():
    total_memory_gb = psutil.virtual_memory().total / (1024**3)
    return total_memory_gb

def get_disk_info():
    disk_usage_gb = psutil.disk_usage('/').free / (1024**3)
    return disk_usage_gb

def get_current_user():
    return getpass.getuser()

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

def get_system_uptime():
    return time.time() - psutil.boot_time()

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

# Function to display the collected information
def display_system_info():
    print(f"OS: {get_os_info()[0]} {get_os_info()[1]}")
    print(f"Processor: {get_processor_info()}")
    print(f"Total Memory: {get_memory_info():.2f} GB")
    print(f"Available Disk Space: {get_disk_info():.2f} GB")
    print(f"Current User: {get_current_user()}")
    print(f"IP Address: {get_ip_address()}")
    print(f"System Uptime: {int(get_system_uptime())} seconds")
    print(f"CPU Usage: {get_cpu_usage()}%")

# Main function to run the program
if __name__ == "__main__":
    display_system_info()
