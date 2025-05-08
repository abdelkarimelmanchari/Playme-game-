import random

# Game Title
print("=== Welcome to the Ultimate Quiz Game! ===\n")
print("This game is a fun way to test your knowledge and learn new deepest secrets.\n")

# List of questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "answers": ["Paris", "London", "Berlin", "Madrid"],
        "correct": 0
    },
    {
        "question": "What is the largest planet in our solar system?",
        "answers": ["Earth", "Mars", "Jupiter", "Saturn"],
        "correct": 2
    },
    {
        "question": "What is the square root of 144?",
        "answers": ["10", "12", "16", "18"],
        "correct": 1
    },
    {
        "question": "What is the capital of France?",
        "answers": ["Paris", "London", "Berlin", "Madrid"],
        "correct": 0
    },
    {
        "question": "What is the largest planet in our solar system?",
        "answers": ["Earth", "Mars", "Jupiter", "Saturn"],
        "correct": 2
    },
    {
        "question": "What is the square root of 144?",
        "answers": ["10", "12", "16", "18"],
        "correct": 1
    },
    {
        "question": "What is the capital of Italy?",
        "answers": ["Venice", "Rome", "Milan", "Naples"],
        "correct": 1
    },
    {
        "question": "What gas do plants absorb from the atmosphere?",
        "answers": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
        "correct": 1
    },
    {
        "question": "How many continents are there on Earth?",
        "answers": ["5", "6", "7", "8"],
        "correct": 2
    },
    {
        "question": "What is the chemical symbol for Gold?",
        "answers": ["Au", "Ag", "Go", "Gd"],
        "correct": 0
    },
    {
        "question": "Which country is known as the Land of the Rising Sun?",
        "answers": ["China", "South Korea", "Japan", "Thailand"],
        "correct": 2
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "answers": ["Charles Dickens", "William Shakespeare", "Mark Twain", "Leo Tolstoy"],
        "correct": 1
    },
    {
        "question": "Which planet is closest to the Sun?",
        "answers": ["Earth", "Mercury", "Venus", "Mars"],
        "correct": 1
    },
    {
        "question": "What is the boiling point of water in Celsius?",
        "answers": ["90", "95", "100", "110"],
        "correct": 2
    },
    {
        "question": "Who painted the Mona Lisa?",
        "answers": ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Michelangelo"],
        "correct": 1
    },
    {
        "question": "How many sides does a hexagon have?",
        "answers": ["5", "6", "7", "8"],
        "correct": 1
    },
    {
        "question": "What is the capital of Canada?",
        "answers": ["Toronto", "Montreal", "Ottawa", "Vancouver"],
        "correct": 2
    },
    {
        "question": "What is H2O commonly known as?",
        "answers": ["Oxygen", "Hydrogen", "Water", "Salt"],
        "correct": 2
    },
    {
        "question": "Which ocean is the largest?",
        "answers": ["Atlantic", "Indian", "Arctic", "Pacific"],
        "correct": 3
    },
    {
        "question": "What is the smallest prime number?",
        "answers": ["0", "1", "2", "3"],
        "correct": 2
    },
    {
        "question": "What is the freezing point of water in Celsius?",
        "answers": ["0", "10", "32", "-5"],
        "correct": 0
    },
    {
        "question": "What is the capital of Germany?",
        "answers": ["Munich", "Frankfurt", "Berlin", "Hamburg"],
        "correct": 2
    },
    {
        "question": "What is the currency of Japan?",
        "answers": ["Won", "Yen", "Dollar", "Ruble"],
        "correct": 1
    },
    {
        "question": "Which organ pumps blood through the body?",
        "answers": ["Lungs", "Brain", "Heart", "Liver"],
        "correct": 2
    },
    {
        "question": "What is the largest mammal?",
        "answers": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
        "correct": 1
    },
    {
        "question": "What is 9 x 8?",
        "answers": ["72", "81", "64", "88"],
        "correct": 0
    },
    {
        "question": "Which planet is known for its rings?",
        "answers": ["Uranus", "Mars", "Saturn", "Neptune"],
        "correct": 2
    },
    {
        "question": "What language is spoken in Brazil?",
        "answers": ["Spanish", "Portuguese", "French", "English"],
        "correct": 1
    },
    {
        "question": "What is the capital of Egypt?",
        "answers": ["Cairo", "Luxor", "Alexandria", "Giza"],
        "correct": 0
    },
    {
        "question": "Who discovered gravity?",
        "answers": ["Albert Einstein", "Galileo", "Isaac Newton", "Nikola Tesla"],
        "correct": 2
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "answers": ["Mars", "Venus", "Mercury", "Saturn"],
        "correct": 0
    },
    {
        "question": "How many legs does a spider have?",
        "answers": ["6", "8", "10", "12"],
        "correct": 1
    },
    {
        "question": "What is the capital of Australia?",
        "answers": ["Sydney", "Melbourne", "Perth", "Canberra"],
        "correct": 3
    },
    {
        "question": "What does DNA stand for?",
        "answers": ["Deoxyribonucleic Acid", "Digital Network Access", "Data Node Array", "Dynamic Natural Architecture"],
        "correct": 0
    },
    {
        "question": "What is the hardest natural substance?",
        "answers": ["Gold", "Iron", "Diamond", "Steel"],
        "correct": 2
    },
    {
        "question": "Which country is home to the Eiffel Tower?",
        "answers": ["Germany", "Italy", "France", "Belgium"],
        "correct": 2
    },
    {
        "question": "How many hours are there in a day?",
        "answers": ["12", "24", "36", "48"],
        "correct": 1
    },
    {
        "question": "What is the process of water turning into vapor called?",
        "answers": ["Condensation", "Melting", "Evaporation", "Freezing"],
        "correct": 2
    },
    {
        "question": "What is the capital of Spain?",
        "answers": ["Barcelona", "Madrid", "Valencia", "Seville"],
        "correct": 1
    },
    {
        "question": "Which continent is the Sahara Desert located in?",
        "answers": ["Asia", "South America", "Africa", "Australia"],
        "correct": 2
    },
    {
        "question": "What is the square root of 81?",
        "answers": ["7", "8", "9", "10"],
        "correct": 2
    },
    {
        "question": "Who was the first man on the Moon?",
        "answers": ["Buzz Aldrin", "Neil Armstrong", "Yuri Gagarin", "John Glenn"],
        "correct": 1
    },
    {
        "question": "Which country invented pizza?",
        "answers": ["Spain", "Italy", "Greece", "France"],
        "correct": 1
    },
    {
        "question": "What is the color of chlorophyll?",
        "answers": ["Blue", "Yellow", "Green", "Red"],
        "correct": 2
    },
    {
        "question": "How many bones are in the human body?",
        "answers": ["206", "210", "198", "214"],
        "correct": 0
    },
    {
        "question": "What is the capital of the United Kingdom?",
        "answers": ["Edinburgh", "Manchester", "London", "Birmingham"],
        "correct": 2
    },
    {
        "question": "Which element has the atomic number 1?",
        "answers": ["Oxygen", "Nitrogen", "Hydrogen", "Helium"],
        "correct": 2
    },
    {
        "question": "Which famous scientist developed the theory of relativity?",
        "answers": ["Isaac Newton", "Stephen Hawking", "Albert Einstein", "Marie Curie"],
        "correct": 2
    },
    {
        "question": "What is 15 divided by 3?",
        "answers": ["3", "4", "5", "6"],
        "correct": 2
    },
    {
        "question": "Which planet has the most moons?",
        "answers": ["Saturn", "Jupiter", "Mars", "Uranus"],
        "correct": 0
    },
    {
        "question": "Which animal is the largest land mammal?",
        "answers": ["Elephant", "Giraffe", "Rhinoceros", "Hippo"],
        "correct": 0
    },
    {
        "question": "What is the capital of the United States?",
        "answers": ["New York", "Washington D.C.", "Los Angeles", "Chicago"],
        "correct": 1
    }
]

