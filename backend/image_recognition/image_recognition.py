import face_recognition
import os
import math

from django.conf import settings

image_database = os.path.join(settings.MEDIA_ROOT, 'images')
output_image_path = '/media/images/'

MAX_DISTANCE = 10000
NUM_IMAGES = 5


def euclidean_distance(x, y):
    if len(y) == 0:
        return MAX_DISTANCE
    accumulate = sum((i - j) ** 2 for i, j in zip(x, y))
    return math.sqrt(accumulate)


def knn_search(query, data, num_neighbors):
    results = []
    for index, row in enumerate(data):
        distance = euclidean_distance(query, row)
        results.append((index, distance))
    results.sort(key=lambda x: x[1])
    results = [i[0] for i in results]
    return results[:num_neighbors]


def load_images():
    image_files = os.listdir(image_database)
    images_list = []
    for image_file in image_files:
        if image_file[0] != '.':
            image = face_recognition.load_image_file(
                image_database + '/' + image_file)
            encoding = face_recognition.face_encodings(image)
            if len(encoding):
                images_list.append(encoding[0])
            else:
                images_list.append([])
        if len(images_list) == NUM_IMAGES:
            break
    return images_list


def execute_query(query_image_path, num_neighbors):
    query_image = face_recognition.load_image_file(query_image_path)
    query_encoding = face_recognition.face_encodings(query_image)[0]

    image_list = os.listdir(image_database)
    output = []
    for image in image_list:
        if image[0] != '.':
            output.append(image)

    image_data = load_images()

    results = knn_search(query_encoding, image_data, num_neighbors)
    return [{'url': output_image_path + output[element],
             'title': output[element]}
            for element in results]
