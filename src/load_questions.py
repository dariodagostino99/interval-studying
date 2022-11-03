#!/bin/bash

def main():
    print(f"\nWelcome to add topic/lesson/question/answer(s)")
    while(True):
        try:
            topic = input("\nTopic: ")
            lesson = input("\nLesson: ")
            question = input("\nQuestion: ")
            while(True):
                type_of_question = input("\nType of question\na. Definition\nb. Multiple Choice\n")
                if (type_of_question.lower() == "a" or type_of_question.lower() == "b"):
                    break
                else:
                    print("\nInvalid input. Try again. Accepted values are [a/b]")
            list_of_answers = list()
            if type_of_question.lower() == "a":
                list_of_answers.append(input("\nAnswer: "))
            else:
                while(True):
                    try:
                        answer = input("\nAnswer: ")
                        is_correct = input("\nIs Correct? [Y/n]: ")
                        list_of_answers.append({"answer":answer, "is_correct":True if is_correct.lower() == "y" else False})
                    except KeyboardInterrupt:
                        interrupt = input(f"\nCaught {len(list_of_answers)}\nKeep adding answers? [Y/n]")
                        if(interrupt.lower() != "y"):
                            break
            print(f"Saved --> Topic: {topic} - Lesson: {lesson} - Question: {question} - Anwers(s): {list_of_answers}")
            # save to DB
        except KeyboardInterrupt:
            quit_adding = input(f"\nQuit adding? [Y/n]:")
            if quit_adding.lower() == "y":
                break

    print("\nEnjoy your learning!\n")



main()
