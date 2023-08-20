#Preferences Gathering - Interactive Dialogue for User Input:
def collect_preferences():
    print("Welcome to the Preferences Gathering!")
    
    # Ask for user's preferred style
    user_style = input("Q1. What's your preferred style? (e.g., Casual, Formal, Boho): ")
    
    # Ask for user's favorite color
    user_color = input("Q2. What's your favorite color? ")
    
    # Ask for user's favorite clothing brands
    user_brands = input("Q3. Do you have any favorite clothing brands? (Separate with commas if multiple): ")
    
    print("Thank you for providing your preferences!")
    
    # Return the collected preferences as a tuple
    return user_style, user_color, user_brands

# Call the function to gather user preferences
user_style, user_color, user_brands = collect_preferences()

# Display the gathered preferences
print("Gathered Preferences:")
print("Preferred Style:", user_style)
print("Favorite Color:", user_color)
print("Favorite Brands:", user_brands)
