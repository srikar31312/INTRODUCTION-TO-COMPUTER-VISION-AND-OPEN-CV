import cv2

#load the image
image= cv2.imread('images-5.png')

# Resize the window to a specific size without resizing the image
cv2.namedWindow('Loaded Image',cv2.WINDOW_NORMAL)# Create a resizable window
cv2.resizeWindow('Loaded Image',800,500)#Set the window size to 800x500(Width x Height)

# Display the image in the resized window
cv2.imshow('Loaded Image',image)
cv2.waitKey(0) #Wait for key press
cv2.destroyAllWindows() # Close the window

# Print image properties
print(f"Image Dimensions:{image.shape}") # Height,Width,Channels