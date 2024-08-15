import pytest
import requests
from api_test_data import APITestData

"""
測試 DELETE 刪除課程
"""
def test_delete_course():
    course_id = 1
    response = requests.delete(f"{APITestData.BASE_URL}/courses/{course_id}")
    
    #確認是否刪除成功
    assert response.status_code == 200


    # 嘗試再次刪除同一課程，預期會返回404
    response = requests.delete(f"{APITestData.BASE_URL}/courses/{course_id}")
    
    assert response.status_code == 404

