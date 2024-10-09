def get_nutritional_advice(user_profile):
    # Simple example; ideally, this should be more detailed
    advice = {
        "weight_loss": "Focus on high protein, low carb meals.",
        "muscle_gain": "Increase protein intake and eat balanced meals.",
        "general_wellness": "Eat a variety of fruits and vegetables, and stay hydrated."
    }
    return advice[user_profile['goals']]

# Example usage
with open('data/user_profiles.json', 'r') as file:
    user_profile = json.load(file)[0]  # Assuming the first user profile

advice = get_nutritional_advice(user_profile)
print("Nutritional Advice:", advice)
