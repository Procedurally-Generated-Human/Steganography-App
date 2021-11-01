import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import Image
from decode import decode
from encode import encode

window = tk.Tk()
window.title("PGH's Steganography")
window.resizable(False, False)


def get_image():
    file_location = askopenfilename()
    lbl_image.config(text="Image: "+ file_location)
    global image
    image = Image.open(file_location)
    global pixels
    pixels = list(image.getdata())
    global width, height
    width, height = image.size


def decode_image():
    txt_message.delete('1.0', tk.END)
    message = decode(pixels)
    txt_message.insert(1.0, message)


def encode_image():
    message = txt_message.get("1.0","end")
    txt_message.delete('1.0', tk.END)
    encode(image, pixels, height, width, message)




#image = Image.open('image.jpeg')
#width, height = image.size


# choose image
frm_upload = tk.Frame(window)

btn_upload = tk.Button(text="Choose Image", command = get_image)
btn_upload.pack(side=tk.TOP, anchor=tk.NW)

lbl_image = tk.Label(text="Image: ")
lbl_image.pack(side=tk.TOP, anchor=tk.W)


# message area
lbl_message = tk.Label(text="Message",font=("Helvetica", 20, 'bold'))
txt_message = tk.Text()


# encode and decoding 
frm_button_pair = tk.Frame(window)

btn_encode = tk.Button(frm_button_pair, text="Encode", command = encode_image)
btn_encode.pack(side = tk.RIGHT)

btn_decode = tk.Button(frm_button_pair, text="Decode", command = decode_image)
btn_decode.pack(side = tk.LEFT)



# packing
frm_upload.pack()
lbl_message.pack()
txt_message.pack()
frm_button_pair.pack()

window.mainloop()