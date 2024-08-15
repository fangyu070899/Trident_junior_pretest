import pytest
import requests
from api_test_data import APITestData

"""
測試 Get 課程列表 api
"""
def test_get_course_list():
    response = requests.get(f"{APITestData.BASE_URL}/courses", params={"limit": 10})
    
    assert response.status_code == 200
    data = response.json()
    
    assert isinstance(data, list)  #確認回傳資料型態是否為list
    assert len(data) <= 10  #確認回傳資料筆數不大於limit
    
    #確認課程內容基本資訊無缺漏
    assert "course_id" in data[0]
    assert "course_name" in data[0]
    assert "instructor" in data[0]
    assert "name" in data[0]["instructor"]
    assert "email" in data[0]["instructor"]
