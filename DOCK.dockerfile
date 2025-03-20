FROM python:3.9

# Set the working directory
WORKDIR /scripts

# Copy the Python script into the container
COPY fetch_cpu_utilization.py .

# Install psutil
RUN pip install psutil

# Command to run the script
CMD ["python", "fetch_cpu_utilization.py"]