import sys
from utils import *
import matplotlib.pyplot as plt

if len(sys.argv)>1:
  folder = sys.argv[1]
else:
  folder = 'headshoulderdata'

seg = fingernailseg(folder)

if len(sys.argv)>2:
  separable = True
else:
  separable = False

if separable:
  print('create separable unet');
  seg.create_separable_unet()
else:
  print('create unet');
  seg.create_unet()

print('loading model')
seg.load_model()
print('predicting')

mask = seg.predict()
raw = seg.X_test
for i in range(0,seg.X_test.__len__()):
  plt.figure(figsize=(5,5))
  rand_image = i
  plt.imshow(raw[rand_image,:,:,:])
  plt.imshow(mask[rand_image,:,:,0], alpha=0.8)
  #plt.title('Fingernails segmentation of test image', fontsize=15)
  filename = str(rand_image)+'.png'
  plt.savefig(filename)
  print('saved',filename)
print('done')
