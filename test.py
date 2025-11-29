import torch

print("PyTorch version:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())  # AMD GPU → False

x = torch.rand(3,3)
print(x)
