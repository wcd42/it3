class CourseRequest:

    def __init__(self, cr_id: int, cr_faculty: str, cr_name: str):
        self.cr_id = cr_id
        self.cr_faculty = cr_faculty
        self.cr_name = cr_name



    def set_faculty(self, new_faculty: str):
        self.__cr_faculty = new_faculty

    def get_faculty(self):
        return self.__cr_faculty

    def get_course_id(self):
        return self.__cr_id

    def set_course_id(self, new_course_id: int):
        self.__cr_id = new_course_id

    def get_course_name(self):
        return self.__cr_name

    def set_course_name(self, new_course_name: str):
        self.__cr_name = new_course_name