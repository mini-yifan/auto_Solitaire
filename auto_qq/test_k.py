import pyautogui
import time
import os
import pyperclip
import ctypes
import cv2

#pyautogui.FAILSAFE = False


#息屏时登录
def simulate_login(password):
    # 模拟点击回车键
    pyautogui.press('enter')

    # 等待一段时间，确保屏幕解锁界面响应
    time.sleep(0.7)

    # 逐字符输入密码
    for char in password:
        # 模拟按下按键
        ctypes.windll.user32.keybd_event(ord(char), 0, 0, 0)

        # 等待一段时间，以实现逐字符输入的效果
        time.sleep(0.1)  # 适当减小延迟时间

        # 模拟释放按键
        ctypes.windll.user32.keybd_event(ord(char), 0, 2, 0)

    # 模拟按下回车键
    ctypes.windll.user32.keybd_event(13, 0, 0, 0)

    # 模拟释放回车键
    ctypes.windll.user32.keybd_event(13, 0, 2, 0)


def find_and_click_qq_icon():
    # 获取屏幕尺寸
    screenWidth, screenHeight = pyautogui.size()

    # 定义任务栏的区域
    taskbar_region = (0, screenHeight - 50, screenWidth, screenHeight)  # 假设任务栏高度为30像素

    # 查找 QQ 图标
    icon_location = pyautogui.locateOnScreen('qq_icon.png', region=taskbar_region, grayscale=True, confidence=0.7)

    if icon_location is not None:
        # 获取图标的中心位置
        center = pyautogui.center(icon_location)
        print(f"Found QQ icon at {center}")

        # 点击图标
        pyautogui.click(center)
        print("Clicked on the QQ icon.")
        return True
    else:
        print("QQ icon not found.")
        return False


def find_and_move_to_image(image_filename, vertical_offset=200):
    # 获取屏幕尺寸
    screenWidth, screenHeight = pyautogui.size()

    # 查找图片
    image_location = pyautogui.locateOnScreen(image_filename, grayscale=False, confidence=0.6)

    if image_location is not None:
        # 获取图片的中心位置
        center = pyautogui.center(image_location)
        print(f"Found {image_filename} at {center}")

        # 计算新的鼠标位置（垂直向下 200 个像素）
        new_position = (center.x, center.y + vertical_offset)
        print(f"Moving mouse to {new_position}")

        # 移动鼠标到新的位置
        pyautogui.moveTo(new_position)
        print(f"Moved mouse to {new_position}")
    else:
        print(f"{image_filename} not found on the screen.")


def find_image_and_scroll(image_filename, max_attempts, num_vscroll, confidence, scroll_time):
    # 确保图片文件存在
    if not os.path.exists(image_filename):
        print(f"Please place the image file '{image_filename}' in the same directory as this script.")
        return False

    # 循环尝试查找图片
    for attempt in range(max_attempts):
        # 查找图片
        try:
            image_location = pyautogui.locateOnScreen(image_filename, grayscale=False, confidence=confidence)
            if image_location is not None:
                # 获取图片的中心位置
                center = pyautogui.center(image_location)
                print(f"Found {image_filename} at {center}")
                return center
        except:
            print(f"Attempt {attempt + 1}: {image_filename} not found. Scrolling down...")
            # 向下滑动一次滚轮
            pyautogui.vscroll(num_vscroll)
            time.sleep(scroll_time)  # 等待页面滚动完成
        '''
        if image_location is not None:
            # 获取图片的中心位置
            center = pyautogui.center(image_location)
            print(f"Found {image_filename} at {center}")
            return center
        else:
            print(f"Attempt {attempt + 1}: {image_filename} not found. Scrolling down...")
            # 向下滑动一次滚轮
            pyautogui.scroll(-1)
            time.sleep(0.5)  # 等待页面滚动完成
        '''
    print(f"{image_filename} not found after {max_attempts} attempts.")
    return None


