# Task 19 - Training Loop Internals

This task explores the mechanics behind neural-network training in PyTorch.

## Topics covered

- Manual implementations of MSE, cross-entropy, and L1 losses, verified against PyTorch.
- SGD and Adam optimizers implemented from scratch and compared with `torch.optim`.
- Mini-batching with datasets and data loaders.
- Learning-rate scheduling, gradient accumulation, `zero_grad`, and gradient clipping.
- Controlled experiments showing how loss functions, optimizers, batch size, and schedules affect training.
