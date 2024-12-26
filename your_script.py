import time
from pyrogram import Client, errors

# Replace these with your own API details
api_id = 24271143  # Get this from https://my.telegram.org
api_hash = "27be842cb506de9b5520146dfd0ba299"

# Replace with your channel username
channel_username = "texttff"  # Example: "mychannel"

# Create a Pyrogram Client
app = Client("my_account", api_id=api_id, api_hash=api_hash)

# Function to add user to the channel
def add_user_to_channel(user_to_add):
    with app:
        try:
            app.add_chat_members(chat_id=channel_username, user_ids=user_to_add)
            print(f"Successfully added {user_to_add} to the channel {channel_username}.")
        except errors.UserNotMutualContact:
            print(f"Cannot add {user_to_add}: User is not a mutual contact.")
        except errors.ChatAdminRequired:
            print("You must be an admin of the channel to add users.")
        except errors.PeerIdInvalid:
            print("Invalid user or channel. Check the details provided.")
        except errors.UserPrivacyRestricted:
            print(f"Cannot add {user_to_add}: User's privacy settings restrict this action.")
        except Exception as e:
            print(f"An error occurred: {e}")

# Read usernames from the text file
with open('members_list.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        # Extract username from the line
        if "Username: " in line:
            username = line.split("Username: ")[1].split(",")[0].strip()
            # Skip if the username is "No Username"
            if username.lower() == "no username":
                continue
            # Add user to the channel
            add_user_to_channel(username)
            # Wait for 30 seconds before adding the next user
            time.sleep(200)  # Increase this delay if needed
