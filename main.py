import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import dotenv

dotenv.load_dotenv()

app = App(
    token=os.environ["SLACK_BOT_TOKEN"]
)


@app.command("/impersonate")
def impersonate(ack, command, client, respond):
    ack()
    uti = command["text"].split(" ")[0].replace("@", "") # UTI: USER TO IMPERSONATE :)
    msg = command["text"].split(' ', 1)[1]

    print(uti)

    channel_id = command["channel_id"]

    result = client.conversations_members(channel=channel_id)

    for user_id in result["members"]:
        print(user_id)
        user = client.users_info(user=user_id)["user"]
        print(user["name"])
        if uti in user["name"]:
            utiid = user_id
            utiimg = user["profile"]["image_192"]
            utiname = user["profile"]["display_name"]
            print(utiimg)
            break

    if utiid:
        client.chat_postMessage(
            channel=command["channel_id"],
            text=msg,
            response_type="ephemeral",
            icon_url=utiimg,
            username=utiname
        )
    else:
        respond(
            text="That user isn't in this channel.",
            response_type="ephemeral"
        )


if __name__ == "__main__":
    SocketModeHandler(
        app,
        os.environ["SLACK_APP_TOKEN"]
    ).start()