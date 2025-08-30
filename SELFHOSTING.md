# Self-Hosting Guide
This guide will walk you through the process of self-hosting your own instance of SealBot.


### 1. Download Assets
First, you need to download the image assets the bot uses.

- [Download Here.](https://drive.proton.me/urls/AX10JBT0ER#H0CnX5ZK1LDY)
- The download contains 4,280 images and is approximately **2.8 GB**.


### 2. Clone the Repository
Next, clone the source code from GitHub to your local machine.

```bash
git clone https://github.com/junapur/SealBot
```


### 3. Configure the Bot
You'll need to create a configuration file to store your bot's token and settings.

1.  Create a new file named `settings.toml` in the root directory of the cloned project.
2.  Copy and paste the following template into the file:

```toml
[bot]
# Your secret bot token from the Discord Developer Portal
token = "..." 

# The full path to the directory where you downloaded the images
assets_dir = "path/to/downloaded/images"

[logging]
log_level = "INFO"
```


### 4. Set Up Your Discord Application
Follow these steps to create a Discord bot application and get your token.

#### Create the Application
1.  Navigate to the **[Discord Developer Portal](https://discord.com/developers/applications)**.
2.  Click the **New Application** button and give your bot a name.
3.  Go to the **Bot** tab in the left-hand menu.
4.  Click the **Reset Token** button to generate a new token.
5.  Copy this token and paste it into the `token` field in your `settings.toml` file.

#### Generate an Installation Link
1. In the Discord Developer Portal, head to the **Installation** tab.
2. Under **Install Link**, select **Discord Provided Link**.
3. In the **Default Install Settings** section:
   - Set **Guild Install** scopes to include `bot`.
   - Under **Bot Permissions**, select:
     - `Send Messages`
     - `Attach Files`
4. Open the generated URL to add the bot to your server or your account's apps.


### 5. Run the Bot
Finally, start the bot. Make sure you are in the project's root directory in your terminal.

```bash
uv run sealbot
```

Your bot should now be online and ready to use! If you experience any issues, please let me know.
