import sys
from utils import *
if len(sys.argv)>1:
  folder = sys.argv[1]
else:
  folder = 'headshoulderdata'
print('folder found=',folder)
seg = fingernailseg(folder=folder)

print('create_unet')
#seg.create_unet()
seg.create_separable_unet()

print('fit');
seg.fit()

print('load_model)')
seg.load_model()
