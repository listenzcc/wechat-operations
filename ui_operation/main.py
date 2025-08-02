"""
File: main.py
Author: Chuncheng Zhang
Date: 2025-08-02
Copyright & Email: chuncheng.zhang@ia.ac.cn

Purpose:
    Real time WeChat operation with uiautomation

Functions:
    1. Requirements and constants
    2. Function and class
    3. Play ground
    4. Pending
    5. Pending
"""


# %% ---- 2025-08-02 ------------------------
# Requirements and constants
import time
from uiautomation import WindowControl
from rich import print

# ! It requires the WeChat UI in active.
wx = WindowControl(Name='微信')
desktop = wx.GetParentControl()
print(desktop)
print(desktop.GetChildren())
exit(0)

wx.SwitchToThisWindow()
print(f'{wx=}')

print(wx.ListItemControl())

hw = wx.ListControl(Name='会话')
print(hw.GetChildren())
print(f'{hw=}')

# for e in hw.GetChildren():
#     e.Click(simulateMove=False)
#     print(e)
#     time.sleep(1)

exit(0)

while True:
    print('Reading...')
    we = hw.TextControl(searchDepth=4)

    while not we.Exists(0):
        # print('1')
        pass

    # print(f'{we=}')

    if we.Name:
        we.Click(simulateMove=False)
        msg = wx.ListControl(Name='消息').GetChildren()
        print(msg)


# %% ---- 2025-08-02 ------------------------
# Function and class


# %% ---- 2025-08-02 ------------------------
# Play ground


# %% ---- 2025-08-02 ------------------------
# Pending


# %% ---- 2025-08-02 ------------------------
# Pending
