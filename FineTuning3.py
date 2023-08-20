#Fine Tuning Outfit Recommendations - Interactive User Feedback Loop
def refine_outfit_recommendations(current_outfit):
    print("Welcome to Outfit Refinement!")
    print("Here's the initial outfit recommendation:", current_outfit)
    
    while True:
        user_feedback = input("Q1. How do you like this outfit? Type 'better' if you want a new one, or 'done' if you're satisfied: ")
        
        if user_feedback.lower() == "better":
            current_outfit = generate_new_outfit()  # Your function to generate a new outfit
            print("Here's a new outfit recommendation:", current_outfit)
            
        elif user_feedback.lower() == "done":
            print("Great choice! Your final outfit recommendation:", current_outfit)
            break
            
        else:
            print("Please enter 'better' or 'done'.")
    
    return current_outfit

# Call the function to refine outfit recommendations
initial_outfit = generate_initial_outfit()  # Your function to generate an initial outfit
final_outfit = refine_outfit_recommendations(initial_outfit)
