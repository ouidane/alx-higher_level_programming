#!/usr/bin/python3
"""Define a stats function"""
import sys
import signal


# Initialize variables to store metrics
total_file_size = 0
status_code_count = {}


# Define a function to handle CTRL + C interruption
def handle_interrupt(signum, frame):
    """
    Handle CTRL + C interruption.
    Print metrics and exit gracefully.

    Args:
        signum (int): Signal number (SIGINT).
        frame: Current execution frame.
    """
    print_metrics()
    sys.exit(0)


# Register the CTRL + C signal handler
signal.signal(signal.SIGINT, handle_interrupt)


def parse_line(line):
    """
    Parse a line of input and extract file size and status code.

    Args:
        line (str): Input line in the specified format.

    Returns:
        tuple: A tuple containing file size (int) and status code (str).
    """
    try:
        parts = line.split()
        file_size = int(parts[-1])
        status_code = parts[-2]

        return file_size, status_code
    except (ValueError, IndexError):
        return None, None


def print_metrics():
    """
    Print the computed metrics, including total file size
    and status code counts
    """
    print("Total file size:", total_file_size)
    for status_code in sorted(status_code_count):
        print(f"{status_code}: {status_code_count[status_code]}")


line_counter = 0


try:
    for line in sys.stdin:
        file_size, status_code = parse_line(line)
        if file_size is not None and status_code is not None:
            total_file_size += file_size
            status_code_count[status_code] =
            status_code_count.get(status_code, 0) + 1
        line_counter += 1

        if line_counter % 10 == 0:
            print_metrics()

except KeyboardInterrupt:
    print_metrics()
