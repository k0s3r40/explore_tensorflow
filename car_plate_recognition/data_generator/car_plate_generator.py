import random

from PIL import Image


class ImageGenerator:
    def __init__(self, plates_count):
        self.plates_count = plates_count
        self.signs = '1234567890ABCEHKMOPTXY'
        for i in range(self.plates_count):
            self.generate(self.generate_plate_number())

    def generate_plate_number(self):
        return ''.join([self.signs[random.randint(0, len(self.signs) - 1)] for i in range(0, 8)])

    def compute_start_x(self, max_width, item_width):
        return int((max_width - item_width) / 2)

    def generate(self, plate_number):
        plate_number = plate_number
        canvas = Image.open('docs/base_plate_1.png').convert('RGBA')

        signs = [
            Image.open(f'docs/images/{i}.png').convert('RGBA') for i in plate_number
        ]
        max_height = max([i.height for i in signs])
        max_width = max([i.width for i in signs])
        accumulated_width = 0
        for index, value in enumerate(plate_number):
            sign = signs[index].resize(size=(signs[index].width, max_height))
            accumulated_width += max_width + (10 * 5 if index in [2, 6] else 1)
            sign_canvas = Image.new('RGBA', size=(120, 180), color=(0, 0, 0, 0))
            sign_canvas.paste(sign, (self.compute_start_x(120, sign.width), 0))
            canvas.paste(sign_canvas, (accumulated_width, 10), sign_canvas)

        canvas.save(f'./car_plates/{plate_number}.png')


if __name__ == '__main__':
    generator = ImageGenerator(20)
