import platform, psutil, socket, time, getpass, os
import matplotlib.pyplot as plt
from datetime import datetime


def get_cpu_usage():
    """Retrieve the current CPU usage as a percentage."""
    try:
        return psutil.cpu_percent(interval=1)
    except Exception as e:
        return None


def get_memory_usage():
    """Retrieve the memory usage of each process."""
    processes = [psutil.Process(pid) for pid in psutil.pids()]
    memory_usage = {}
    for proc in processes:
        try:
            name = proc.name()
            memory = proc.memory_info().rss / (1024 ** 2)  # Convert bytes to MB
            if name in memory_usage:
                memory_usage[name] += memory
            else:
                memory_usage[name] = memory
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return memory_usage


def get_disk_info():
    """Retrieve the available disk space in gigabytes."""
    try:
        disk_usage_gb = psutil.disk_usage('/').free / (1024 ** 3)
        return disk_usage_gb
    except Exception:
        return None


def collect_data(duration_minutes=10):
    end_time = time.time() + 60 * duration_minutes
    data = {'time': [], 'cpu_usage': [], 'disk_space': []}
    memory_usage_over_time = []

    while time.time() < end_time:
        current_time = datetime.now().strftime('%H:%M:%S')
        cpu_usage = get_cpu_usage()
        disk_space = get_disk_info()
        memory_usage = get_memory_usage()

        data['time'].append(current_time)
        data['cpu_usage'].append(cpu_usage)
        data['disk_space'].append(disk_space)
        memory_usage_over_time.append(memory_usage)

        print(f"Time: {current_time}, CPU Usage: {cpu_usage}%, Disk Space: {disk_space} GB")

        time.sleep(60)  # Sleep for a minute

    return data, memory_usage_over_time


def analyze_data(data, memory_usage_over_time):
    plt.figure(figsize=(10, 5))
    plt.plot(data['time'], data['cpu_usage'], marker='o', label='CPU Usage (%)')
    plt.xticks(rotation=45)
    plt.title('CPU Usage Over Time')
    plt.xlabel('Time')
    plt.ylabel('CPU Usage (%)')
    plt.legend()
    plt.show()

    plt.figure(figsize=(10, 5))
    plt.plot(data['time'], data['disk_space'], marker='o', color='r', label='Disk Space (GB)')
    plt.xticks(rotation=45)
    plt.title('Available Disk Space Over Time')
    plt.xlabel('Time')
    plt.ylabel('Disk Space (GB)')
    plt.legend()
    plt.show()

    avg_memory_usage = {}
    for snapshot in memory_usage_over_time:
        for process, memory in snapshot.items():
            if process in avg_memory_usage:
                avg_memory_usage[process].append(memory)
            else:
                avg_memory_usage[process] = [memory]
    avg_memory_usage = {proc: sum(mem) / len(mem) for proc, mem in avg_memory_usage.items()}

    max_process = max(avg_memory_usage, key=avg_memory_usage.get)
    max_avg_memory = avg_memory_usage[max_process]

    print(
        f"The process '{max_process}' uses the most memory on average, with an average usage of {max_avg_memory:.2f} MB")


if __name__ == "__main__":
    data, memory_usage_over_time = collect_data(duration_minutes=10)
    analyze_data(data, memory_usage_over_time)
