import vugrad as vg
import numpy as np


a = vg.TensorNode(np.random.randn(2,2))
b = vg.TensorNode(np.random.randn(2,2))

c = a + b