import torch

# Define inputs
x = torch.tensor(2.0, requires_grad=True)
y = torch.tensor(4.0, requires_grad=True)

# Compute a function of x and y
z = x**2 + y**3

# Compute gradients: dz/dx and dz/dy
grads = torch.autograd.grad(
    outputs=z,                      # Tensors of which to compute gradients w.r.t. inputs
    inputs=[x, y],                  # Inputs to take derivative against
    grad_outputs=torch.tensor(7.0)  # Vector for Jacobian-vector product; 1.0 for simple gradient
)

print("dz/dx =", grads[0].item())
print("dz/dy =", grads[1].item())
