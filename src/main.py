#!/bin/python

import winsound
import random
from dotenv import load_dotenv
import os
import time
from random import choice

load_dotenv()

duration = int(os.getenv("DURATION", 500))  # milliseconds
freq = 440  # Hz

topic = os.getenv("TOPIC")
lesson = os.getenv("LESSON")

def show_config():
    print(f"Your configuration looks like this:\n-{topic}\n-{lesson}")


def get_all_topics():
    return list()


def get_all_lessons_by_topic(topic):
    return list()


def get_questions_and_answers():
    return ["question 1", "question 2", "question 3"]


def get_answers():
    # according to qustions, answers will be fetched
    reutrn list()


#main loop for the program
def main():
    global topic
    global lesson
    while(True):
        try:
            show_config()
            while(True):
                winsound.Beep(freq, duration)
                questions_list = get_questions_and_answers()
                try:
                    show_questions(questions_list)
                    print(f"\nScheduling next questions ...\n")
                    time.sleep(choice(range(int(os.getenv("FLOOR_BOUND", 5)), int(os.getenv("CEIL_BOUND", 10)))))
                except KeyboardInterrupt:
                    user_answer = input("\nDo you want to change topic/lesson? [Y/n]: ")
                    if (user_answer.lower() == "y"):
                        topic = input("Topic: ")
                        lesson = input("Lesson: ")
                        break
                    else:
                        raise KeyboardInterrupt()

        except KeyboardInterrupt:
            exit_program = input("\nDo you want to exit program? [Y/n]: ")
            if (exit_program.lower() == "y"):
                break


def show_questions(questions_list):
    for question in questions_list:
        print(question)
        input("Your answer: ")


main()