def double_click_image_center(image_filename, max_attempts, num_vscroll, move=None, confidence=0.7, scroll_time=0.8):
    # 查找图片并获取中心位置
    center = find_image_and_scroll(image_filename, max_attempts=max_attempts, num_vscroll=num_vscroll, confidence=confidence, scroll_time=scroll_time)

    if center:
        time.sleep(0.8)
        if move is not None:
            # 计算新的鼠标位置（垂直向下 200 个像素）
            center = (center.x, center.y + move)
            # 移动鼠标到新的位置
            pyautogui.moveTo(center)
        # 双击图片中心位置
        pyautogui.doubleClick(center)
        print(f"Doubled clicked at {center}")
    else:
        print("Image not found.")


def perform_actions():
    # 获取当前鼠标位置
    current_mouse_x, current_mouse_y = pyautogui.position()

    # 在当前鼠标位置双击
    pyautogui.doubleClick(x=current_mouse_x, y=current_mouse_y)

    # 模拟 Ctrl+A 操作
    pyautogui.hotkey('ctrl', 'a')

    # 按下退格键
    pyautogui.press('backspace')

    # 模拟 Ctrl+V 操作
    pyautogui.hotkey('ctrl', 'v')


def read_file_and_copy_to_clipboard(filename):
    try:
        # 读取文件内容
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        # 将内容复制到剪贴板
        pyperclip.copy(content)
        print(f"Content from {filename} has been copied to clipboard.")
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


def move_mouse_to_left_center_and_click():
    # 获取屏幕的宽度和高度
    screenWidth, screenHeight = pyautogui.size()

    # 计算屏幕左侧中心的坐标
    left_center_x = 0  # 左侧边缘
    left_center_y = screenHeight // 2  # 屏幕高度的一半

    # 将鼠标移动到左侧中心位置
    pyautogui.moveTo(left_center_x, left_center_y)

    # 单击该位置
    pyautogui.click()

def main():
    #确保显示器未息屏
    try:
        find_and_move_to_image('windows.png')
    except:
        simulate_login("password")

    time.sleep(0.4)
    # 确保 QQ 图标的截图文件存在
    if not os.path.exists('qq_icon.png'):
        print("Please place the screenshot of the QQ icon in the same directory as this script.")
    else:
        # 查找并点击QQ图标
        c_qq = find_and_click_qq_icon()
        time.sleep(1)
        if c_qq:
            # 查找并移动到QQ头像下方
            find_and_move_to_image('my_qq_head.png')
            # 双击班级群图片
            double_click_image_center('jidian_benyan.png', max_attempts=10, num_vscroll=-200, scroll_time=0.4)
            time.sleep(0.3)
            # 查找并移动到对话框上方
            find_and_move_to_image('dialog_box.png', vertical_offset=-200)
            # 查找链接图片并双击
            double_click_image_center('lbq_link.png', max_attempts=40, num_vscroll=300, move=10, confidence=0.9, scroll_time=0.3)
            time.sleep(3)
            #查找并识别网站中的接龙按键并双击
            double_click_image_center('add_jielong.png', max_attempts=20, num_vscroll=-300)
            time.sleep(0.5)
            # 读取文件内容并复制到剪贴板
            read_file_and_copy_to_clipboard('t.txt')
            time.sleep(1)
            #在鼠标位置将剪贴板中的内容复制到输入框
            perform_actions()
            time.sleep(0.2)
            #添加循环以识别接龙中是否有剪贴板的内容
            for i in range(0, 10):
                try:
                    name_image_location = pyautogui.locateOnScreen('name_sh.png', grayscale=False, confidence=0.9)
                    break
                except:
                    double_click_image_center('add_jielong.png', max_attempts=20, num_vscroll=-300)
                    time.sleep(0.5)
                    perform_actions()
                    time.sleep(0.2)
            # 移动鼠标到左侧中心位置并点击,目的是完成接龙
            move_mouse_to_left_center_and_click()



if __name__ == "__main__":
    main()


