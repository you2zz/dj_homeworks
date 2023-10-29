import pytest

from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Course, Student


@pytest.fixture()
def client():
    return APIClient()


@pytest.fixture()
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.fixture()
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.fixture()
def url():
    return '/api/v1/courses/'


# проверка получения первого курса
@pytest.mark.django_db
def test_get_first_course(client, course_factory, url):
    # Arrange
    course = course_factory(_quantity=1)
    # Act
    test_id = course[Course.objects.count() - 1].id
    response = client.get(f'{url}{test_id}/')
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert test_id == data['id']


# проверка получения списка курсов
@pytest.mark.django_db
def test_courses_list(client, course_factory, url):
    # Arrange
    courses = course_factory(_quantity=10)
    # Act
    response = client.get(url)
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)
    for i, c in enumerate(data):
        assert c['id'] == courses[i].id


# проверка фильтрации списка курсов по `id`:
@pytest.mark.django_db
def test_filter_id(client, course_factory, url):
    # Arrange
    courses = course_factory(_quantity=10)
    test_id = courses[6].id
    url = f'{url}?id={test_id}'
    # Act
    response = client.get(url)
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert test_id == data[0]['id']


# проверка фильтрации списка курсов по `name`
@pytest.mark.django_db
def test_filter_name(client, course_factory, url):
    # Arrange
    courses = course_factory(_quantity=10)
    test_name = courses[6].name
    temp_url = f'{url}?name={test_name}'
    # Act
    response = client.get(temp_url)
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert test_name == data[0]['name']


# - тест успешного создания курса:
@pytest.mark.django_db
def test_create_course(client, url):
    # Arrange
    count = Course.objects.count()
    name = 'test name course 1'
    # Act
    response = client.post(url, {'name': name})
    response_2 = client.get(url)
    # Assert
    assert response.status_code == 201
    assert Course.objects.count() == count + 1
    data = response.json()
    assert data['name'] == name
    data2 = response_2.json()
    assert data2[-1]['name'] == name


# - тест успешного обновления курса:
@pytest.mark.django_db
def test_update_course(client, course_factory, url):
    # Arrange
    courses = course_factory(_quantity=10)
    test_id = courses[6].id
    url = f'{url}{test_id}/'
    new_name = 'new name course'
    # Act
    response = client.patch(url, {'name': new_name})
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data['name'] == new_name


# тест успешного удаления курса.
@pytest.mark.django_db
def test_delete_course(client, course_factory, url):
    # Arrange
    courses = course_factory(_quantity=10)
    count = Course.objects.count()
    test_id = courses[6].id
    url = f'{url}{test_id}/'
    # Act
    response = client.delete(url)
    response_2 = client.get(url)
    # Assert
    assert response.status_code == 204
    assert Course.objects.count() == count - 1
    assert response_2.status_code == 404
