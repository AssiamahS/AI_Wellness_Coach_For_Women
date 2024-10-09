import json
import random

def load_wellness_plans():
    with open('data/wellness_plans.json', 'r') as file:
        return json.load(file)

def generate_wellness_plan(user_profile):
    wellness_plans = load_wellness_plans()
    user_goals = user_profile['goals']
    personalized_plan = random.choice(wellness_plans[user_goals])
    return personalized_plan

# Example usage
with open('data/user_profiles.json', 'r') as file:
    user_profile = json.load(file)[0]  # Assuming the first user profile for demo purposes

wellness_plan = generate_wellness_plan(user_profile)
print("Your personalized wellness plan:", wellness_plan)
