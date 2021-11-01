from PIL import Image
import io
import numpy as np


def padd_list(current_list, ideal_length):
	return current_list + [''] * (ideal_length - len(current_list))

def encode(image, pixels, height, width, message):

    pixels = [list(i) for i in pixels]
    message = message.replace('”', '"')
    message = message.replace('’', "'")
    message = message.replace('“', '"')
    message = message.replace('‘', "'")
    message = message.replace('—', '-')
    message = (message+"~")

    message_in_binary = []
    for char in message:
        message_in_binary.append(bin(ord(char))[2:].zfill(8))         # char -> ascii code -> binary -> remove first 0b -> padd to 8 bits

    bit_map = [i for ele in message_in_binary for i in ele]
    bit_map = padd_list(bit_map, width*height*3)
    bit_map = np.array(bit_map)
    bit_map = np.reshape(bit_map, (int(height*width), 3))


    for x in range(0,len(pixels)):

        pixel_message = bit_map[x]
        bit_num = 0

        for bit in pixel_message:
            if bit == '1':
                if pixels[x][bit_num] % 2 == 0:
                    pixels[x][bit_num] -= 1
                elif pixels[x][bit_num] % 2 == 1:
                    pass
            elif bit == '0':
                if pixels[x][bit_num] % 2 == 0:
                    pass
                elif pixels[x][bit_num] % 2 == 1:
                    pixels[x][bit_num] -= 1
            else:
                pass     
            bit_num += 1


    pixels = tuple(map(tuple, pixels))

    im2 = Image.new(image.mode, image.size)
    im2.putdata(pixels)
    im2.save("encoded_image.png")
    print("image saved")