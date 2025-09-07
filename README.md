# Discover Weekly Saver

🎵 **Automatically save your Spotify Discover Weekly playlist to prevent losing great music recommendations!**

This Python script finds your current Discover Weekly playlist and saves all songs to a permanent "Discover Weekly Collection" playlist, ensuring you never lose track of amazing music discoveries.

## ✨ Features

- 🔍 **Automatic Discovery**: Finds your Discover Weekly playlist automatically
- 📚 **Master Collection**: Creates and maintains a "Discover Weekly Collection" playlist
- 🚫 **No Duplicates**: Prevents duplicate songs from being added
- 📅 **Optional Weekly Playlists**: Can create dated weekly playlists if desired
- 🔐 **Secure Configuration**: Keeps API credentials safe and out of git
- 🤖 **Automation Ready**: Perfect for cron jobs and scheduling
- 💬 **User Friendly**: Clear status messages and error handling

## 🚀 Quick Start

### 1. Prerequisites

- Python 3.6+
- A Spotify account
- Internet connection

### 2. Installation

```bash
# Clone or download this repository
git clone <your-repo-url>
cd spotify-backup

# Create virtual environment (recommended)
python -m venv spotify-env
source spotify-env/bin/activate  # On Windows: spotify-env\Scripts\activate

# Install dependencies
pip install spotipy
```

### 3. Spotify App Setup

1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications)
2. Click "Create an App"
3. Fill in app name and description
4. Set **Redirect URI** to: `http://127.0.0.1:8080/callback`
5. Copy your **Client ID** and **Client Secret**

### 4. Configuration

Run the script for the first time to set up configuration:

```bash
python discover_weekly_saver.py
```

The script will guide you through the setup process and create a `config.py` file with your credentials.

**Alternative**: Set environment variables instead:
```bash
export SPOTIFY_CLIENT_ID="your_client_id_here"
export SPOTIFY_CLIENT_SECRET="your_client_secret_here"
export SPOTIFY_REDIRECT_URI="http://127.0.0.1:8080/callback"
```

### 5. First Run

```bash
python discover_weekly_saver.py
```

The script will:
- Find your Discover Weekly playlist
- Create a "Discover Weekly Collection" playlist
- Save all songs (avoiding duplicates)
- Show you the results

## 📖 How It Works

1. **Authentication**: Uses Spotify OAuth to access your playlists
2. **Discovery**: Searches your playlists for "Discover Weekly"
3. **Collection**: Creates or finds your master collection playlist
4. **Deduplication**: Checks existing songs to avoid duplicates
5. **Saving**: Adds new songs to your permanent collection

## ⚙️ Configuration Options

Edit `config.py` to customize behavior:

```python
# Create weekly dated playlists?
CREATE_WEEKLY_PLAYLISTS = False  # Recommended: False (only master collection)

# Change redirect URI if needed
SPOTIFY_REDIRECT_URI = "http://127.0.0.1:8080/callback"
```

## 🤖 Automation

Perfect for weekly automation! Add to crontab:

```bash
# Run every Monday at 9 AM
0 9 * * 1 cd /path/to/spotify-backup && source spotify-env/bin/activate && python discover_weekly_saver.py
```

## 📁 File Structure

```
spotify-backup/
├── discover_weekly_saver.py    # Main script
├── config.template.py          # Configuration template (safe for git)
├── config.py                   # Your actual config (DO NOT commit)
├── .gitignore                  # Excludes credentials from git
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## 🔒 Security

- ✅ `config.py` is excluded from git via `.gitignore`
- ✅ Use `config.template.py` as a safe template
- ✅ Environment variables supported as alternative
- ✅ OAuth tokens cached locally in `.cache` (also git-ignored)

## 🛠️ Troubleshooting

### "Discover Weekly playlist not found"
- Make sure you have Discover Weekly in your Spotify library
- Try following/saving the Discover Weekly playlist on Spotify

### "Authentication failed" 
- Check your Client ID and Client Secret
- Verify redirect URI matches your Spotify app settings
- Delete `.cache` file and try again

### "Permission denied"
- Make sure your Spotify app has the right permissions
- The script needs: `playlist-read-private`, `playlist-modify-private`, `playlist-modify-public`

## 📝 Requirements

Create a `requirements.txt`:
```
spotipy>=2.22.1
```

Install with: `pip install -r requirements.txt`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

MIT License - feel free to use and modify!

## 🎵 Enjoy Your Music!

Never lose another great Discover Weekly recommendation! 🎧
