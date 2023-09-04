#Q-1 using function to create txt file eith current time stamp
from datetime import datetime

def date_time():
    # Get the current timestamp
    current_time = datetime.now()

    # Format the timestamp as a string
    time_stamp = current_time.strftime("%Y-%m-%d %H:%M:%S")

    # Create and write to the text file
    with open("timestamp.txt", mode="w") as file:
        file.write(time_stamp)

    print("Timestamp written to 'timestamp.txt' file.")

date_time()


#Q-2 read the file display the content on console
def timestamp():
    fi = "timestamp.txt"
    with open(fi, mode = "r") as file:
        content = file.read()
        print("file content:", content)
timestamp()


