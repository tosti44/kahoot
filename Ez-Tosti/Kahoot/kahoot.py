import json
import urllib.request
import pyautogui
import time
import keyboard

# Define the screen coordinates for each color button
# Replace these coordinates with the actual positions on your screen
color_coordinates = {
    'Red': (327, 594),    # Example coordinates
    'Blue': (973, 581),   # Example coordinates
    'Yellow': (282, 660), # Example coordinates
    'Green': (1068, 658)   # Example coordinates
}

# Function to fetch quiz answers from Kahoot
def fetch_quiz_answers(quiz_id):
    api = 'https://play.kahoot.it/rest/kahoots/'
    link = api + quiz_id
    answers = {}

    try:
        with urllib.request.urlopen(link) as url:
            data = json.load(url)
            for question_index, question_data in enumerate(data['questions']):
                if question_data['type'] == "quiz":
                    choices = question_data.get('choices', [])
                    for idx, choice in enumerate(choices):
                        if choice.get('correct', False):
                            color = ['Red', 'Blue', 'Yellow', 'Green'][idx]
                            answers[f"Question {question_index + 1}"] = color
                            break
    except Exception as err:
        print("There was an error! It could be because the quiz id is incorrect.\n")
        print(err)

    return answers

# Function to simulate mouse clicks based on colors
def click_color(color):
    if color in color_coordinates:
        x, y = color_coordinates[color]
        pyautogui.click(x, y)
        time.sleep(1)  # Add a small delay between clicks

# Main function
if __name__ == "__main__":
    quiz_id = input("Quiz ID = ")
    answers = fetch_quiz_answers(quiz_id)
    print(f"Answers: {answers}")

    answer_iterator = iter(answers.values())
    
    print("Press 'n' to input the next answer.")
    while True:
        if keyboard.is_pressed('n'):
            try:
                color = next(answer_iterator)
                print(f"Inputting color: {color}")
                click_color(color)
                time.sleep(0.5)  # Debounce to prevent multiple inputs
            except StopIteration:
                print("No more answers.")
                break
