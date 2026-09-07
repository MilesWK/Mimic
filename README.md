# <div align=center>Mimic</div>
<div align=center>Research slack bot for impersonating other users.</div>

> [!CAUTION]
> This bot is for research purposes only. It also isn't 100% perfect at impersonating users. The author can not be held responsible for usage of this bot

<img width="365" height="108" alt="image" src="https://github.com/user-attachments/assets/57e8283d-c09c-4c92-8d62-76f485c7dcef" />


## How this works: 
This slack bot uses the Slack API to lookup the ID of the requested user, get the image url and display name of that user, and then send a message with that information. Because it is a bot, the `app` icon will always remain visible, insuring that an impersonation is decipherable. 

## How to run it locally

1. Clone this repository and enter the `app` directory
2. In the directory, run `pip install -r requirements.txt` to install the required libraries
3. Create a new slack app using `manifest.json` and install it in the desired workspace. 
4. in the app directory following `.env-example`, create an `.env` file with your bots Bot token, app token, and signing secret. 
5. Run `main.py`
6. Run `/mimic` followed by mentioning the user you want to mimic and the message you want to send.
