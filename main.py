from PIL import Image
import numpy as np

# from PIL, I created an object called 'im' which is an instance of the Image class and this photo is now an Image object
img = Image.open(r"E:\Python\Projects\Photomosaics\monkey.jpg")
img.show()

# img. size returns width (number of pixel columns) x height (number of pixel rows)
print(img.format, img.size, img.mode)
image_new_width = 500
image_new_height = 500
# we need to resize the image to make it a square image. One thing we can do later is make a method that always does this or can just search for images in a file and make them square automatically or find square images
img = img.resize((image_new_width, image_new_height), Image.ANTIALIAS)
img.show()
# each block of lists outputted (in this case, printed) is a row of pixels in the image. Remember that matrices are R (rows) x C (columns)
# pixel_matrix = np.asarray(img)
#print(pixel_matrix)

'''
The below returns a flattened list of tuples representing RGB values for one pixel (not an array/matrix),
so let's do it manually instead of using numpy just as a super mini-challenge :)
'''
all_pixels = list(img.getdata())
#print(all_pixels)
#print(len(all_pixels))
pixel_matrix = []
starting_point = 0
for i in range(0, img.size[1]):
    pixel_matrix.append(all_pixels[starting_point : starting_point+img.size[0]])
    # update the starting point
    starting_point = starting_point+img.size[0]

#print(pixel_matrix)
print(len(pixel_matrix))
print(len(pixel_matrix[0]))
print(pixel_matrix[0])
print(pixel_matrix[0][0])

square_size = 50
number_squares = int(img.size[0] / square_size)
print(square_size, number_squares)

#corner = pixel_matrix[i][j]
#opposite_corner = pixel_matrix[i][j +  square_size]
square = []
for i in range(0, len(pixel_matrix)-square_size, square_size):
    for k in range(0, len(pixel_matrix[0]), square_size):
        row = []
        for j in range(i, i + square_size):
            row.append(pixel_matrix[j][k:k+square_size])
        square.append(row)

#print(square)
print(square[0])
print(len(square))
print(len(square[0]))
print(len(square[0][0]))
print(square[0][0])
print(square[0][1])
print(square[0][0][0])

average_pixel_square_matrix = []
for i in range(0, len(square)):
    sum_red = 0
    sum_green = 0
    sum_blue = 0
    average_pixel = ()
    for j in range(0, len(square[0])):
        for k in range(0, len(square[0][0])):
            sum_red += square[i][j][k][0]
            sum_green += square[i][j][k][1]
            sum_blue += square[i][j][k][2]
        average_pixel = (int(sum_red / (square_size * 2)), int(sum_green / (square_size * 2)), int(sum_blue / (square_size * 2)))
    average_pixel_square_matrix.append(average_pixel)
print(len(average_pixel_square_matrix))
'''
print(len(average_pixel_square_matrix))
print(average_pixel_square_matrix)
'''
#pixellated_img = Image.frombytes('RGB', (10,10), average_pixel_square_matrix)
#average_pixel_square_matrix = np.asarray(average_pixel_square_matrix)
#pixellated_img = Image.fromarray(average_pixel_square_matrix)
pixellated_img = Image.new('RGB', (len(average_pixel_square_matrix),len(average_pixel_square_matrix)))
pixellated_img.putdata(average_pixel_square_matrix)
for x in range(len(average_pixel_square_matrix)):
    for y in range(len(average_pixel_square_matrix)):
        pixellated_img.putpixel((x, y), average_pixel_square_matrix[x][y])
pixellated_img.show()
all_pixels2 = list(pixellated_img.getdata())
print(all_pixels2)
'''

source_images = []
for i in range(0, )
img = Image.open(r"E:\Python\Projects\Photomosaics\monkey.jpg")
'''
