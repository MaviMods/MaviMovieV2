<p align="center">
  <img src="https://telegra.ph/file/504babe67ae701cb458f8.jpg" alt="Mavi Mavi Logo">
</p>
<h1 align="center">
  <b> Mavi Movie V2 </b>
</h1>

## ⚡️Features
- [x] Auto Filter
- [x] Manual Filter
- [x] IMDB
- [x] Admin Commands
- [x] Broadcast
- [x] Index
- [x] IMDB search
- [x] Inline Search
- [x] Random pics
- [x] ids and User info 
- [x] Stats, Users, Chats, Ban, Unban, Leave, Disable, Channel
- [x] Spelling Check Feature
- [x] File Store

## Variables

Read [this](https://telegram.dog/LazyDevelopers/8) before you start messing up with your edits.

### Required Variables
* `BOT_TOKEN`: Create a bot using [@BotFather](https://telegram.dog/BotFather), and get the Telegram API token.
* `API_ID`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `API_HASH`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `CHANNELS`: Username or ID of channel or group. Separate multiple IDs by space
* `ADMINS`: Username or ID of Admin. Separate multiple Admins by space
* `DATABASE_URI`: [mongoDB](https://www.mongodb.com) URI. Get this value from [mongoDB](https://www.mongodb.com).
* `DATABASE_NAME`: Name of the database in [mongoDB](https://www.mongodb.com).
* `LOG_CHANNEL` : A channel to log the activities of bot. Make sure bot is an admin in the channel.
* `REQ_CHANNEL`: Channel ID where logs of requested content is to be sent.
* `PICS`: Telegraph links of images to show in start message.( Multiple images can be used separated by space )
* `FILE_STORE_CHANNEL`: Channel from were file store links of posts should be made.Separate multiple IDs by space
* `LAZY_MODE`: True or False . If true then bot will rename files else it will not rename.
* `LAZY_RENAMERS`: ID of the users to which you want to give file renaming authentication. Separate multiple ids by space.
* `REQ_CHANNEL`: ID of the channel where you want to send request logs.
* `URL_MODE`: True or False. If true then bot will use url shortner.
* `URL_SHORTENR_WEBSITE`: Name of the url shortner website.
* `URL_SHORTNER_WEBSITE_API`: API ID of the url shortner website.
* `LZURL_PRIME_USERS`: IDs of the users who you don't want to use url. Separate multiple ids by space
* `LAZY_GROUPS`: IDs of the groups where you don't want bot to use url. Separate multiple ids by space
* `MY_USERS`: ID of the users to which you want to give file sharing authentication for private files. Separate multiple ids by space.
* `FQDN`: Domain name of your currently deployed bot.
* `PRIME_DOWNLOADERS`: ID of the users to which you want to give file uploading using url. Separate multiple ids by space.


* Check [info.py](https://github.com/MaviMods/MaviMovieV2/blob/master/info.py) for more


## Deploy
You can deploy this bot anywhere.


<a target="_blank" href="https://app.koyeb.com/deploy?type=git&repository=github.com/MaviMods/MaviMovieV2&branch=master&name=lazyprincessbot"><img alt="Deploy to Koyeb" src="https://binbashbanana.github.io/deploy-buttons/buttons/remade/koyeb.svg"></a>


<details><summary>Deploy To Heroku</summary>
<p>
<br>
<a href="https://heroku.com/deploy?template=https://github.com/MaviMods/MaviMovieV2">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">
</a>
</p>
</details>

<details><summary>Deploy To VPS</summary>
<p>
<pre>
git clone https://github.com/MaviMods/MaviMovieV2
# Install Packages
pip3 install -U -r requirements.txt
Edit info.py with variables as given below then run bot
python3 bot.py
</pre>
</p>
</details>


## Commands
```
• /logs - to get the rescent errors
• /stats - to get status of files in db.
* /filter - add manual filters
* /filters - view filters
* /connect - connect to PM.
* /disconnect - disconnect from PM
* /del - delete a filter
* /delall - delete all filters
* /deleteall - delete all index(autofilter)
* /delete - delete a specific file from index.
* /info - get user info
* /id - get tg ids.
* /imdb - fetch info from imdb.
• /users - to get list of my users and ids.
• /chats - to get list of the my chats and ids 
• /index  - to add files from a channel
• /leave  - to leave from a chat.
• /disable  -  do disable a chat.
* /enable - re-enable chat.
• /ban  - to ban a user.
• /unban  - to unban a user.
• /channel - to get list of total connected channels
• /broadcast - to broadcast a message to all LazyPrincess users
• /batch - to create link for multiple posts
• /link - to create link for one post
• /set_caption - to set new custom caption #renaming_feature
• /del_caption - To delete custom caption #renaming_feature
• /set_thumb or /st - To set custom thumbnail #renaming_feature
• /set_lazy_thumb or /slt - To set custom thumbnail #url_downloading_feature
• /view_thumb or /vt - To view custom thumbnail #renaming_feature
• /view_lazy_thumb or /vlt - To view custom thumbnail #url_downloading_feature
• /del_thumb or /dt - To delete custom thumbnail #renaming_feature
• /del_lazy_thumb or /dlt - To delete custom thumbnail #url_downloading_feature

```
## Support
[![telegram badge](https://img.shields.io/badge/Telegram-Group-30302f?style=flat&logo=telegram)](https://telegram.dog/LazyPrincessSupport)
[![telegram badge](https://img.shields.io/badge/Telegram-Channel-30302f?style=flat&logo=telegram)](https://telegram.dog/LazyDeveloper)

## Credits 
* [![LazyPrincess-Devs](https://img.shields.io/static/v1?label=LazyPrincess&message=devs&color=critical)](https://telegram.dog/LazyDeveloper)


## Thanks to 
 - Thank you [LazyDeveloper](https://github.com/LazyDeveloperr) for helping us in this journey ❤
