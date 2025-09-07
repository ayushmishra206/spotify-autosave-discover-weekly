#!/usr/bin/env python3
"""
Setup script for Discover Weekly Saver

This script helps you get started quickly by:
1. Creating a virtual environment
2. Installing dependencies
3. Setting up configuration
4. Running a test
"""

import os
import sys
import subprocess

def run_command(cmd, description):
    """Run a command and handle errors."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        if e.stdout:
            print(f"Output: {e.stdout}")
        if e.stderr:
            print(f"Error: {e.stderr}")
        return False

def main():
    print("🎵 Discover Weekly Saver Setup")
    print("=" * 40)
    
    # Check Python version
    if sys.version_info < (3, 6):
        print("❌ Python 3.6+ is required")
        sys.exit(1)
    
    print(f"✅ Python {sys.version.split()[0]} detected")
    
    # Create virtual environment if it doesn't exist
    if not os.path.exists("spotify-env"):
        if not run_command("python -m venv spotify-env", "Creating virtual environment"):
            sys.exit(1)
    else:
        print("✅ Virtual environment already exists")
    
    # Activate virtual environment and install dependencies
    if os.name == 'nt':  # Windows
        activate_cmd = "spotify-env\\Scripts\\activate"
        pip_cmd = "spotify-env\\Scripts\\pip"
    else:  # Linux/Mac
        activate_cmd = "source spotify-env/bin/activate"
        pip_cmd = "spotify-env/bin/pip"
    
    if not run_command(f"{pip_cmd} install spotipy", "Installing spotipy"):
        sys.exit(1)
    
    # Check if config exists
    if not os.path.exists("config.py"):
        print("\n🔧 Configuration needed!")
        print("Run the main script to set up your Spotify credentials:")
        print(f"   {activate_cmd} && python discover_weekly_saver.py")
    else:
        print("✅ Configuration file exists")
    
    print("\n🎉 Setup complete!")
    print("\nNext steps:")
    print(f"1. Activate virtual environment: {activate_cmd}")
    print("2. Run the script: python discover_weekly_saver.py")
    print("3. Set up automation with cron (optional)")

if __name__ == "__main__":
    main()
