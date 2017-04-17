# ASF Naive Web UI

### 如何使用
1. 需要安装 Python 2 以及 web.py 库；
2. Linux 需要安装 mono；
3. 自己去看 [ASF 的文档](https://github.com/JustArchi/ArchiSteamFarm)，把 ASF 装好，自己跑一下试试，看看能不能跑起来，需不需要额外的密令啥的；
4. 确定能跑起来，关了；
5. [找到自己的 steamID](https://steamcommunity.com/sharedfiles/filedetails/?id=209000244)，只要第二个冒号后的数字部分；
6. 修改 `ASF.json`，把 `Headless` 改成 `true`，把 `SteamOwnerID` 后面的 0 改成刚才找到的自己的 Steam ID；
7. 到 ASF.exe 所在目录下，，执行 `git clone https://github.com/MrWhoami/ASF-Naive-WUI.git`；
8. Linux 执行 `mono ASF.exe --server`，Windows 执行 `ASF.exe --server`
8. 执行 `python ASF-Naive-WUI/index.py 9563`；
9. 访问你的服务器的 IP 的 9563 端口即可。
