import pytest
import requests
from api_test_data import APITestData

"""
測試 POST 新增新的課程
"""
def test_create_new_course():
    course_data = APITestData.get_course_data()
    
    response = requests.post(f"{APITestData.BASE_URL}/courses", json=course_data)
    
    assert response.status_code == 201
    data = response.json()
    
    #確認課程內容基本資訊無缺漏
    assert data["course_name"] == course_data["course_name"]
    assert data["description"] == course_data["description"]
    assert data["start_time"] == course_data["start_time"]
    assert data["end_time"] == course_data["end_time"]
    assert data["instructor"]["instructor_id"] == course_data["instructor"]["instructor_id"]
