from mysql1.CourseRequestDAO import CourseRequestDAO
from mysql1.CourseRequest import CourseRequest
import mysql.connector
from mysql.connector import errorcode
from mysql.connector import pooling
from mysql1.CourseSearchType import CourseSearchType
from typing import List

class DAO_CourseRequest_MySQL(CourseRequestDAO):
    DB_NAME = 'KUDB'

    __pool__: pooling.MySQLConnectionPool
    __cnx__: mysql.connector.connection = None
    cursor = None

    @classmethod
    def setup(cls):
            cls.__cnx__ = mysql.connector.connect(user='root',
                                                  password='Halo4242',
                                                  host='127.0.0.1',
                                                  database='KUDB')

            create = """
            DROP TABLE IF EXISTS `CourseRequests`;
            CREATE TABLE `courseRequests` (
              `idCourse` int NOT NULL,
              `faculty` varchar(45) NOT NULL,
              `course_name` varchar(45) NOT NULL
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
            """
            with cls.__cnx__.cursor() as cursor:
                cursor.execute(create, multi=True)

    @classmethod
    def connect(cls):
        try:
            cls.__pool__ = pooling.MySQLConnectionPool(pool_name="mypool", pool_size=5, user='root',
                                                        password='Halo4242',
                                                        host='127.0.0.1', database=cls.DB_NAME)

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cls.__cnx__.close()

        cls.__cnx__ = cls.__pool__.get_connection()
        print("connection", cls.__cnx__)

    def close(cls):
        if cls.__cnx__ is not None:
            cls.__cnx__.close()

    @classmethod
    def insert_course(cls, courserequest: CourseRequest):
        idCourse = courserequest.get_course_id()
        faculty = courserequest.get_faculty()
        course_name = courserequest.get_course_name()

        insert = """
                    INSERT INTO KUDB.CourseRequests (idCourse, faculty, course_name)  
                    VALUES ("%s", "%s", "%s")
                    """ % (idCourse, faculty, course_name)

        with cls.__cnx__.cursor(dictionary=True) as cursor:
            cursor.execute(insert)
            cls.__cnx__.commit()

    @classmethod
    def update_course(cls, course: CourseRequest):
        idCourse = course.get_course_id()
        faculty = course.get_faculty()
        course_name = course.get_course_name()

        update = """
            UPDATE KUDB.CourseRequests 
            SET idCourse = "%s", faculty = "%s", course_name = "%s" 
            """ % (idCourse, faculty, course_name)

        cls.__cnx__ = mysql.connector.connect(pool_name="mypool")

        with cls.__cnx__.cursor(dictionary=True) as cursor:
            cursor.execute(update)
            cls.__cnx__.commit()

    @classmethod
    def delete_course(cls, course: CourseRequest):
        idcourse = course.get_course_id()

        delete = """
                DELETE FROM KUDB.CourseRequests 
                WHERE idCourse="%s"
                """ % idcourse

        with cls.__cnx__.cursor(dictionary=True) as cursor:
            cursor.execute(delete)
            cls.__cnx__.commit()

    def find_course_by_property(self, search_type: CourseSearchType, value: object) -> List[CourseRequest]:
        pass

    @classmethod
    def find_all(cls) -> List[CourseRequest]:

        query = "SELECT * FROM KUDB.Courses"
        print("findall connection", cls.__cnx__)
        cursor = cls.__cnx__.cursor(dictionary=True)
        with cls.__cnx__.cursor(dictionary = True) as cursor:
            cursor.execute(query)
            all_courses = cursor.fetchall()
        print(all_courses)
        print(cls.__pool__)
        return all_courses