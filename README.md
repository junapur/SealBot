# 🦭 SealBot
A Discord bot for seal enjoyers.

<br>

## Self-Hosting Guide

### 1. Download the Images
You can download the images [here](https://drive.proton.me/urls/AX10JBT0ER#H0CnX5ZK1LDY).
It's 4,280 images, totalling around 2.8 GB.

### 2. Clone the Repository
```bash
git clone https://github.com/junapur/SealBot
```

### 3. Configure the Bot
Create a `settings.toml` file in the project's root directory 
and copy the following template:

```toml
[bot]
token = "..."
assets_dir = "path/to/downloaded/images"

[logging]
log_level = "INFO"
```

### 4. Discord Bot Setup

#### Create a Bot Application
1. Head to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application
3. Go to the `Bot` tab
4. Click `Reset Token` to generate your bot token
5. Copy the token and add it to your `settings.toml`

#### Bot Installation
1. In the Discord Developer Portal, head to the `Installation` tab
2. Under `Install Link`, select `Discord Provided Link`
3. In the `Default Install Settings` section:
   - Set `Guild Install` scopes to include `bot`
   - Under `Bot Permissions`, select:
     - `Send Messages`
     - `Attach Files`
4. Open the generated URL to add the bot to your server or your account's apps

### 5. Run the Bot
In the project's root directory, run:

```bash
uv run sealbot
```
