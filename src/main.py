#!/bin/python

import winsound
from dotenv import load_dotenv
import os
import time
from random import choice
from sqlalchemy import create_engine, text


load_dotenv()

duration = int(os.getenv("DURATION", 500))  # milliseconds
freq = 440  # Hz

topic = os.getenv("TOPIC")
lesson = os.getenv("LESSON")

engine = create_engine(os.getenv("CONNECTION"))

def show_config():
    print(f"\nYour configuration looks like this:\n\nTopic: {topic}\nLesson: {lesson}")


def get_all_topics():
    return list()


def get_all_lessons_by_topic(topic):
    return list()


def get_questions_and_answers(connection):
    return connection.execute(text("SELECT q.*, a.* FROM questions q JOIN lessons l ON q.lesson_id = l.id JOIN topics t ON l.topic_id = t.id JOIN answers a ON a.question_id = q.id WHERE t.name = :topic AND l.name = :lesson"), topic=topic, lesson=lesson)

#main loop for the program
def main():
    global topic
    global lesson
    while (True):
        try:
            show_config()
            while (True):
                winsound.Beep(freq, duration)
                questions_list = get_questions_and_answers(engine)
                try:
                    show_questions(questions_list)
                    print(f"\nScheduling next questions ...\n")
                    time.sleep(choice(range(int(os.getenv("FLOOR_BOUND", 5)), int(os.getenv("CEIL_BOUND", 10)))))
                except KeyboardInterrupt:
                    user_answer = input("\nChange topic/lesson? [Y/n]: ")
                    if (user_answer.lower() == "y"):
                        topic = input("Topic: ")
                        lesson = input("Lesson: ")
                        break
                    else:
                        raise KeyboardInterrupt()

        except KeyboardInterrupt:
            exit_program = input("\nQuit program? [Y/n]: ")
            if (exit_program.lower() == "y"):
                break



def show_questions(questions_list):
    for count, question in enumerate(questions_list):
        print(f"\n{count+1}) {question[2]} \n")
        input("Your answer: ")
        print(f"\nAnswer in database:\n\n{question[5]}")


main()

