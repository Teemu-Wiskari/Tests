courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python",
           "Frontend-разработчик с нуля"]
name = [
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
     "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков",
     "Роман Гордиенко"],
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
     "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
     "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
     "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
     "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков",
     "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
     "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]


def search_popular_name(mentors):
    """Функция определения топ-3 популярных имён среди преподавателей."""
    python = set(mentors[0])
    java = set(mentors[1])
    fullstack = set(mentors[2])
    frontend = set(mentors[3])

    all_mentors = python | java | fullstack | frontend

    list_mentor = []
    for mentor in all_mentors:
        name = mentor.split()
        list_mentor.append(name[0])

    unique_names = set(list_mentor)

    list_unique_names = list(unique_names)
    list_unique_names.sort()

    сonsolidated_list = list(python) + list(java) + list(fullstack) + list(frontend)

    name_сonsolidated_list = []
    for all_name in сonsolidated_list:
        names = all_name.split()
        name_сonsolidated_list.append(names[0])

    list_count_name = []

    for count_name in set(name_сonsolidated_list):
        count_name_mentor = name_сonsolidated_list.count(count_name)
        list_count_name.append([count_name_mentor, count_name])

    list_count_name.sort()

    list_popular_name = list_count_name[-1:-4:-1]

    return (f"{list_popular_name[0][1]}: {list_popular_name[0][0]} раз(а), {list_popular_name[1][1]}:"
            f" {list_popular_name[1][0]} раз(а), {list_popular_name[2][1]}: {list_popular_name[2][0]} раз(а)")


def unique_names(mentors):
    """Функция определения уникальных имен преподавателей:"""
    python = set(mentors[0])
    java = set(mentors[1])
    fullstack = set(mentors[2])
    frontend = set(mentors[3])

    all_mentors = python | java | fullstack | frontend

    list_mentor = []
    for mentor in all_mentors:
        name = mentor.split()
        list_mentor.append(name[0])

    unique_names = set(list_mentor)

    list_unique_names = list(unique_names)
    list_unique_names.sort()

    return f'Уникальные имена преподавателей: {", ".join(list_unique_names)}'


def duration_courses(mentors):
    """Функция, определяющая продолжительность курсов"""
    global min, max
    durations = [14, 20, 12, 20]
    courses_list = []
    for title, mentors, duration in zip(courses, mentors, durations):
        course_dict = {"Название курса": title, "Продолжительность курса": duration,
                       "Преподаватели курса": ', '.join(mentors)}
        courses_list.append(course_dict)

    min_d = min(durations)
    max_d = max(durations)

    maxes = []
    minis = []
    for id, duration in enumerate(durations):
        if duration == max_d:
            maxes.append(id)
        elif duration == min_d:
            minis.append(id)

    courses_min = []
    courses_max = []
    for id in minis:
        courses_min.append(courses_list[id]['Название курса'])
    for id in maxes:
        courses_max.append((courses_list[id]['Название курса']))

    return (f'Самый короткий курс(ы): {", ".join(courses_min)} - {min} месяца(ев), Самый длинный курс(ы):'
            f' {", ".join(courses_max)} - {max} месяца(ев)')

