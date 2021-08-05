import torch
import torchvision.transforms as transforms
from PIL import Image
import io

DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
# torch.manual_seed(777)
# if DEVICE == 'cuda':
#     torch.cuda.manual_seed_all(777)


LABELS = [
    'combination',
    'dry',
    'oily',
    'sensitive'
]



mean=[0.485, 0.456, 0.406]
std=[0.229, 0.224, 0.225]

transform = transforms.Compose([
                        # transforms.Grayscale(num_output_channels=1),
                        transforms.Resize([300,300]),
                        transforms.ToTensor(),
                        # transforms.RandomHorizontalFlip(p=0.5),
                        # transforms.RandomVerticalFlip(p=0.5),  
                        transforms.Normalize(torch.Tensor(mean),torch.Tensor(std))
                        ])

# albumentation으로 변경 고려
def transform_image(image_location):
    # image = Image.open(io.BytesIO(image_bytes))
    image = Image.open(image_location)
    image = transform(image).unsqueeze(0).to(DEVICE)
    return image

def prediction(img_tensor, model):
    # with torch.no_grad:
    output = model(img_tensor)
    _, predicted = torch.max(output.data, 1)
    return LABELS[predicted.item()]

