from PIL import Image
import binascii


def binary_to_chr(binary):
    string = int(binary, 2)
    string = chr(string)
    return string


def chunks(l, n):
    n = max(1, n)
    return (l[i:i+n] for i in range(0, len(l), n))


def decode(pixels):
    code_in_binary = []
    for x in range(0,len(pixels)):

        bit_num = 0
        for bit in pixels[x]:
            if pixels[x][bit_num] % 2 == 0:
                code_in_binary.append('0')
            elif pixels[x][bit_num] % 2 == 1:
                code_in_binary.append('1')
            
            bit_num += 1


    code_in_binary = "".join(code_in_binary)
    chunked_message = list(chunks(code_in_binary, 8))

    message = []
    for byte in chunked_message:
        message.append(binary_to_chr(byte))

    message = "".join(message)
    return(message.split('~')[0])

