from sqlalchemy import func, desc, and_, distinct, select

from src.models import Teacher, Student, Discipline, Grade, Group
from src.db import session


def select_1():
    """
    Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    :return:
    """
    result = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()
    return result


def select_2():
    """
    Знайти студента із найвищим середнім балом з певного предмета.
    :return:
    """
    result = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .join(Grade).filter(Grade.discipline_id == 2).group_by(Student.id) \
        .order_by(desc('avg_grade')).first()
    return result


def select_3():
    """
    Знайти середній бал у групах з певного предмета.
    :return:
    """
    result = session.query(Group.name, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .join(Student).join(Grade).filter(Grade.discipline_id == 2).group_by(Group.id).all()
    return result


def select_4():
    """
    Знайти середній бал на потоці (по всій таблиці оцінок).
    :return:
    """
    result = session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')).scalar()
    return result


def select_5():
    """
    Знайти список курсів, які читає певний викладач.
    :return:
    """
    result = session.query(Discipline.name).filter(Discipline.teacher_id == 3).all()
    return result


def select_6():
    """
    Знайти список студентів у певній групі.
    :return:
    """
    result = session.query(Student.fullname).filter(Student.group_id == 2).all()
    return result


def select_7():
    """
    Знайти оцінки студентів в окремій групі з певного предмета.
    :return:
    """
    result = session.query(Student.fullname, Grade.grade) \
        .join(Grade).filter(Student.group_id == 1, Grade.discipline_id == 2).all()
    return result


def select_8():
    """
    Знайти середній бал, який ставить певний викладач зі своїх предметів.
    :return:
    """
    result = session.query(distinct(Teacher.fullname), func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade) \
        .join(Discipline)  \
        .join(Teacher) \
        .where(Teacher.id == 3).group_by(Teacher.fullname).order_by(desc('avg_grade')).limit(5).all()
    return result


def select_9():
    """
    Знайти список курсів, які відвідує певний студент.
    :return:
    """
    result = session.query(Discipline.name).join(Grade).filter(Grade.student_id == 3).all()
    return result


def select_10():
    """
    Список курсів, які певному студенту читає певний викладач.
    :return:
    """
    result = session.query(Discipline.name) \
        .join(Grade).join(Teacher).filter(Grade.student_id == 2, Teacher.id == 3).all()
    return result



if __name__ == '__main__':
    print(select_1())
    print(select_2())
    print(select_3())
    print(select_4())
    print(select_5())
    print(select_6())
    print(select_7())
    print(select_8())
    print(select_9())
    print(select_10())