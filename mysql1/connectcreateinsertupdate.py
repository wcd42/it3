import mysql.connector
from mysql.connector import errorcode
from mysql1.Course import Course

class MySQLDB:
    DB_NAME = "kudb"
    @classmethod
    def createDataBase(cls):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Halo4242"
        )
        mycursor = db.cursor()

        mycursor.execute("CREATE DATABASE kuplanner")

    @classmethod
    def setup(cls):
        db = mysql.connector.connect(
            user='root',
            password='Halo4242',
            host='127.0.0.1',
            database="kuplanner"
        )
        mycursor = db.cursor()

        create = """CREATE TABLE Courses1 ("
        "`course_id` INT NOT NULL,"
        "`faculty` VARCHAR(45) NOT NULL,"
        "`course_name` VARCHAR(45) NOT NULL,"
        "PRIMARY KEY (`course_id`));"

        "CREATE TABLE IF NOT EXISTS courseRequests1 ("
        "`course_id` INT NOT NULL,"
        "`faculty` VARCHAR(45) NOT NULL,"
        "`course_name` VARCHAR(45) NOT NULL,"
        "PRIMARY KEY (`course_id`))", multi = True)
        """

        mycursor.execute(create, multi=True)
        db.commit()

    @classmethod
    def insert_course(cls, course: Course):
        db = mysql.connector.connect(
            user='root',
            password='Halo4242',
            host='127.0.0.1',
        )
        id_course = course.get_course_id()
        faculty = course.get_faculty()
        course_name = course.get_course_name()
        mycursor = db.cursor()
        insert = """INSERT INTO Courses (id_course, faculty, course_name) "
                         "VALUES (%s,%s,%s)"
                        """
        mycursor.execute(insert, (id_course, faculty, course_name), multi=True)
        db.commit()

    @classmethod
    def insert_courseRequest(cls, course: Course):
        db = mysql.connector.connect(
            user='root',
            password='Halo4242',
            host='127.0.0.1',
            database='KUDB'
        )
        id_course = course.get_course_id()
        faculty = course.get_faculty()
        course_name = course.get_course_name()
        mycursor = db.cursor()

        insert = """INSERT INTO courseRequests (id_course, faculty, course_name) "
                         "VALUES (%s,%s,%s)"
                        """
        mycursor.execute(insert, (id_course, faculty, course_name), multi=True)
        db.commit()

    @classmethod
    def delete_course(cls, course: Course):
        db = mysql.connector.connect(
            user='root',
            password='Halo4242',
            host='127.0.0.1',
            database='KUDB'
        )

        idcourse = course.get_course_id()
        mycursor = db.cursor()

        delete = """
                DELETE FROM KUDB.Courses
                WHERE idcourse="%s"
                """ % idcourse

        mycursor.execute(delete)
        mycursor.commit()

    @classmethod
    def delete_courseRequest(cls, course: Course):
        db = mysql.connector.connect(
            user='root',
            password='Halo4242',
            host='127.0.0.1',
            database='KUDB'
        )

        idcourse = course.get_course_id()
        mycursor = db.cursor()

        delete = """
                DELETE FROM KUDB.courseRequests
                WHERE idcourse="%s"
                """ % idcourse

        mycursor.execute(delete)
        mycursor.commit()

    @classmethod
    def fetch_courseRequests(cls, course_id):
        cls.course_id = course_id
        db = mysql.connector.connect(
            user='root',
            password='Halo4242',
            host='127.0.0.1',
            database='KUDB'
        )

        mycursor = db.cursor()

        fetch = """ 
                SELECT * FROM KUDB.courseRequests WHERE course_id = "course_id"
                """

        mycursor.execute(fetch)
        record = mycursor.fetchone()


