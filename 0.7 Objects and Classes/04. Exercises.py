while True:
    token = input()
    if token == 'go go go':
        break
    topic, course, link, problems = token.split(' -> ')
    print('Exercises:', topic)
    print(f'Problems for exercises and homework for the "{course}" course @ SoftUni.')
    print('Check your solutions here:', link)
    [print(str(i + 1) + '. ' + x) for i, x in enumerate(problems.split(', '))]

'''
ObjectsAndSimpleClasses -> ProgrammingFundamentalsExtended -> https://judge.softuni.bg/Contests/439 -> Exercises, OptimizedBankingSystem, Animals, Websites, Boxes, BoxIntersection, Messages
go go go
'''

'''
class Exercise:
    def __init__(self, topic='', course_name='', judge_contest_link='', problems=None):
        self.topic = topic
        self.course_name = course_name
        self.judge_contest_link = judge_contest_link
        self.problems = problems

    def __repr__(self):
        array = self.problems.split(', ')
        course = '"' + self.course_name + '"'
        return (
                f"Exercises: {self.topic}\n"
                f"Problems for exercises and homework for the {course} course @ SoftUni.\n"
                f"Check your solutions here: {self.judge_contest_link}\n"
                + "\n".join([f"{i + 1}. {x}" for i, x in enumerate(array)])
        )


# lst = [x.strip() for x in input().split(' -> ') if x != 'go go go']
#
# cls = Exercise()
# cls.topic, cls.course_name, cls.judge_contest_link, cls.problems = lst
# print(cls)
def main():
    exercises = []

    while True:
        line = input().strip()
        if line == "go go go":
            break

        parts = line.split(" -> ")
        if len(parts) != 4:
            continue

        topic, course_name, judge_contest_link, problems = parts
        problems_list = problems.split(", ")
        exercise = Exercise(topic, course_name, judge_contest_link, problems_list)
        exercises.append(exercise)

    for exercise in exercises:
        print(exercise)


if __name__ == "__main__":
    main()
'''




