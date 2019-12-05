import cv2
def processed_image(img, scale):
    height, width, channels = img.shape
    new_height = int(height * scale)  
    new_width = int(width * scale)  
    new_dim = (new_width, new_height)
    img_resized = cv2.resize(img, new_dim, interpolation=cv2.INTER_LINEAR)  # resized image
    img_resized = (img_resized - 127.5) / 128   
    return img_resized


#img=(100,120)  20*20  40*40
#100*12/20=60   (60,72)  先检测小人脸，再通过缩放检测大人脸
#(42.54,51.048)


#net_size=6  (30,36)  降低net_size相当于减少了金字塔层数
def pyramid_image(img):
    net_size = 12       
    min_face_size = 20   #原始图片的最小人脸
    current_scale = float(net_size) / min_face_size   # find initial scale
    im_resized = processed_image(img, current_scale)  # the first layer of image pyramid
    current_height, current_width, _ = im_resized.shape
    while min(current_height, current_width) > net_size:  #默认最大人脸为图片本身
        current_scale *= self.scale_factor
        im_resized = processed_image(im, current_scale)
