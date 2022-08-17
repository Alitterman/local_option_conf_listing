# 这是一个示例 Python 脚本。
import Loader
import Obj_B

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def main():
    B = Obj_B.B()
    C = Obj_B.C()
    # 在下面的代码行中使用断点来调试脚本。
    loader = Loader.Loader("./", "1312.json", B, C)


# 按间距中的绿色按钮以运行脚本。
if __name__ == "__main__":
    main()

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
