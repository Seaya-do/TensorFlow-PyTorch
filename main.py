#텐서1.py
import torch
import numpy as np

data = [[1, 2],[3, 4]]
x_data = torch.tensor(data)
print(x_data)

np_array = np.array(data)
x_np = torch.from_numpy(np_array)

print(x_np)

#이미 있는 텐서를 이용해 생성하기
x_ones = torch.ones_like(x_data) # x_data의 속성을 유지합니다.
print(f"Ones Tensor: \n {x_ones} \n")

#명시적으로 재정의(override)하지 않는다면, 인자로 주어진 텐서의 속성(모양(shape),
#자료형(datatype))을 유지합니다.
x_rand = torch.rand_like(x_data, dtype=torch.float) # x_data의 속성을 덮어씁니다.
print(f"Random Tensor: \n {x_rand} \n")


