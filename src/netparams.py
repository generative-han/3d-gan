
'''
params.py

Managers of all hyper-parameters

'''

import torch
import torch_xla
import torch_xla.core.xla_model as xm

class net_params:
    """A Simple Class for managing 3DGAN params"""
    
    def __init__(self,epochs = 200,
        colab=False,
        batch_size = 16,
        soft_label = False,
        adv_weight = 0,
        d_thresh = 0.8,
        z_dim = 200,
        z_dis = "norm",
        model_save_step = 1,
        g_lr = 0.0025,
        d_lr = 0.00001,
        beta = (0.5, 0.999),
        cube_len = 64,
        leak_value = 0.2,
        bias = False):

        epochs = 200
        cloud_tpu=False
        batch_size = 8
        soft_label = False
        adv_weight = 0
        d_thresh = 0.8
        z_dim = 200
        z_dis = "norm"
        model_save_step = 1
        g_lr = 0.0025
        d_lr = 0.00001
        beta = (0.5, 0.999)
        cube_len = 64
        leak_value = 0.2
        bias = False

    def print_params():
        if cloud_tpu:
            device = dev = xm.xla_device()
        else:
            device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
        data_dir = '../volumetric_data/architecture/'
        output_dir = '../outputs'
        # images_dir = '../images'

        l = 16
        print (l*'*' + 'hyper-parameters' + l*'*')

        print ('epochs =', epochs)
        print ('batch_size =', batch_size)
        print ('soft_labels =', soft_label)
        print ('adv_weight =', adv_weight)
        print ('d_thresh =', d_thresh)
        print ('z_dim =', z_dim)
        print ('z_dis =', z_dis)
        print ('model_images_save_step =', model_save_step)
        print ('data =', data_dir)
        print ('device =', device)
        print ('g_lr =', g_lr)
        print ('d_lr =', d_lr)
        print ('cube_len =', cube_len)
        print ('leak_value =', leak_value)
        print ('bias =', bias)

        print (l*'*' + 'hyper-parameters' + l*'*')







