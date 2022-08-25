# Drama-Notifier
Get notification of the latest episode of your current watching drama in ur telegram group.

Pulls info from "Dramacool" website.

## Requirements:-
1. Any Cloud Server or Home Server (on Raspberry Pi or old pc) or anything like that. You can try it on Termux idk.
2. Some basic knowledge about `linux directories` and `crontab` and `.bashrc (optional)`.

## Dependencies:-
1. Python 3
2. bs4 library
3. requests library

### Following documentation is not completely noob friendly. Btw I am also in level- 'noob+1'.

* You can manually input drama url in `current_drama` file or use `.bashrc` to add an alias. (Change /path/to/file/)
```
alias drama_url='/usr/bin/python /user/Path_to_folder/Drama_Notifier/url_input.py > /user/Path_to_folder/Drama_Notifier/current_drama'
```
* Use `BotFather` to create a bot that will get you the updates. Use [this](https://youtu.be/ps1yeWwd6iA "Telegram and Python - Automate sending messages to Telegram Groups Using Python") video for help.
   * You need to change the bot id and chat id in `notify.py`
* Automate the script using crontab. Runs every 5 minute. (Change /path/to/file/)
```
*/15 * * * * bash /user/Path_to_folder/Drama_Notifier/drama_alert.sh
```
* Following /path/to/file/ is to be changes as per your need.
  * In `drama_alert.sh`
  ```
  cd /user/Path_to_folder/Drama_Notifier/
  ```
  * In `notify.py`
  ```
  update= open('/user/Path_to_folder/Drama_Notifier/firstScrape', 'r').read()
  ```
  * In `scraper.py`
  ```
  url = open('/user/Path_to_folder/Drama_Notifier/current_drama', 'r').read()
  ```
#### Screenshot Preview

![drama_notifier_preview](https://user-images.githubusercontent.com/72310402/186623879-7b5407bc-36ff-4471-8788-2d3c6976a064.PNG)

#### That's it.
You can use it however you want.

#### Credits:-
This was completed with the help of - https://github.com/abhayruparel/website-change-notifier

