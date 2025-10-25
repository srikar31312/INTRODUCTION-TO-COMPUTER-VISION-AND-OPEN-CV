import cv2

# load the image
image=cv2.imread('1234.png')

#convert the image into gray scale
gray_image =cv2.cvtColor(image.cv2.COLOR_BGR2GRAY)

#resize the gray scale image to 224 x 224
resized_image = cv2.resize(gray_image, (224,224))

#Display the resized grayscale image in a single window
cv2.imshow('Processed image',resized_image)

#Wait for a key press
key = cv2.waitkey(0) # Wait indefinetly for a key press

# Check if the "S" key was pressed(ASCII for 'S' is 83)
if key == ord('S'):
    #Save the processed image when "S" is pressed
    cv2.imwrite('grayscale_resized_image.png',resized_image)
    print("Image saved as grayscale_resized _image.png")
else:
    print("Image not saved")

    # Close the window 
    cv2.destroyAllWindows()

    #Print processed image properties
    print(f"Processed Image Dimensions: {resized_image.shape}")