# List of deepest secrets 
deepest_secrets = [
    "You are made of stardust—almost every atom in your body was formed in a dying star.",
    "The universe has no center—it expands equally in all directions.",
    "Dark matter and dark energy make up about 95% of the universe, yet we know almost nothing about them.",
    "The observable universe is 93 billion light-years wide, but the actual universe may be infinite.",
    "A teaspoon of a neutron star would weigh around 6 billion tons.",
    "Time moves slower in stronger gravity—this is why time moves slightly slower on Earth than on satellites.",
    "The moon is slowly drifting away from Earth at about 3.8 cm per year.",
    "There are more stars in the universe than grains of sand on all Earth’s beaches.",
    "Black holes can evaporate over trillions of years via Hawking radiation.",
    "Quantum particles can exist in two places at once (superposition), but collapse into one state when observed.",
    "Your brain generates enough electricity to power a small lightbulb.",
    "Memories are reconstructed, not replayed—each recall slightly alters them.",
    "Most of your decisions are made subconsciously before you're aware of them.",
    "The gut has its own 'brain'—the enteric nervous system—with over 100 million neurons.",
    "Meditation can physically rewire the brain through neuroplasticity.",
    "Trauma can be inherited genetically through epigenetic changes.",
    "The placebo effect is real—belief alone can activate healing in the brain.",
    "You never see the world directly—your brain recreates it based on signals.",
    "Your brain can’t feel pain—it has no pain receptors.",
    "During REM sleep, your body is paralyzed to prevent you from acting out dreams.",
    "All life on Earth shares a common ancestor.",
    "Octopuses have three hearts and blue blood.",
    "You shed about 500 million skin cells every day.",
    "Trees can communicate with each other through underground fungi networks.",
    "Bacteria in your body outnumber your human cells 10 to 1.",
    "Some jellyfish can biologically revert to earlier life stages—potentially making them immortal.",
    "Your body replaces its cells constantly—your skin is about a month old.",
    "Mitochondria in your cells were once free-living bacteria.",
    "There’s more genetic diversity in one spoonful of soil than in all mammals combined.",
    "Sleep is essential for memory consolidation and waste removal in the brain.",
    "Energy cannot be created or destroyed—only transformed.",
    "Time may not be fundamental—it could be an emergent property of quantum entanglement.",
    "Free will is debated—many neuroscientists believe it may be an illusion.",
    "Reality may be a simulation—serious scientists have published on this theory.",
    "The universe doesn’t care about humans—we give meaning to it.",
    "Your body is constantly dying and regenerating—it’s more a process than a fixed object.",
    "Light behaves as both a particle and a wave depending on observation.",
    "You can’t observe something without changing it—this is the observer effect.",
    "The laws of physics might differ in other parts of the multiverse (if it exists).",
    "Most of the universe is empty space—even atoms are 99.999999999% empty.",
    "Success depends more on consistency than talent.",
    "Most fears are learned, not real.",
    "You can’t control others—only your response to them.",
    "Simplicity is often the highest form of intelligence.",
    "True freedom is mental—not external.",
    "You become what you repeatedly do.",
    "Comparison is the thief of joy.",
    "Gratitude rewires your brain for happiness.",
    "People don’t resist change—they resist being changed.",
    "Death gives meaning to life—it reminds us to live fully.",
    # Add more life hacks here...
]

def display_question(question):
    """
    Displays a multiple-choice question and prompts the user for an answer.
    """
    print(question["question"])
    for i, answer in enumerate(question["answers"]):
        print(f"{i+1}. {answer}")
    user_answer = int(input("Enter your answer (1-4): "))
    return user_answer - 1

def check_answer(question, user_answer):
    """
    Checks if the user's answer is correct and provides feedback.
    """
    if user_answer == question["correct"]:
        print("Correct! Here's a secret for you:")
        print(random.choice(deepest_secrets))
        return True
    else:
        print("Incorrect. Try again.")
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer - 1 == question["correct"]:
            print("Correct! Here's a secret for you:")
            print(random.choice(deepest_secrets))
            return True
        else:
            print(":(")
            return False

def play_game():
    """
    Runs the quiz-style game.
    """
    score = 0
    while True:
        question = random.choice(questions)
        user_answer = display_question(question)
        if check_answer(question, user_answer):
            score += 1
        else:
            print("Game over. Would you like to play again? (yes/no)")
            if input().lower() != "yes":
                break
    print(f"Your final score is {score} out of {len(questions)}.")

if __name__ == "__main__":
    play_game()