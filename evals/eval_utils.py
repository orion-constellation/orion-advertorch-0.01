import numpy as np
import matplotlib as plt 

def tensor2npimg(tensor):
    return bchw2bhwc(tensor[0].cpu().numpy())
 
def _show_images(enhance=127):
    np_advimg = tensor2npimg(advimg)
    np_perturb = tensor2npimg(advimg - img)
 
    pred = imagenet_label2classname(predict_from_logits(model(img)))
    advpred = imagenet_label2classname(predict_from_logits(model(advimg)))
 
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 3, 1)
    plt.imshow(np_img)
    
    plt.axis("off")
    plt.title("original image\n prediction: {}".format(pred))
    plt.subplot(1, 3, 2)
    plt.imshow(np_perturb * enhance + 0.5)
    
    plt.axis("off")
    plt.title("The perturbation")
    plt.subplot(1, 3, 3)
    plt.imshow(np_advimg)
    plt.axis("off")
    plt.title("Perturbed image\n prediction: {}".format(advpred))
    plt.show()

adversary = L2PGDAttack(
    model, eps=1., eps_iter=1.*2/40, nb_iter=40,
    rand_init=False, targeted=False)
#advimg = adversary.perturb(img, label)
_show_images()
#And here is the result,