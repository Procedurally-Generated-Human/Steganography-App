# What is Steganography?   
Steganography is the practice of concealing a message within another message or a physical object. In computing/electronic contexts, a computer file, message, image, or video is concealed within another file, message, image, or video.  

# What Does This Program Do?   
It allows you to encode and decode text into any image file. 
![alt text](https://github.com/Procedurally-Generated-Human/Steganography-App/blob/main/Screen%20Shot%202021-11-02%20at%2011.04.01%20AM.png)

# How Much Text Can You Store in an Image?  
It depends on the size of the file. About 3 bytes for every 8 pixels. For example a 1000x1200 image can store around 450000 ASCII characters.  

# How Does This Program Hide Text in Images?  
First of all your inputted message is converted into binary, then the program loops through every pixel in the image and changes the RGB value acourding to the value of binary message(0=even and 1=odd).

# Does The Image Containing The Message Look Similar To The Orginal?  
Yes. It is practically impossible to see any difference between the two with the human eye. For example:  
![alt text](https://github.com/Procedurally-Generated-Human/Steganography-App/blob/main/comparison.jpeg) 
left: monalisa and right: monalisa + the entire text of alice in wonderland. 
  
# How Can I Use This Program?
Copy or clone all the files in this repository to a folder then run:
```
python main.py
```

