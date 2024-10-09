from scripts.generate_wellness_plan import generate_wellness_plan
from scripts.track_progress import track_progress
from scripts.nutritional_advice import get_nutritional_advice
from scripts.motivational_tips import get_motivational_tip

def main():
    user_id = 1
    # Load user profile (for demo purposes)
    with open('data/user_profiles.json', 'r') as file:
        user_profiles = json.load(file)
    user_profile = user_profiles[0]  # Assuming the first user profile

    # Generate wellness plan
    wellness_plan = generate_wellness_plan(user_profile)
    print("Your personalized wellness plan:", wellness_plan)

    # Track progress (for demo purposes)
    progress_data = {
        'date': str(datetime.date.today()),
        'workout_completed': True,
        'notes': 'Feeling empowered after the workout!'
    }
    track_progress(user_id, progress_data)

    # Get nutritional advice
    advice = get_nutritional_advice(user_profile)
    print("Nutritional Advice:", advice)

    # Get motivational tip
    tip = get_motivational_tip()
    print("Motivational Tip:", tip)

if __name__ == "__main__":
    main()
