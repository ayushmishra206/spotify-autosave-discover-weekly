"""
Configuration template for Discover Weekly Saver

Copy this file to config.py and fill in your actual credentials.

To set up:
1. Copy this file: cp config.template.py config.py
2. Go to https://developer.spotify.com/dashboard/applications
3. Create a new app or use an existing one
4. Copy your Client ID and Client Secret to config.py
5. Make sure the Redirect URI in your Spotify app matches the one below

Environment Variables (alternative):
You can also set these as environment variables instead of using config.py:
- SPOTIFY_CLIENT_ID
- SPOTIFY_CLIENT_SECRET  
- SPOTIFY_REDIRECT_URI
"""

# Spotify App Credentials
# Get these from https://developer.spotify.com/dashboard/applications
SPOTIFY_CLIENT_ID = "your_client_id_here"
SPOTIFY_CLIENT_SECRET = "your_client_secret_here"

# Redirect URI - MUST match what you set in your Spotify app
SPOTIFY_REDIRECT_URI = "http://127.0.0.1:8080/callback"

# Optional: Default behavior for weekly playlist creation
# True = Always create weekly playlists
# False = Never create weekly playlists (recommended)
# None = Ask each time
CREATE_WEEKLY_PLAYLISTS = False
