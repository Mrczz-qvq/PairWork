from Judge import compare
from PIL import Image

def get_matrix():
    letter_list = ['a', 'a2', 'b', 'b2', 'c', 'd', 'd2', 'e', 'f2', 'g',
                'h', 'h2', 'j2', 'k', 'm', 'm2', 'n',
                'o', 'o2', 'p', 'p2', 'q', 'q2', 'r', 's', 't',
                'u', 'u2', 'v', 'w2', 'x', 'x2', 'y', 'y2', 'z', 'z2']
    image_list = []
    for index in range(1, 10):
        filename = str(index) + '.jpg'
        image = Image.open(filename)
        image_list.append(image)
    white_image = Image.open('white.jpg')
    black_image = Image.open('black.jpg')

    letter = get_letter(image_list, letter_list, white_image, black_image)

    image_exam_list = []
    for index in range(1, 10):
        filename = filename = './gl/' + letter + '/' + str(index) + '.jpg'
        image_exam = Image.open(filename)
        image_exam_list.append(image_exam)

    tmp_map = []
    remain = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    for image in image_list:
        if compare(image, white_image) == 0:
            tmp_map.append(0)
            continue
        for index in range(0, 9):
            if index not in remain:
                continue
            if compare(image, image_exam_list[index]) == 0:
                tmp_map.append(index+1)
                remain.remove(index)

    orig_map = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for index in range(0, 9):
        orig_map[index//3][index%3] = tmp_map[index]
    return orig_map

def get_letter(image_list, letter_list, white_image, black_image):

    for image in image_list:
        if compare(image, white_image)==0 or compare(image, black_image)==0:
            continue
        for letter in letter_list:
            for num in range(1, 10):
                filename = './gl/' + letter + '/' + str(num) + '.jpg'
                image_exam = Image.open(filename)
                if compare(image, image_exam) == 0:
                    return letter
