import requests
import json
import datetime
import shutil

user_id = input("Enter the user ID: ")

headers = {
    "Authorization": "MTAzNzAyMTU4OTA1ODg5OTk2OA.G26J6T.TFe_3vc8cNTN2wJLjNFBRiKWee7IIyKuvrbJPM"
}

if not user_id.isdigit():
    print("Error: Invalid user ID.")
    exit()

response = requests.get(f"https://discord.com/api/users/{user_id}", headers=headers)

if response.status_code != 200:
    print("Error: Failed to fetch user information.")
    exit()

user_data = json.loads(response.text)

username = user_data["username"] + "#" + user_data["discriminator"]
avatar_url = f"https://cdn.discordapp.com/avatars/{user_id}/{user_data['avatar']}"
banner_url = f"https://cdn.discordapp.com/banners/{user_id}/{user_data['banner']}" if user_data['banner'] else None

created_at_unix = ((int(user_id) >> 22) + 1420070400000) / 1000
created_at = datetime.datetime.fromtimestamp(created_at_unix).strftime("%Y-%m-%d %H:%M:%S")


print("User ID:", user_id)
print("Username:", username)
print("Avatar URL:", avatar_url)
print("Banner URL:", banner_url)
print("Account created at:", created_at)

save_option = input("Would you like to save the profile picture to your device? (y/n): ")

if save_option.lower() == "y":
    with open(f"{username}_profile_picture.png", "wb") as file:
        response = requests.get(avatar_url)
        file.write(response.content)
        print("Profile picture saved successfully!")
        
if banner_url:
    save_banner_option = input("Would you like to save the banner picture to your device? (y/n): ")
    if save_banner_option.lower() == "y":
        with open(f"{username}_banner_picture.gif", "wb") as file:
            response = requests.get(banner_url)
            file.write(response.content)
            print("Banner picture saved successfully!")

