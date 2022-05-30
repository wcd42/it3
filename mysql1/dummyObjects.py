from Course import Course
from Courses import Courses
class dummyObjects:
    @staticmethod
    def create():
        courseA = Course(1,"DTU", "Programming")
        courseB = Course(2,"KU", "D0CT3R")
        courseList = Courses()
        courseList.append_course(courseA)
        courseList.append_course(courseB)
        return courseList