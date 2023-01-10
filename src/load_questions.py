#!/bin/python

from models.topic import Topic
from models.lesson import Lesson
from models.question import Question
from models.answer import Answer
from create_engine import ENGINE
from sqlalchemy import text


def save_all(topic: Topic, lesson: Lesson, question: Question, answer: Answer):
    ENGINE.execute(text("INSERT INTO topics VALUES (nextval('public.topics_id_seq'), :name)"), name=topic)
    ENGINE.execute(text("INSERT INTO lessons VALUES (nextval('public.lessons_id_seq'), currval('public.topics_id_seq'), :name)"), name=lesson)
    ENGINE.execute(text("INSERT INTO questions VALUES (nextval('public.questions_id_seq'), currval('public.lessons_id_seq'), :value)"), value=question)
    ENGINE.execute(text("INSERT INTO answers VALUES (nextval('public.answers_id_seq'), currval('public.questions_id_seq'), :value)"), value=answer)

def main():
    print(f"\nWelcome to add topic/lesson/question/answer(s)")
    while (True):
        try:
            topic = input("\nTopic: ")
            lesson = input("\nLesson: ")
            question = input("\nQuestion: ")
            while (True):
                # TODO in the future uncomment this and implement multiple choice questions
                # type_of_question = input("\nType of question\na. Definition\nb. Multiple Choice\n")
                type_of_question = 'a'
                if (type_of_question.lower() == "a" or type_of_question.lower() == "b"):
                    break
                else:
                    print("\nInvalid input. Try again. Accepted values are [a/b]")
            list_of_answers = list()
            if type_of_question.lower() == "a":
                list_of_answers.append(input("\nAnswer: "))
            else:
                while (True):
                    try:
                        answer = input("\nAnswer: ")
                        is_correct = input("\nIs Correct? [Y/n]: ")
                        list_of_answers.append(
                            {"answer": answer, "is_correct": True if is_correct.lower() == "y" else False})
                    except KeyboardInterrupt:
                        interrupt = input(f"\nCaught {len(list_of_answers)}\nKeep adding answers? [Y/n]")
                        if (interrupt.lower() != "y"):
                            break
            # TODO this is hardcoded for now, in the future we may implement multiple choice questions
            save_all(topic, lesson, question, list_of_answers[0])
            print(f"Saved --> Topic: {topic} - Lesson: {lesson} - Question: {question} - Anwers(s): {list_of_answers}")
            # save to DB
        except KeyboardInterrupt:
            quit_adding = input(f"\nQuit adding? [Y/n]:")
            if quit_adding.lower() == "y":
                break

    print("\nEnjoy your learning!\n")


main()
