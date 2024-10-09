import random

def get_motivational_tip():
    tips = [
        "You are unstoppable!",
        "Every step is progress!",
        "Your strength is inspiring!",
        "Stay focused and stay fit!",
        "You’ve got this, warrior!"
    ]
    return random.choice(tips)

# Example usage
tip = get_motivational_tip()
print("Motivational Tip:", tip)
