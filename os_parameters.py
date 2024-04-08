import platform, psutil, socket, time, getpass, os
# Retrieve the operating system's name and

def get_os_info():
    try:
        return platform.system(), platform.version()
    except Exception as e:
        return ("Error retrieving OS info", str(e))

# Retrieve the processor name/information
def get_processor_info():
    try:
        return platform.processor()
    except Exception as e:
        return "Error retrieving processor info"

# Retrieve the total memory in gigabytes
def get_memory_info():
    try:
        total_memory_gb = psutil.virtual_memory().total / (1024**3)
        return total_memory_gb
    except Exception as e:
        return "Error retrieving memory info"

# Retrieve the available disk space in gigabytes.
def get_disk_info():
    try:
        disk_usage_gb = psutil.disk_usage('/').free / (1024**3)
        return disk_usage_gb
    except Exception as e:
        return "Error retrieving disk info"

# Retrieve the current user logged into the operating system.
def get_current_user():
    try:
        return getpass.getuser()
    except Exception as e:
        return "Error retrieving current user"

# Retrieve the system's primary IP address.
def get_ip_address():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    except Exception as e:
        ip = "Error retrieving IP address"
    finally:
        s.close()
    return ip

# Retrieve the system uptime in seconds.
def get_system_uptime():
    try:
        return time.time() - psutil.boot_time()
    except Exception as e:
        return "Error retrieving system uptime"

# Retrieve the current CPU usage as a percentage.
def get_cpu_usage():
    try:
        return psutil.cpu_percent(interval=1)
    except Exception as e:
        return "Error retrieving CPU usage"

# Retrieve details of running processes
def get_running_processes_info():
    # Retrieve a list of all running processes represented by psutil.Process objects
    processes = [psutil.Process(pid) for pid in psutil.pids()]
    process_info = []
    for proc in processes:  # Limiting to the first 10 processes for brevity
        try:
            pid = proc.pid
            name = proc.name()
            memory_usage = proc.memory_info().rss / (1024 ** 2)  # Convert bytes to MB
            process_info.append((pid, name, f"{memory_usage:.2f} MB"))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass  # If the process no longer exists or access is denied, skip it
    return process_info

# Retrieve information about disk partitions
def get_disk_partitions_info():
    partitions = psutil.disk_partitions()
    partition_info = [(partition.device, partition.mountpoint) for partition in partitions]
    return partition_info

# Function to display the collected system information.
def display_system_info():
    print(f"OS: {get_os_info()[0]} {get_os_info()[1]}")
    print(f"Processor: {get_processor_info()}")
    memory_info = get_memory_info()
    print(f"Total Memory: {memory_info:.2f} GB" if not isinstance(memory_info, str) else memory_info)
    disk_info = get_disk_info()
    print(f"Available Disk Space: {disk_info:.2f} GB" if not isinstance(disk_info, str) else disk_info)
    print(f"Current User: {get_current_user()}")
    print(f"IP Address: {get_ip_address()}")
    system_uptime = get_system_uptime()
    print(f"System Uptime: {int(system_uptime)} seconds" if not isinstance(system_uptime, str) else system_uptime)
    cpu_usage = get_cpu_usage()
    print(f"CPU Usage: {cpu_usage}%" if not isinstance(cpu_usage, str) else cpu_usage)
    print(f"System Architecture: {platform.architecture()[0]}")
    # Running processes
    print("\nRunning Processes:")
    for pid, name, memory_usage in get_running_processes_info():
        print(f"PID: {pid}, Name: {name}, Memory Usage: {memory_usage}")
    # Disk partitions
    print("\nDisk Partitions:")
    for device, mountpoint in get_disk_partitions_info():
        print(f"Device: {device}, Mountpoint: {mountpoint}")
    # Environment variables
    print("\nEnvironment Variables:")
    for key in list(os.environ.keys())[:10]:  # Showing only the first 10 for brevity
        print(f"{key}: {os.environ[key]}")

# The main function that runs the program.
if __name__ == "__main__":
    display_system_info()
