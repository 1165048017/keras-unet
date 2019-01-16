import sys
from utils import *
if len(sys.argv)>1:
  folder = sys.argv[1]
else:
  folder = 'headshoulderdata'

print('folder found=',folder)
seg = fingernailseg(folder=folder)

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

print('fit');
seg.fit()

print('load_model)')
seg.load_model()
