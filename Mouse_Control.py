import pyautogui

x_dim, y_dim = pyautogui.size()
smooth_x, smooth_y = 0.5, 0.5

def moveto(xylist):
    raw_x, raw_y = xylist
    
    global smooth_x
    global smooth_y
    
    smooth_x += 0.5 * (raw_x - smooth_x)
    smooth_y += 0.5 * (raw_y - smooth_y)
    
    x = smooth_x
    y = smooth_y
    
    y = 1 - y
    x *= x_dim
    y *= y_dim
    
    x = min(x_dim - 10, max(10, x))
    y = min(y_dim - 10, max(10, y))
    
    pyautogui.moveTo(x, y)

