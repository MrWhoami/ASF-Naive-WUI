# ANW
## Description
ANW is an [Archi Steam Farm](https://github.com/JustArchi/ArchiSteamFarm) Naive Web UI.

## Features
* Can run with python itself or wsgi.
* Can run on Windows or Linux.
* Manage multi users through Web UI.
* Display current farming, games to farm and time remaining.
* Start and stop bots.
* Login by 2FA code or email code through Web UI. (Experimental)

## Dependencies
* ASF
* Python 2.7
* web.py
* mono (Linux and macOS)

## How to Use
### Python server
1. Check dependencies.
2. Modify `config.json`.
3. Create your own configuration by copy `static/template.json` into `username.json`, in which `username` is user defined.
4. Modify `username.json`. You may need to fill in `SteamLogin`, `SteamPassword` and `WUIPassword`.
5. Move `username.json` under the `config` folder of ASF.
6. Configurate the ASF according to its wiki.
7. Start ASF.
8. `python index.py`
9. You can login your website:8080 with `username` and `WUIPassword`.
