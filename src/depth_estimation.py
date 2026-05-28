import torch
import cv2

def load_model():
    model = torch.hub.load("intel-isl/MiDaS", "MiDaS_small")
    model.eval()

    transform = torch.hub.load("intel-isl/MiDaS", "transforms").small_transform

    return model, transform


def predict_depth(image, model, transform):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    img = cv2.resize(img, (320, 240))

    input_batch = transform(img)

    if len(input_batch.shape) == 3:
        input_batch = input_batch.unsqueeze(0)

    with torch.no_grad():
        prediction = model(input_batch)
        prediction = torch.nn.functional.interpolate(
            prediction.unsqueeze(1),
            size=img.shape[:2],
            mode="bicubic",
            align_corners=False,
        ).squeeze()

    depth = prediction.cpu().numpy()
    return depth