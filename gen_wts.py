from utils import torch_utils
import torch
from slim import attempt_load
import struct

# Initialize
device = torch_utils.select_device('0')
# Load model
print('-[INFO] loading model...')
model = attempt_load('last.pt', map_location=device)
# model = torch.load('last.pt', map_location=device)['model'].float().half()  # load to FP32
model.to(device).eval()
print('-[INFO] model loaded!')

print('-[INFO] converting model...')
f = open('yolov5m.wts', 'w')
f.write('{}\n'.format(len(model.state_dict().keys())))
for k, v in model.state_dict().items():
    vr = v.reshape(-1).cpu().numpy()
    f.write('{} {} '.format(k, len(vr)))
    for vv in vr:
        f.write(' ')
        f.write(struct.pack('>f',float(vv)).hex())
    f.write('\n')
