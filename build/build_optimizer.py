# @Time    : 2022/9/14 20:17
# @Author  : PEIWEN PAN
# @Email   : 121106022690@njust.edu.cn
# @File    : build_optimizer.py
# @Software: PyCharm
from torch.optim import *


# TODO Solve the problem that **kwargs cannot be passed
def build_optimizer(model, cfg):
    optimizer_name = cfg.optimizer['type']
    optimizer_class = globals()[optimizer_name]
    optimizer = optimizer_class(model.parameters(), **cfg.optimizer['setting'])
    return optimizer
