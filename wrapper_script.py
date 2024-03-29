import time
import subprocess

# Define application script path and flag file path
app_script_path = "socket_connection/handler.py"
flag_file_path = "data_received.txt" 

while True:
    # Execute the application script
    subprocess.run(["python", app_script_path])

    # Check for the flag file every 1 second (adjust as needed)
    while os.path.exists(flag_file_path):
        time.sleep(1)

        received_filename = os.path.basename(flag_file_path)  # Get the filename

        # Execute the data processing script after processing is finished
        subprocess.run(["python", "atm_data_seeder.py", received_filename])  

        # Delete the flag file
        os.remove(flag_file_path)
        print("Data processed and flag file removed.")

    # Wait for some time before checking again
    time.sleep(5)
