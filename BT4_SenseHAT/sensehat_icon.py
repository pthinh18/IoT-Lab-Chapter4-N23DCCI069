from sense_emu import SenseHat
import time

sense = SenseHat()

# Định nghĩa màu
r = [255, 0, 0]    # Đỏ
b = [0, 0, 0]      # Tắt (đen)
w = [255, 255, 255] # Trắng (Làm hiệu ứng bóng sáng)

# Trái tim 8x8 (Tự thiết kế)
heart = [
    b, r, r, b, b, r, r, b,
    r, r, w, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    b, r, r, r, r, r, r, b,
    b, b, r, r, r, r, b, b,
    b, b, b, r, r, b, b, b,
    b, b, b, b, b, b, b, b,
]

sense.set_pixels(heart)
print('Biểu tượng Trái Tim đã hiển thị.')
time.sleep(5)
sense.clear()
