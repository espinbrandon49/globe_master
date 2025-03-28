import random
from classes import Question
from questions import *


def display_ascii_art():
    print(
        r"""
  ________ .__           ___.               _____                     __                   
 /  _____/ |  |    ____  \_ |__    ____    /     \  _____     _______/  |_   ____  _______ 
/   \  ___ |  |   /  _ \  | __ \ _/ __ \  /  \ /  \ \__  \   /  ___/\   __\_/ __ \ \_  __ \
\    \_\  \|  |__(  <_> ) | \_\ \\  ___/ /    Y    \ / __ \_ \___ \  |  |  \  ___/  |  | \/
 \______  /|____/ \____/  |___  / \___  >\____|__  /(____  //____  > |__|   \___  > |__|   
        \/                    \/      \/         \/      \/      \/             \/        
    """
    )


def create_player():
    title = "🌍 Test Your Global Genius! 🌍"
    rules = "Ready to prove you're a world whiz? Answer each question and see how far you go! (You can exit anytime to get your score and try again!)"
    display_ascii_art()
    print(title)
    print(rules)
    name = input("\nBefore we begin, tell us your name, future world champion! 🏆: ")
    return name


def display_menu():
    main_menu = (
        "\nWhat’s your move, explorer?\n"
        "1) Start the Adventure\n"
        "2) Choose a difficulty level\n"
        "3) Choose a category\n"
        "Q) Exit\n"
    )
    difficulty = "\nSelect your difficulty level:\n4) Easy: A gentle start\n5) Medium: A daring quest\n6) Hard: Only for the bold!\nQ) Exit\n"
    categories = (
        "\n7) Capitol Cities\n"
        "8) Famous Landmarks\n"
        "9) Country Flags\n"
        "10) Oceans and Seas\n"
        "11) Cultural Foods\n"
        "12) Animal Habitats\n"
        "13) Languages of the World\n"
        "14) Natural Wonders\n"
        "Q) Exit\n"
    )
    game_mode = ""
    while True:
        selection = input(f"{main_menu}").lower()
        if selection == "1" or selection == "2" or selection == "3":
            if selection == "1":
                game_mode = selection
            elif selection == "2":
                game_mode = input(difficulty)
            elif selection == "3":
                game_mode = input(categories)

            if game_mode == "q":
                return None
            else:
                return game_mode
        elif selection == "q":
            return None
        else:
            print("❓ That's not quite what we're looking for. Give it another go!")


def ask_question(game_mode):
    question = {}
    if game_mode == "1":
        question = random.choice(all_questions)
    elif game_mode == "4":
        question = random.choice(easy_questions)
    elif game_mode == "5":
        question = random.choice(intermediate_questions)
    elif game_mode == "6":
        question = random.choice(hard_questions)
    elif game_mode == "7":
        question = random.choice(capital_city_questions)
    elif game_mode == "8":
        question = random.choice(famous_landmarks)
    elif game_mode == "9":
        question = random.choice(country_flags)
    elif game_mode == "10":
        question = random.choice(oceans_and_seas)
    elif game_mode == "11":
        question = random.choice(cultural_foods)
    elif game_mode == "12":
        question = random.choice(animal_habitats)
    elif game_mode == "13":
        question = random.choice(languages_of_the_world)
    elif game_mode == "14":
        question = random.choice(natural_wonders)

    new_question = Question(
        list(question.keys())[0],
        list(question.values())[0].lower(),
    )

    ask = input("\n" + new_question.question + " ").lower()
    return new_question.validate(ask)


def display_scoreboard(player, badge_list):
    print(f"🎉 {player.name}'s Game Stats 🎉")
    print(f"🏆 Score: {player.score}")
    print(f"❓ Questions Asked: {player.questions_asked}")
    print(f"📊 Accuracy: {player.percentage()}%\n")
    print("Badges:")
    if len(badge_list) == 0:
        print("🚫 No badges yet. The journey continues!")
    else:
        for badge in badge_list:
            print(badge)


def continue_game(game_mode):
    while True:
        next = input(
            "\n🏆 Forge ahead, brave explorer!\n1) Next question awaits!\n2) Return to the main menu\n3) Conclude your quest and bask in your achievements!\n"
        )
        if next == "1":
            return game_mode
        if next == "2":
            displayMenu = display_menu()
            return displayMenu
        elif next == "3":
            print("\n🎉 Thanks for joining the adventure! 🎉")
            print("🌟 Your Final Score 🌟\n")
            return False
        else:
            print("❓ That's not quite what we're looking for. Give it another go!")


