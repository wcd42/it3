import sys
from PyQt6 import QtWidgets
from mysql1.Course import Course
from mysql1.ActiveSystem import ActiveSystem
from Controller.KU_Planner_login import MainWindowGUI
from mysql1.mysqlcoursedao import MySQLCourseDAO

def main():

    # create a DAO (database access object)
    courseDAO = MySQLCourseDAO()

    ActiveSystem.set_dao(courseDAO)
    # set up the database (drop the existing table!)
    courseDAO.setup()
    # start a connection to the database
    # connect to the database
    courseDAO.connect()
    # list all entries (it should be empty)
    courseDAO.find_all()

    # add som test persons
    course1 = Course(1, "ku", "dev")
    ActiveSystem.add_course(course1)
    courseDAO.insert_course(course1)

if __name__ == '__main__':
    main()