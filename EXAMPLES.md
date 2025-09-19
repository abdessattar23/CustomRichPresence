# Example Configurations for hardcoded_rich_presence.py

Here are some example configurations you can use by modifying the `__init__` method in the script:

## Example 1: Simple Status (No Buttons)
```python
def __init__(self):
    self.client_id = "YOUR_CLIENT_ID_HERE"
    self.details = "Playing a game"
    self.state = "In menu"
    self.image_name = "game_logo"
    self.small_image = None
    self.buttons = []  # No buttons
    self.show_elapsed_time = True
    self.update_interval = 15
```

## Example 2: Coding/Development Status
```python
def __init__(self):
    self.client_id = "YOUR_CLIENT_ID_HERE"
    self.details = "Coding in Python"
    self.state = "Working on Discord bot"
    self.image_name = "python_logo"
    self.small_image = "vscode"
    self.buttons = [
        {"label": "View Repository", "url": "https://github.com/username/project"},
        {"label": "Documentation", "url": "https://project-docs.example.com"}
    ]
    self.show_elapsed_time = True
    self.update_interval = 30
```

## Example 3: Streaming/Content Creation
```python
def __init__(self):
    self.client_id = "YOUR_CLIENT_ID_HERE"
    self.details = "Live Streaming"
    self.state = "Playing Minecraft"
    self.image_name = "streaming"
    self.small_image = "minecraft"
    self.buttons = [
        {"label": "Watch Stream", "url": "https://twitch.tv/username"},
        {"label": "Join Discord", "url": "https://discord.gg/serverId"}
    ]
    self.show_elapsed_time = True
    self.update_interval = 10
```

## Example 4: Music/Audio Work
```python
def __init__(self):
    self.client_id = "YOUR_CLIENT_ID_HERE"
    self.details = "Producing Music"
    self.state = "In FL Studio"
    self.image_name = "music_note"
    self.small_image = "fl_studio"
    self.buttons = [
        {"label": "SoundCloud", "url": "https://soundcloud.com/username"},
        {"label": "YouTube", "url": "https://youtube.com/@username"}
    ]
    self.show_elapsed_time = False  # Don't show elapsed time
    self.update_interval = 60  # Update every minute
```

## Example 5: Study/Learning
```python
def __init__(self):
    self.client_id = "YOUR_CLIENT_ID_HERE"
    self.details = "Studying Computer Science"
    self.state = "Reading about algorithms"
    self.image_name = "book"
    self.small_image = "university_logo"
    self.buttons = [
        {"label": "Study Notes", "url": "https://notion.so/study-notes"},
    ]  # Only one button
    self.show_elapsed_time = True
    self.update_interval = 300  # Update every 5 minutes
```

## Example 6: Work/Professional
```python
def __init__(self):
    self.client_id = "YOUR_CLIENT_ID_HERE"
    self.details = "Working"
    self.state = "In a meeting"
    self.image_name = "office"
    self.small_image = None
    self.buttons = []  # No buttons for privacy
    self.show_elapsed_time = False  # Don't show how long you've been working
    self.update_interval = 60
```

## Getting Images for Discord Rich Presence

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Select your application
3. Go to "Rich Presence" → "Art Assets"
4. Upload images (recommended size: 512x512 pixels)
5. Use the "Key" name you set as the `image_name` or `small_image` value

## Tips

- Keep `details` and `state` under 128 characters each
- Image keys should match exactly what you uploaded to Discord
- URLs in buttons must be valid HTTP/HTTPS links
- Discord supports maximum 2 buttons
- Set `show_elapsed_time = False` if you don't want to show how long you've been doing something
- Adjust `update_interval` based on how often you want the presence to refresh