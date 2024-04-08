# OS Parameters Display Tool
Project created by Astana IT Student - Shirbayev Adilzhan from SE-2204 group.<br>
This Python script retrieves and displays essential parameters of the operating system, including OS name and version, processor information, total memory, available disk space, current user, IP address, system uptime, CPU usage, and more.

## Features
<ul>
<li>Retrieve OS name and version. There might be a problem if you are using Windows 11, it would print that you are using 10th windows because Windows 11 and Windows 10 share a substantial amount of their codebase and, to a large extent, are treated by Microsoft as different versions/builds of the same core OS. </li>
<li>Display processor information.</li>
<li>Show total system memory.</li>
<li>List available disk space.</li>
<li>Identify the current user.</li>
<li>Display the system's IP address.</li>
<li>Show system uptime.</li>
<li>Display current CPU usage.</li>
<li>Summarize running processes.</li>
<li>Provide disk partitions information.</li>
<li>Display system architecture.</li>
<li>List environment variables. </li>
</ul>

## Dependencies
<ul>
<li>Python 3.6 or newer</li>
<li>psutil</li>
</ul>

To install psutil run the command ```pip install psutil``` in the terminal

## How to run
<ol>
<li>Clone this repository to your local machine using Git.</li>
<li>Open a terminal and navigate to the directory where you cloned this repository.</li>
<li>Run the script with the following command: </li>
</ol>

```python os_parameters.py```

