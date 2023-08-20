#Visual Moodboard Selection - Displaying Moodboard Themes
def display_moodboards(themes):
    print("Welcome to Moodboard Selection!")
    
    # Display available moodboard themes
    print("Choose from the following themes:")
    for i, theme in enumerate(themes):
        print(f"{i+1}. {theme}")
    
    # Prompt user to select a theme
    while True:
        try:
            user_choice = int(input("Q1. Select a theme by entering its corresponding number: "))
            
            if 1 <= user_choice <= len(themes):
                selected_theme = themes[user_choice - 1]
                print(f"You've selected the '{selected_theme}' theme.")
                break
            else:
                print("Please enter a valid theme number.")
                
        except ValueError:
            print("Please enter a valid number.")
    
    print("Thank you for selecting a theme!")
    return selected_theme

# List of available themes
themes = ["Casual", "Formal", "Boho", "Sporty"]

# Call the function to display moodboards and get the selected theme
selected_theme = display_moodboards(themes)
