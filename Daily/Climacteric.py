import datetime
import math

# Emotion check function
def check_emotion():
    print("Please enter your emotion for today:")
    print("1. Happy")
    print("2. Stressed")
    print("3. Anxious")
    print("4. Tired")
    print("5. Calm")
    
    emotion_input = input("Enter the number corresponding to your emotion: ")
    
    emotions = {
        "1": "Happy",
        "2": "Stressed",
        "3": "Anxious",
        "4": "Tired",
        "5": "Calm"
    }
    
    emotion = emotions.get(emotion_input, "Unknown")
    print(f"Today's emotion: {emotion}")
    return emotion

# Biorhythm calculation function
def calculate_biorhythm(birth_date, check_date):
    physical_cycle = 23
    emotional_cycle = 28
    intellectual_cycle = 33

    birth_date = datetime.datetime.strptime(birth_date, "%Y-%m-%d")
    check_date = datetime.datetime.strptime(check_date, "%Y-%m-%d")
    days_lived = (check_date - birth_date).days

    physical = math.sin(2 * math.pi * days_lived / physical_cycle)
    emotional = math.sin(2 * math.pi * days_lived / emotional_cycle)
    intellectual = math.sin(2 * math.pi * days_lived / intellectual_cycle)

    return physical, emotional, intellectual

# Positive message function
def provide_positive_message(emotion):
    messages = {
        "Happy": "Enjoy your happiness today! Share your joy with others.",
        "Stressed": "It seems you're feeling stressed. Take a deep breath and try to relax.",
        "Anxious": "Feeling anxious? A short walk might help clear your mind.",
        "Tired": "You seem tired. Make sure to get some rest and maybe enjoy a warm cup of tea.",
        "Calm": "You're feeling calm. Take this time to enjoy the peaceful moment!"
    }
    
    print(messages.get(emotion, "Keep going, you're doing great!"))

# Save emotion data to file
def save_emotion_data(emotion, date):
    with open("emotion_data.txt", "a") as file:
        file.write(f"{date}, {emotion}\n")
    print("Emotion data has been saved.")

# Main program execution
if __name__ == "__main__":
    birth_date = input("Please enter your birth date (YYYY-MM-DD): ")
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    
    emotion = check_emotion()
    save_emotion_data(emotion, today)
    
    physical, emotional, intellectual = calculate_biorhythm(birth_date, today)
    print(f"Today's Biorhythm:")
    print(f"Physical: {physical:.2f}")
    print(f"Emotional: {emotional:.2f}")
    print(f"Intellectual: {intellectual:.2f}")
    
    provide_positive_message(emotion)
