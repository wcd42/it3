from abc import abstractmethod
from mysql1.DAO import DAO
from mysql1.CourseRequest import CourseRequest
from typing import List
from mysql1.CourseSearchType import CourseSearchType


class CourseRequestDAO(DAO):

    @abstractmethod
    def insert_course(self, course: CourseRequest):
        pass

    @abstractmethod
    def update_course(self, course: CourseRequest) -> bool:
        pass

    @abstractmethod
    def delete_course(self, course: CourseRequest) -> bool:
        pass

    @abstractmethod
    def find_course_by_property(self, search_type: CourseSearchType, value: object) -> List[CourseRequest]:
        pass

    @abstractmethod
    def find_all(self) -> List[CourseRequest]:
        pass