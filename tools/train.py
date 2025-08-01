from ultralytics import YOLO
import torch

if __name__ == '__main__':
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f'Using device: {device}')

    model = YOLO('yolo11n.pt').to(device)

    model.train(
        data='dataset.yaml',
        epochs=100,
        imgsz=640,
        batch=16,
        project='../../models',
        name='version name',
        save=True,
        verbose=True
    )