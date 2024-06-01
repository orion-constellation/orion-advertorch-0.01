"""
https://analyticsindiamag.com/a-guide-to-advertorch-python-toolbox-for-adversarial-robustness/

EXAMPLE TAKEN FROM ABOVE SITE FOR IMPLEMENTATION REFERENCE GUIDE.

"""
from .evals.eval_utils import tensor2npimg, _show_images 
# install torch
#! pip install torch==1.3.0 torchvision==0.4.1
 
# install library
#! pip install advertorch

import torch
import torch.nn as nn
from torchvision.models import vgg16
 
# preprocessing dependencies
from advertorch.utils import predict_from_logits
from advertorch_examples.utils import ImageNetClassNameLookup
from advertorch_examples.utils import get_panda_image
from advertorch_examples.utils import bhwc2bchw
from advertorch_examples.utils import bchw2bhwc
 
# load the attack class
from advertorch.attacks import L2PGDAttack
from .libs.custom_loggers.logging.setup_logger as _logger
_logger.info("Test") 
 
device = "mps" if torch.backends.mps.is_available() else "cpu"

#Here we are going to perform an attack on a pre-trained transfer learning model called VGG16 
# #with its pre-trained weights for the ImageNet competition. 

# load the model
model = vgg16(pretrained=True)
model.eval()
model = nn.Sequential(model)
model = model.to(device)
#Now we’ll load the image and associated label that later be used to check the severity of the attack.

# load the image and index for true label
np_img = get_panda_image()
img = torch.tensor(bhwc2bchw(np_img))[None, :, :, :].float().to(device)
label = torch.tensor([388, ]).long().to(device) # true label
imagenet_label2classname = ImageNetClassNameLookup()