import os                  # for getting environment variables
from slack_bolt import App # for making the app
from slack_bolt.adapter.socket_mode import SocketModeHandler # for socket, as I don't have a domain
import dotenv # for getting the environment variables from an env file

dotenv.load_dotenv() # load the env

app = App(
    token=os.environ["SLACK_BOT_TOKEN"] # create the app
)


@app.command("/impersonate") # that one function.
def impersonate(ack, command, client, respond):
    ack()
    uti = command["text"].split(" ")[0].replace("@", "") # UTI: USER TO IMPERSONATE :)
    msg = command["text"].split(' ', 1)[1]               # Everything that isn't the UTI

    print(uti) # debug stuff

    channel_id = command["channel_id"] # get the channel.

    result = client.conversations_members(channel=channel_id) # get all the users in the channel

    for user_id in result["members"]: # for each id in that list,
        user = client.users_info(user=user_id)["user"] # find the user with that id
        if uti in user["name"]: # if the id matches up with the User we want to impersonate
            utiid = user_id # set the UTI-ID to that user's id
            utiimg = user["profile"]["image_192"] # get the image of the user
            utiname = user["profile"]["display_name"] # and get the name.
            break # and stop. We don't need to look any further.

    if utiid: # dunno why I set up the code like this, but I did.
        client.chat_postMessage( # send the message. 
            channel=command["channel_id"],
            text=msg,
            icon_url=utiimg, # set the bot's picture
            username=utiname # set the bot's username
        )
    else:
        respond( # send an error.
            text="That user isn't in this channel.",
            response_type="ephemeral"
        )


if __name__ == "__main__":
    SocketModeHandler(   # start the bot.
        app,
        os.environ["SLACK_APP_TOKEN"]
    ).start()