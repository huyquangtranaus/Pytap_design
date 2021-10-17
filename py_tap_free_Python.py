#!python
import os
from PIL import Image, ImageFont, ImageDraw # cài đặt bằng lệnh: pip install Pillow
import qrcode # cài đặt bằng  lệnh:  pip install qrcode

''' 1-  Nhập tên chủ thẻ '''
ten_cua_ban = input('\nNhap ten cua ban: ')

''' 2- Đọc file thẻ nền '''
my_image = Image.open("py_tap_sample_jpg.jpg")

''' 3  Đọc font chữ (tùy chọn, có thể chọn từ: # https://fonts.google.com/ '''
title_font = ImageFont.truetype('Roboto-Bold.ttf', 100)  
# (100: ở đây là font chữ, có thể thay đổi tùy ý)

''' 4-  Tạo mã qrcode '''
img = qrcode.make( str(ten_cua_ban))  # tạo qrcode
img.save(str(ten_cua_ban) + '.bmp') # Lưu file qrcode

''' 5-  Đọc file  qrcode vừa tạo để chuẩn bị copy lên file thẻ '''
im = Image.open(str(ten_cua_ban) + '.bmp')  # 25x25

''' 6-  Copy qrcode lên file thẻ'''
my_image.paste(im, (15, 15)); os.remove(str(ten_cua_ban) + '.bmp')

''' 7 - Chèn chữ: tên chủ thẻ  lên thẻ'''
image_editable = ImageDraw.Draw(my_image) 
image_editable.text((15,450), ten_cua_ban, (237, 230, 211), font=title_font) 
# (15,450: Vị trí có thể thay đổi)


''' 8 - Lưu thẻ thành file'''
my_image.save(ten_cua_ban +".jpg")