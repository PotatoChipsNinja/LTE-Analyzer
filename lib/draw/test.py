# -*- coding: utf-8 -*-
import draw

# JPEG
draw.save_jpg(20.0, 'img.jpg')

# Base64
with open('base64.txt', 'w') as f:
    f.write(draw.get_base64(20.0))
