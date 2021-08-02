import torch
import torchvision.transforms as transforms
import torch.nn as nn
from PIL import Image
import io

DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
# torch.manual_seed(777)
# if DEVICE == 'cuda':
#     torch.cuda.manual_seed_all(777)

MODEL_PATH ='D:\learn_flask\Practice_Flask\model.pth'
LABELS = [
    'combination',
    'dry',
    'oily',
    'sensitive'
]
model = None
model= torch.load(MODEL_PATH)
model.to(DEVICE)
model.eval()

mean=[0.485, 0.456, 0.406]
std=[0.229, 0.224, 0.225]

# albumentation으로 변경 고려
def transform_image(image_bytes):
    transform = transforms.Compose([
                            # transforms.Grayscale(num_output_channels=1),
                            transforms.Resize([300,300]),
                            transforms.ToTensor(),
                            # transforms.RandomHorizontalFlip(p=0.5),
                            # transforms.RandomVerticalFlip(p=0.5),  
                            transforms.Normalize(torch.Tensor(mean),torch.Tensor(std))
                            ])
    image = Image.open(io.BytesIO(image_bytes))
    image = transform(image).float()
    return image.unsqueeze(0)

def prediction(img_tensor, model):
    with torch.no_grad:
        output = model(img_tensor)
        _, predicted = torch.max(output.data, 1)
    return LABELS[predicted.item()]

