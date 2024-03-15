from datetime import datetime
import pytz

def convert_time_lisbon_to_nepal(lisbon_time_str):
    # Define time zones
    lisbon_tz = pytz.timezone('Europe/Lisbon')
    nepal_tz = pytz.timezone('Asia/Kathmandu')

    # Convert string to datetime object
    lisbon_time = datetime.strptime(lisbon_time_str, '%Y-%m-%d %H:%M')

    # Set the time zone for Lisbon
    lisbon_time = lisbon_tz.localize(lisbon_time)

    # Convert to Nepal time
    nepal_time = lisbon_time.astimezone(nepal_tz)

    return nepal_time.strftime('%Y-%m-%d %H:%M %Z%z')

if __name__ == "__main__":
    lisbon_time_str = '2024-03-13 03:10'
    nepal_time = convert_time_lisbon_to_nepal(lisbon_time_str)
    print("Given time in Lisbon:", lisbon_time_str)
    print("Converted time in Nepal (Kathmandu):", nepal_time)
