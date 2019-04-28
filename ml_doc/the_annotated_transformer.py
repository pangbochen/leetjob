# to generate the annotated tranformer

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import math, copy, time
from torch.autograd import Variable
import matplotlib.pyplot as plt
import seaborn


# the model architecture
class EncoderDecoder(nn.Module):
    """
    the standard encoder-decoder architecture
    base for this and many other models
    """
    def __init__(self, encoder, decoder, src_embed, tgt_embed, generator):
        super(EncoderDecoder, self).__init__()