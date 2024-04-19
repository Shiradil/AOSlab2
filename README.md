# System Resource Monitor

## Overview
This Python script is designed to monitor and analyze system resource usage over time. It collects data on CPU usage, memory usage by each process, and available disk space, storing this data for later analysis. The script plots the CPU usage and disk space over time, helping identify trends and peak usage periods.

## Data Collection
The script runs a loop, collecting system parameters every minute. It records the following:
- CPU usage as a percentage
- Memory usage by each process
- Available disk space in gigabytes

The data is stored in an internal data structure for the duration of the monitoring period.

## Data Analysis
After collecting data for a defined period (configurable by the user), the script performs the following analysis:
- CPU usage variation over time
- Process with the highest average memory usage
- Disk space availability trend

## Questions and Answers

### How does the CPU usage vary over time? Is there a specific time when the CPU usage peaks?
The CPU usage varies depending on system activity. The script records CPU usage percentage at one-minute intervals. To determine if there is a specific time when CPU usage peaks, the script plots the CPU usage over the collection period. The time of peak CPU usage can be observed on the generated graph.

### Which process uses the most memory on average?
The script collects memory usage of each process every minute. It calculates the average memory usage of each process over the monitoring period. The process that uses the most memory on average is identified and printed in the console output.

### How does the available disk space change over time?
Similar to CPU usage, the script monitors the available disk space at one-minute intervals. The trend of available disk space over time is plotted on a graph. Any significant changes or trends can be observed, allowing for an assessment of disk space usage.

## Result Presentation
The results are presented in two ways:
1. Console Output: Immediate printout of the collected data at each interval.
2. Graphs: Using the `matplotlib` library, the script generates graphs for visualizing CPU usage and available disk space over time.

## Usage
To run the script, ensure you have Python and the required libraries (`psutil` and `matplotlib`) installed. Run the script from the command line or an IDE. The monitoring period can be adjusted in the `collect_data` function.

