%matplotlib inline



rom PIL import Image

import matplotlib.pyplot as plt
import numpy as np




img = np.asarray(Image.open('../../doc/_static/stinkbug.png'))
print(repr(img))

array([[[104, 104, 104],
        [104, 104, 104],
        [104, 104, 104],
        ...,
        [109, 109, 109],
        [109, 109, 109],
        [109, 109, 109]],

       [[105, 105, 105],
        [105, 105, 105],
        [105, 105, 105],
        ...,
        [109, 109, 109],
        [109, 109, 109],
        [109, 109, 109]],

       [[107, 107, 107],
        [106, 106, 106],
        [106, 106, 106],
        ...,
        [110, 110, 110],
        [110, 110, 110],
        [110, 110, 110]],
       
       
       
       
       
       imgplot = plt.imshow(img)
       
       
       
       
       
       lum_img = img[:, :, 0]
plt.imshow(lum_img)



plt.imshow(lum_img, cmap="hot")



imgplot = plt.imshow(lum_img)
imgplot.set_cmap('nipy_spectral')



imgplot = plt.imshow(lum_img)
plt.colorbar()




plt.hist(lum_img.ravel(), bins=range(256), fc='k', ec='k')



plt.imshow(lum_img, clim=(0, 175))



imgplot = plt.imshow(lum_img)
imgplot.set_clim(0, 175)




img = Image.open('../../doc/_static/stinkbug.png')
img.thumbnail((64, 64))  # resizes image in-place
imgplot = plt.imshow(img)




imgplot = plt.imshow(img, interpolation="bilinear")




imgplot = plt.imshow(img, interpolation="bicubic")




