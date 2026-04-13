import cv2
import numpy as np


def create_background(width: int, height: int, color: np.ndarray = np.array([255, 255, 255])) -> np.ndarray:
    bg = np.full((height, width, 3), color, dtype=np.uint8)
    return bg


def create_square(frame: np.ndarray, center: tuple, width: int,
                  color: np.ndarray = np.array([255, 255, 0])) -> np.ndarray:
    frame[center[0]-width//2:center[0]+width//2, center[1]-width//2:center[1]+width//2] = color
    return frame


T, H, W = 200, 1080, 1920

fps = 30
height, width = H, W

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output_from_array.mp4', fourcc, fps, (width, height))

frames = list()
for tick in range(T):
    frame = create_background(W, H)
    frame = create_square(frame, center=(100, 200), width=50)
    out.write(frame)

out.release()
print("视频已成功从 NumPy 数组写入！")
