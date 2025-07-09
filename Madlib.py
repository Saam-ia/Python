def words():
    nouns= [input(f"Enter noun #{i+1}: " ) for i in range (2)]
    adjectives=[input(f"Enter adjective #{i+1}: ")for i in range (2)]
    verbs=[input(f"Enter noun #{i+1}: ")for i in range (2)]
    return nouns,adjectives,verbs

def story1(n,adj,v):
     return f"""
    Once upon a time, a {adj[0]} {n[0]} decided to {v[0]} in the forest.
    The weather was {adj[1]}, and the sky shimmered.
    As the {n[0]} moved forward, it heard something.
    It was the {n[1]}, making strange noises.
    Without hesitation, the {n[0]} started to {v[1]} quickly.
    The path was narrow, but the journey was thrilling.
    It turned out to be a truly unforgettable day.
    """
def story_2(n, adj, v):
    return f"""
    On a {adj[0]} morning, a {n[0]} went to the beach.
    The sand felt {adj[1]} under its feet.
    Suddenly, a wave brought a {n[1]} ashore.
    Curious, the {n[0]} began to {v[0]} toward it.
    The crowd gathered, everyone watching it {v[1]}.
    Excitement buzzed through the air like electricity.
    The day ended with laughter and warm sunlight.
    """

def story_3(n, adj, v):
    return f"""
    In a busy town, a {adj[0]} {n[0]} was late for work.
    It had to {v[0]} through the crowded streets.
    A {adj[1]} billboard caught its eye along the way.
    Just then, a {n[1]} appeared out of nowhere.
    The {n[0]} had to quickly {v[1]} to avoid it.
    Hearts were pounding, but disaster was averted.
    Another wild morning in the city had passed.
    """

def story_4(n, adj, v):
    return f"""
    Deep in a {adj[0]} cave, a {n[0]} prepared for an adventure.
    The silence was broken by a {adj[1]} noise.
    It echoed off the stone, making the {n[0]} nervous.
    From the shadows, a giant {n[1]} emerged.
    Without thinking, it began to {v[0]} away.
    Then, suddenly, it stopped and decided to {v[1]} instead.
    What a twist in the journey beneath the earth!
    """

def main():
    print("🎉 Welcome to Mad Libs!\nChoose a story:")
    print("1. Forest Adventure")
    print("2. Beach Mystery")
    print("3. City Chaos")
    print("4. Cave Quest")
    
    choice = input("Enter 1, 2, 3, or 4: ")
    nouns, adjectives, verbs = words()
    
    print("\n📝 Here's your story:\n")
    
    if choice == "1":
        print(story1(nouns, adjectives, verbs))
    elif choice == "2":
        print(story_2(nouns, adjectives, verbs))
    elif choice == "3":
        print(story_3(nouns, adjectives, verbs))
    elif choice == "4":
        print(story_4(nouns, adjectives, verbs))
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()

