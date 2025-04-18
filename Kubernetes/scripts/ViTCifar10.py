from torchvision.datasets import CIFAR10
from torchvision.models import vit_b_16, ViT_B_16_Weights
from torch.utils.data import DataLoader
from sklearn.metrics import precision_recall_fscore_support as evaluate
from torch import nn
import torch
import os

# get number of jobs and epochs from the environment
TORCH_NUM_JOBS = int(os.environ.get("TORCH_NUM_JOBS", "4"))
TORCH_NUM_EPOCHS = int(os.environ.get("TORCH_NUM_EPOCHS", "1"))

cifar10_train = CIFAR10(root="~/data", download=True, train=True, transform=ViT_B_16_Weights.IMAGENET1K_V1.transforms())

train_data_loader = DataLoader(cifar10_train,
                               batch_size=32,
                               shuffle=True,
                               num_workers=TORCH_NUM_JOBS)

model = vit_b_16(weights=ViT_B_16_Weights.IMAGENET1K_V1)

# set output neurons to Num Classes = 10
model.heads[0] = nn.Linear(768, 10)

# freeze the backbone
model.encoder.requires_grad_(False)

# create opt and loss
optimizer = torch.optim.Adam(model.parameters(), lr=0.0001)
loss_function = nn.CrossEntropyLoss()

model.cuda()
model.train()

for epoch in range(TORCH_NUM_EPOCHS):
    print("*" * 20 + f"\nEpoch {epoch+1} / {TORCH_NUM_EPOCHS}")
    epoch_loss = 0
    epoch_correct = 0
    
    for i, (data, labels) in enumerate(train_data_loader):
        data = data.cuda()
        labels = labels.cuda()
        
        optimizer.zero_grad()
        model_outputs = model(data)
        
        loss = loss_function(model_outputs.float(), labels.long())
        
        if torch.isnan(loss):
            raise RuntimeError("Loss reached NaN!")
        
        loss.backward()
        optimizer.step()
            
            
        _, predictions = torch.max(model_outputs, 1)
        epoch_correct += torch.sum(predictions == labels)        
        epoch_loss += loss.item()
        if i > 0 and (i % (len(train_data_loader) // 10) == 0 or i == 1):
            print(f"{i} / {len(train_data_loader)}"
                  f"\tLoss = {epoch_loss / i:.2f}"
                  f"\tAcc = {epoch_correct:d} / {i * train_data_loader.batch_size} "
                  f"({epoch_correct / (i * train_data_loader.batch_size) * 100:.1f}%)", flush=True)
        
    print(f"Loss = {epoch_loss / len(train_data_loader):.4f}")
    print(f"Train Acc = {epoch_correct / len(cifar10_train) * 100:.2f}%") 
    
cifar10_test = CIFAR10(root="~/data", download=True, train=False, transform=ViT_B_16_Weights.IMAGENET1K_V1.transforms())

test_data_loader = DataLoader(cifar10_test,
                              batch_size=32,
                              shuffle=False,
                              num_workers=TORCH_NUM_JOBS)

model.eval()

predictions = []
labels = []
with torch.no_grad():
    print("*" * 20 + f"\nRunning Eval")
    for i, (data, lb) in enumerate(test_data_loader):
        
        model_outputs = model(data.cuda())

        _, preds = torch.max(model_outputs, 1)

        labels.extend(lb.numpy().tolist())
        predictions.extend(preds.cpu().numpy().tolist())
        if i > 0 and i % (len(test_data_loader) // 10) == 0:
            print(f"{i} / {len(test_data_loader)}", flush=True)



prec, rec, fscore, _ = evaluate(predictions, labels, average="macro")

print("*" * 20 + f"""\n
Precision  \t{prec*100:.2f}%
Recall  \t{rec*100:.2f}%
F-1 Score \t{fscore*100:.2f}%
""")