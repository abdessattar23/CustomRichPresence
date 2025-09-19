# Hardcoded Rich Presence Script

A simplified version of CustomRichPresence that sets up Discord Rich Presence with hardcoded values, based on the same logic as the `src/CustomRichPresence.py` but without the GUI.

## Features

- Uses the same core Rich Presence logic as the main CustomRichPresence application
- Hardcoded configuration (no GUI required)
- Support for custom details, state, image, and buttons
- Two modes: single update or continuous updates
- Proper error handling and validation
- Clean connection management

## Requirements

- Python 3.6 or higher
- `pypresence` library: `pip install pypresence`
- Discord application running on your system
- Valid Discord application client ID

## Configuration

Edit the hardcoded values in the `HardcodedRichPresence.__init__()` method:

```python
def __init__(self):
    # Basic configuration
    self.client_id = "827124648206270514"  # Replace with your Discord app client ID
    self.details = "Coding something awesome"
    self.state = "Working on Python project"
    self.image_name = "icon"  # Large image key from your Discord app assets
    self.small_image = None  # Optional small image key
    
    # Button configuration (up to 2 buttons supported by Discord)
    self.buttons = [
        {"label": "View on GitHub", "url": "https://github.com/abdessattar23/CustomRichPresence"},
        {"label": "Discord Server", "url": "https://discord.gg/example"}
    ]
    
    # Advanced options
    self.show_elapsed_time = True  # Set to False to hide elapsed time
    self.update_interval = 15  # Seconds between updates in continuous mode
```

See `EXAMPLES.md` for more configuration examples.

## Usage

1. **Install dependencies:**
   ```bash
   pip install pypresence
   ```

2. **Configure your values:**
   - Edit the script to set your Discord application client ID
   - Customize the details, state, and image name
   - Set up buttons with labels and URLs (optional)

3. **Run the script:**
   ```bash
   python3 hardcoded_rich_presence.py
   ```

4. **Choose mode:**
   - **Mode 1**: Update once and exit
   - **Mode 2**: Run continuously (updates based on your `update_interval` setting)

## Getting a Discord Application Client ID

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application or use an existing one
3. Copy the "Application ID" (this is your client ID)
4. Optionally, go to "Rich Presence" > "Art Assets" to upload images

## Example Output

```
Hardcoded Discord Rich Presence
========================================
Configuration:
  Client ID: 827124648206270514
  Details: Coding something awesome
  State: Working on Python project
  Image: icon
  Buttons: 2 configured

Choose mode:
1. Update once and exit
2. Run continuously (updates every 15 seconds)
Enter choice (1 or 2): 2

Starting continuous Rich Presence mode...
Press Ctrl+C to stop
Connecting to Discord with Client ID: 827124648206270514
Successfully connected to Discord!
Updating Rich Presence...
  Details: Coding something awesome
  State: Working on Python project
  Image: icon
  Buttons: 2 button(s)
Rich Presence updated successfully!
Rich Presence is active. Waiting 15 seconds before next update...
```

## Notes

- This script uses the same core logic as the main CustomRichPresence application
- The script validates input data and handles errors gracefully
- Make sure Discord is running before executing the script
- Press Ctrl+C to stop the continuous mode
- The script will automatically clean up the Discord connection on exit