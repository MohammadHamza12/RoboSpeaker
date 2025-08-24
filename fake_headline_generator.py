import random

subjects = [
    "Shahrukh Khan",
    "Virat Kohli",
    "Nirmala Sitharaman",
    "A Mumbai Cat",
    "Salman Khan",
    "Auto Rickshaw driver from Delhi",
    "Prime Minister Modi"
]

actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates"
]

places_or_things = [
    "at Red Fort",
    "in Mumbai Local Train",
    "a Plate of Samosa",
    "inside Parliament",
    "at Ganga Ghat",
    "during IPL Match",
    "at India Gate"
]

while True:
    subject = random.choice(subjects)       # pick from list
    action = random.choice(actions)         # pick from list
    place_or_thing = random.choice(places_or_things)  # pick from list

    headline = f"BREAKING NEWS : {subject} {action} {place_or_thing}"
    print("\n" + headline)

    user_input = input("\nDo you want another headline? (yes/no): ").strip().lower()
    if user_input == "no":
        break

print("\nThanks for using the Fake Headline Generator. Have a fun day! 🎉")
