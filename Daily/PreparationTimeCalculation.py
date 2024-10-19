from math import radians, sin, cos, sqrt, atan2
from datetime import datetime, timedelta

def get_preparation_input():
    """
    Collect user input for preparation tasks and return the total preparation time.
    
    Returns:
    int: Total preparation time in minutes.
    """
    shower_time = int(input("Enter shower time (in minutes): "))
    makeup_time = int(input("Enter makeup time (in minutes): "))
    hair_time = int(input("Enter hair styling time (in minutes): "))
    outfit_time = int(input("Enter time to choose an outfit (in minutes): "))
    travel_time = int(input("Enter travel time (in minutes): "))
    buffer_time = int(input("Enter buffer time (in minutes): "))
    
    # Calculate total preparation time
    total_time = shower_time + makeup_time + hair_time + outfit_time + travel_time + buffer_time
    return total_time

def avoid_lateness(meeting_time_str, preparation_time_minutes):
    """
    Calculate the latest time to start preparing for the event to avoid being late.
    
    Parameters:
    meeting_time_str (str): The time of the meeting in 'HH:MM' format (24-hour format).
    preparation_time_minutes (int): The total preparation time in minutes.
    
    Returns:
    str: The latest time to start preparation to avoid being late.
    """
    # Convert the meeting time string to a datetime object
    meeting_time = datetime.strptime(meeting_time_str, '%H:%M')
    
    # Subtract the preparation time (in minutes) from the meeting time
    start_time = meeting_time - timedelta(minutes=preparation_time_minutes)
    
    # Return the time to start getting ready as a formatted string
    return start_time.strftime('%H:%M')

def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great-circle distance between two points on the Earth using the Haversine formula.
    Input coordinates should be in decimal degrees.
    
    Parameters:
    lat1, lon1: Latitude and Longitude of the current location.
    lat2, lon2: Latitude and Longitude of the destination location (e.g., meeting point).
    
    Returns:
    float: Distance between the two points in kilometers.
    """
    # Radius of the Earth in kilometers
    R = 6371.0
    
    # Convert latitude and longitude from degrees to radians
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)
    
    # Difference in coordinates
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    
    # Haversine formula
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    
    # Distance in kilometers
    distance = R * c
    return distance

# Example usage for input
meeting_time_str = input("Enter meeting time (HH:MM, 24-hour format): ")  # User will input meeting time

# Get preparation time using user input
preparation_time_minutes = get_preparation_input()

# Calculate the time to start preparation
start_preparation_time = avoid_lateness(meeting_time_str, preparation_time_minutes)

# User inputs for location
current_lat = float(input("Enter your current latitude: "))
current_lon = float(input("Enter your current longitude: "))
meeting_lat = float(input("Enter meeting place latitude: "))
meeting_lon = float(input("Enter meeting place longitude: "))

# Calculate the distance to the meeting place
distance_to_meeting = haversine(current_lat, current_lon, meeting_lat, meeting_lon)

print(f"Start preparing by: {start_preparation_time}")
print(f"The distance to the meeting place is: {distance_to_meeting:.2f} km")
