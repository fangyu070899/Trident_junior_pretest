class APITestData:
    BASE_URL = "http://example.com" 

    @staticmethod
    def get_course_data():
        return {
            "course_name": "Data Structures",
            "description": "Study of various data structures.",
            "start_time": "1000",
            "end_time": "1200",
            "instructor": {
                "instructor_id": 1,
                "name": "John Doe",
                "email": "john.doe@example.com"
            }
        }
