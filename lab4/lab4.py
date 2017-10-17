import sys
from PIL import Image

def argument_parser(argv):
    """ 
    Description: This function will parse the argument passed from the terminal.
    
    TODO: You have to parse the argument and perform the corresponding operation.
    
    Args:
        argv: input argument passed from the terminal
    """

    ########## Write your code in below ##########
    if len(argv)==6:
        fileName, imageName, saveImageName, filterType, threshold, highThreshold=argv
        highThreshold=int(highThreshold)
    else:
        fileName, imageName, saveImageName, filterType, threshold=argv
    threshold=int(threshold)

    filterTypes=['HPF','LPF','BPF']
    img=read_image(imageName)

    img=image_to_list(img)

    if filterType == filterTypes[0]:
        high_pass_filter(img,threshold)
    elif filterType == filterTypes[1]:
        low_pass_filter(img,threshold)
    else:
        band_pass_filter(img,threshold,highThreshold)
    img=list_to_image(img)


    save_image(img,saveImageName)


def read_image(filename):
    """ 
    Description: This function will read the image according to the filename 
    and return the image.
    TODO: You have to read the image according to the filename and return 
	    the image.
    Args:
        filename: file name of the image
        img: the image
    """
    
    ########## Write your code in below ##########
    img=Image.open(filename)
    return img

def image_to_list(img):
    """
    Description: This function will transform an image to a high dimensional list.

    TODO: You have to transform the given image and return the result.
    Args:
        img: an input image 
        result: high dimensional list
    """

    ########## Write your code in below ##########
    result=[]
    
    for i in range(img.size[0]):
        temp=[]
        for j in range(img.size[1]):
            temp.append(list(img.getpixel((i,j))))
        result.append(temp)
    return result


def high_pass_filter(img, threshold):
    """
    Description: This function acts as a high pass filter 
        according to the given threshold and apply the filter to the image.
    
    TODO: You have to apply a high pass filter to the image according to the 
        given threshold and return the processed result.

    Args:
        img: an input image (high dimensional list)
        threshold: a threshold for a high pass filter
        result: the result (processed high dimensional list)
    """

    ########## Write your code in below ##########
    for i in range(len(img)):
        for j in range(len(img[i])):
            for k in range(len(img[i][j])):
                if img[i][j][k]<threshold:
                    img[i][j][k]=0
    result=img
    return result


def band_pass_filter(img, low_threshold, high_threshold):
    """
    Description: This function acts as a band pass filter 
        according to the two given thresholds and apply the filter to the image.
    
    TODO: You have to apply a band pass filter to the image according to the two
        given thresholds and return the processed result.

    Args:
        img: an input image (high dimensional list)
        low_threshold: low threshold for a band pass filter
        high_threshold: high threshold for a band pass filter
        result: the result (processed high dimensional list)
    """

    ########## Write your code in below ##########
    for i in range(len(img)):
        for j in range(len(img[i])):
            for k in range(len(img[i][j])):
                if img[i][j][k]<low_threshold:
                    img[i][j][k]=0
                elif img[i][j][k]>high_threshold:
                    img[i][j][k]=0
    result=img
    return result


def low_pass_filter(img, threshold):
    """
    Description: This function acts as a low pass filter 
        according to the given threshold and apply the filter to the image.
    
    TODO: You have to apply a low pass filter to the image according to the 
        given threshold and return the processed result.

    Args:
        img: an input image (high dimensional list)
        threshold: a threshold for a low pass filter
        result: the result (processed high dimensional list)
    """

    ########## Write your code in below ##########
    for i in range(len(img)):
        for j in range(len(img[i])):
            for k in range(len(img[i][j])):
                if img[i][j][k]>threshold:
                    img[i][j][k]=0
    result=img   
    return result
    

def list_to_image(img_list):
    """
    Description: This function will transform the high dimensional list to an image.

    TODO: You have to transform the given list and return the result.

    Args:
        img_list: a high dimensional list
        img: an image
    """

    ########## Write your code in below ##########

    imgNew=Image.new(mode='RGB', size=(len(img_list),len(img_list[0])))
    for i in range(len(img_list)):
        for j in range(len(img_list[0])):
            imgNew.putpixel((i,j),tuple(img_list[i][j]))
    return imgNew


def save_image(img, filename):
    """ 
    Description: This function will save the image as filename.

    TODO: You have to save the image according to the given filename.

    Args:
        img: the image
        filename: file name of the image
    """

    ########## Write your code in below ##########
    img.save(str(filename))


if __name__ == '__main__':
    argument_parser(sys.argv)

    