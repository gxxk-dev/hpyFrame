# HPYF-bootselect 2025 Gxxk
# 在boot.py运行阶段供用户选择加载项并保持运行性能
# 本模块是hPyFrame(HPYF)的一部分。
# HPYF是自由软件，按照AGPL v3+进行许可。
# AGPL v3+(指 AGPL V3-or-later):https://www.gnu.org/licenses/agpl.txt

# 模块导入
from ssd1106 import SSD1106_I2C
from machine import I2C,Pin,Timer
from time import sleep
from os import rename

# OLED屏幕
Oled=SSD1106_I2C(128,64,I2C(0, scl=Pin(Pin.P19), sda=Pin(Pin.P20), freq=400000),60)
Oled.fill(0)
Oled.text("will start hPyFrame in 1s",0,0)
Oled.text("if u want2entry main.py,press buttonA&B plz",0,8)
Oled.show()
oled.fill(0)


buttonStat=[0,0]
def ButtonStatChange(source:int)->None:
    global buttonStat
    buttonStat[source]=True
ButtonA = Pin(0,Pin.IN,Pin.PULL_UP)
ButtonA.irq(trigger=Pin.IRQ_FALLING,handler=lambda:ButtonStatChange(0))
ButtonB = Pin(2,Pin.IN,Pin.PULL_UP)
ButtonB.irq(trigger=Pin.IRQ_FALLING,handler=lambda:ButtonStatChange(1))
sleep(1)
buttonStat=buttonStat[0] and buttonStat[1]

if buttonStat:
    print("[boot.py]正常进入main.py")
else:
    rename("main.py","main.py.bak")
    rename("HPYFLoader.py","main.py")

def TimerCallback(RestoreFileName:bool)->None:
    # 对象销毁 IRQ回调注销
    ButtonA.irq(handler=None);ButtonB.irq(handler=None)
    del Oled,SSD1106_I2C,I2C,Timer,Pin,sleep,ButtonStatChange,ButtonA,ButtonB,TimerCallback
    if RestoreFileName: #本段是在main.py下运行的 故重命名后无影响
        rename("main.py","HPYFLoader.py")
        rename("main.py.bak","main.py")
    del rename
    __import__("gc").collect() 
    # 我轻轻的走了 正如我轻轻的来

Timer(0).init(period=1500, mode=Timer.ONE_SHOT, callback=lambda:TimerCallback(buttonStat))