def award_badges(game_mode, category_points, badge_list):
    if game_mode in category_points:
        category_points[game_mode] += 1
    else:
        category_points[game_mode] = 1

    if category_points.get("4") == 2:
        if not "Easy: 🟢 Trailblazer - Starting the Journey" in badge_list:
            badge_list.append("Easy: 🟢 Trailblazer - Starting the Journey")
            print("BADGE EARNED")
            print("Easy: 🟢 Trailblazer - Starting the Journey\n")

    if category_points.get("5") == 2:
        if not "Medium: 🟠 Adventurer - Fearless Explorer" in badge_list:
            badge_list.append("Medium: 🟠 Adventurer - Fearless Explorer")
            print("BADGE EARNED")
            print("Medium: 🟠 Adventurer - Fearless Explorer\n")

    if category_points.get("6") == 2:
        if not "Hard: 🔴 Legend - Conqueror of Challenges" in badge_list:
            badge_list.append("Hard: 🔴 Legend - Conqueror of Challenges")
            print("BADGE EARNED")
            print("Hard: 🔴 Legend - Conqueror of Challenges")

    if category_points.get("7") == 2:
        if not "🌆 City Slicker - You know your way around the capitals!" in badge_list:
            badge_list.append(
                "🌆 City Slicker - You know your way around the capitals!"
            )
            print("BADGE EARNED")
            print("🌆 City Slicker - You know your way around the capitals!")

    if category_points.get("7") == 3:
        if (
            not "🗺️ Global Navigator - You’ve navigated capitals like a pro!"
            in badge_list
        ):
            badge_list.append(
                "🗺️ Global Navigator - You’ve navigated capitals like a pro!"
            )
            print("BADGE EARNED")
            print("🗺️ Global Navigator - You’ve navigated capitals like a pro!")

    if category_points.get("7") == 5:
        if (
            not "🏛️ Capital Conqueror - You’ve mastered the world's capitals!"
            in category_points
        ):
            badge_list.append(
                "🏛️ Capital Conqueror - You’ve mastered the world's capitals!"
            )
            print("BADGE EARNED")
            print("🏛️ Capital Conqueror - You’ve mastered the world's capitals!")

    if category_points.get("8") == 2:
        if not "🌉 Globe Trotter - Landmarks Expert" in badge_list:
            badge_list.append("🌉 Globe Trotter - Landmarks Expert")
            print("BADGE EARNED")
            print("🌉 Globe Trotter - Landmarks Expert")

    if category_points.get("8") == 4:
        if not "🏛️ History Buff - Keeper of Ancient Wonders" in badge_list:
            badge_list.append("🏛️ History Buff - Keeper of Ancient Wonders")
            print("BADGE EARNED")
            print("🏛️ History Buff - Keeper of Ancient Wonders")

    if category_points.get("8") == 6:
        if not "📸 Landmark Photographer - Seen the World's Icons" in badge_list:
            badge_list.append("📸 Landmark Photographer - Seen the World's Icons")
            print("BADGE EARNED")
            print("📸 Landmark Photographer - Seen the World's Icons")

    if category_points.get("9") == 2:
        if not "🎌 Flag Prodigy - Colors and Symbols Guru" in badge_list:
            badge_list.append("🎌 Flag Prodigy - Colors and Symbols Guru")
            print("BADGE EARNED")
            print("🎌 Flag Prodigy - Colors and Symbols Guru")

    if category_points.get("9") == 4:
        if not "🏴 Flag Master - Unmatched in National Pride" in badge_list:
            badge_list.append("🏴 Flag Master - Unmatched in National Pride")
            print("BADGE EARNED")
            print("🏴 Flag Master - Unmatched in National Pride")

    if category_points.get("9") == 6:
        if not "🚩 Worldly Observer - Flag Recognition Expert" in badge_list:
            badge_list.append("🚩 Worldly Observer - Flag Recognition Expert")
            print("BADGE EARNED")
            print("🚩 Worldly Observer - Flag Recognition Expert")

    if category_points.get("10") == 2:
        if not "🌊 Ocean Navigator - Explorer of Waters" in badge_list:
            badge_list.append("🌊 Ocean Navigator - Explorer of Waters")
            print("BADGE EARNED")
            print("🌊 Ocean Navigator - Explorer of Waters")

    if category_points.get("10") == 4:
        if not "⚓ Sea Sage - Master of the Seas" in badge_list:
            badge_list.append("⚓ Sea Sage - Master of the Seas")
            print("BADGE EARNED")
            print("⚓ Sea Sage - Master of the Seas")

    if category_points.get("10") == 6:
        if not "🐚 Marine Marvel - Knowledge of Deep Blue" in badge_list:
            badge_list.append("🐚 Marine Marvel - Knowledge of Deep Blue")
            print("BADGE EARNED")
            print("🐚 Marine Marvel - Knowledge of Deep Blue")

    if category_points.get("11") == 2:
        if not "🍕 Culinary Tourist - International Food Fan" in badge_list:
            badge_list.append("🍕 Culinary Tourist - International Food Fan")
            print("BADGE EARNED")
            print("🍕 Culinary Tourist - International Food Fan")

    if category_points.get("11") == 4:
        if not "🍜 World Taster - A Taste for Culture" in badge_list:
            badge_list.append("🍜 World Taster - A Taste for Culture")
            print("BADGE EARNED")
            print("🍜 World Taster - A Taste for Culture")

    if category_points.get("11") == 6:
        if not "🍱 Global Gourmet - Champion of World Flavors" in badge_list:
            badge_list.append("🍱 Global Gourmet - Champion of World Flavors")
            print("BADGE EARNED")
            print("🍱 Global Gourmet - Champion of World Flavors")

    if category_points.get("12") == 2:
        if not "🐾 Wildlife Enthusiast - Habitat Knowledge Master" in badge_list:
            badge_list.append("🐾 Wildlife Enthusiast - Habitat Knowledge Master")
            print("BADGE EARNED")
            print("🐾 Wildlife Enthusiast - Habitat Knowledge Master")

    if category_points.get("12") == 4:
        if not "🌳 Eco Explorer - Knower of Nature's Homes" in badge_list:
            badge_list.append("🌳 Eco Explorer - Knower of Nature's Homes")
            print("BADGE EARNED")
            print("🌳 Eco Explorer - Knower of Nature's Homes")

    if category_points.get("12") == 6:
        if not "🦁 Animal Tracker - Expert of Natural Habitats" in badge_list:
            badge_list.append("🦁 Animal Tracker - Expert of Natural Habitats")
            print("BADGE EARNED")
            print("🦁 Animal Tracker - Expert of Natural Habitats")

    if category_points.get("13") == 2:
        if not "🗣️ Linguistic Explorer - Multilingual Marvel" in badge_list:
            badge_list.append("🗣️ Linguistic Explorer - Multilingual Marvel")
            print("BADGE EARNED")
            print("🗣️ Linguistic Explorer - Multilingual Marvel")

    if category_points.get("13") == 4:
        if not "🌐 Language Sage - Champion of World Tongues" in badge_list:
            badge_list.append("🌐 Language Sage - Champion of World Tongues")
            print("BADGE EARNED")
            print("🌐 Language Sage - Champion of World Tongues")

    if category_points.get("3") == 6:
        if not "📖 Global Communicator - Polyglot in Training" in badge_list:
            badge_list.append("📖 Global Communicator - Polyglot in Training")
            print("BADGE EARNED")
            print("📖 Global Communicator - Polyglot in Training")

    if category_points.get("14") == 2:
        if not "⛰️ Wonder Seeker - Knower of Earth’s Treasures" in badge_list:
            badge_list.append("⛰️ Wonder Seeker - Knower of Earth’s Treasures")
            print("BADGE EARNED")
            print("⛰️ Wonder Seeker - Knower of Earth’s Treasures")

    if category_points.get("14") == 4:
        if not "🌍 Naturalist - Guardian of Earth's Marvels" in badge_list:
            badge_list.append("🌍 Naturalist - Guardian of Earth's Marvels")
            print("BADGE EARNED")
            print("🌍 Naturalist - Guardian of Earth's Marvels")

    if category_points.get("14") == 6:
        if not "🌋 Adventure Seeker - Conqueror of Natural Wonders" in badge_list:
            badge_list.append("🌋 Adventure Seeker - Conqueror of Natural Wonders")
            print("BADGE EARNED")
            print("🌋 Adventure Seeker - Conqueror of Natural Wonders")
