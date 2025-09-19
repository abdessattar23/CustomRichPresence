#!/usr/bin/env python3
"""
Hardcoded Rich Presence Script

A simplified version of CustomRichPresence that sets up Discord Rich Presence
with hardcoded values. Based on the same logic as the src/CustomRichPresence.py
but without the GUI and with predefined settings.

Usage:
    python3 hardcoded_rich_presence.py

Requirements:
    - pypresence library: pip install pypresence
    - Discord application running
    - Valid Discord application client ID
"""

import time
import sys

try:
    from pypresence import Presence
except ImportError:
    print("Error: pypresence library not found.")
    print("Please install it with: pip install pypresence")
    sys.exit(1)


class HardcodedRichPresence:
    def __init__(self):
        # Hardcoded configuration - modify these values as needed
        self.client_id = "827124648206270514"  # Example client ID, replace with your own
        self.details = "Coding something awesome"
        self.state = "Working on Python project"
        self.image_name = "icon"  # Large image key from your Discord app assets
        self.small_image = None  # Optional small image key
        
        # Button configuration (up to 2 buttons supported by Discord)
        # Set to empty list [] if you don't want buttons
        self.buttons = [
            {"label": "View on GitHub", "url": "https://github.com/abdessattar23/CustomRichPresence"},
            {"label": "Discord Server", "url": "https://discord.gg/example"}
        ]
        
        # Advanced configuration options
        self.show_elapsed_time = True  # Set to False to hide elapsed time
        self.update_interval = 15  # Seconds between updates in continuous mode
        
        # Internal state
        self.rpc = None
        self.connected = False
        self.old_client_id = ""

    def validate_client_id(self):
        """Validate that the client ID is numeric"""
        if not self.client_id.isnumeric():
            print(f"Error: Invalid Client ID '{self.client_id}'. Client ID must be numeric.")
            return False
        return True

    def connect_to_discord(self):
        """Connect to Discord RPC"""
        try:
            if not self.connected:
                # Not connected - create new connection
                print(f"Connecting to Discord with Client ID: {self.client_id}")
                self.rpc = Presence(self.client_id)
                self.rpc.connect()
                self.connected = True
                print("Successfully connected to Discord!")
            elif self.client_id != self.old_client_id:
                # Connected but client ID changed - reconnect
                print("Client ID changed, reconnecting...")
                self.rpc.close()
                self.rpc = Presence(self.client_id)
                self.rpc.connect()
                print("Reconnected successfully!")
            
            self.old_client_id = self.client_id
            return True
            
        except Exception as e:
            print(f"Error: Could not connect to Discord. Make sure Discord is running.")
            print(f"Details: {e}")
            return False

    def validate_and_prepare_data(self):
        """Validate and prepare data for Rich Presence update"""
        # Ensure minimum length for details and state (Discord requirement)
        if not self.details or len(self.details) < 2:
            self.details = "  "
        if not self.state or len(self.state) < 2:
            self.state = "  "
        if not self.image_name:
            self.image_name = "  "

        # Validate buttons if they exist
        validated_buttons = []
        for button in self.buttons:
            if button.get("label") and button.get("url"):
                # Basic URL validation
                if button["url"].startswith(("http://", "https://")):
                    validated_buttons.append(button)
                else:
                    print(f"Warning: Invalid URL for button '{button['label']}': {button['url']}")
            
        return validated_buttons

    def update_presence(self):
        """Update Discord Rich Presence with hardcoded values"""
        if not self.validate_client_id():
            return False

        if not self.connect_to_discord():
            return False

        validated_buttons = self.validate_and_prepare_data()

        try:
            # Prepare presence data
            presence_data = {
                "details": self.details,
                "state": self.state,
                "large_image": self.image_name,
            }

            # Add elapsed time if enabled (matches original CustomRichPresence behavior)
            if self.show_elapsed_time:
                presence_data["start"] = int(time.time())

            # Add small image if specified
            if self.small_image:
                presence_data["small_image"] = self.small_image

            # Add buttons if valid ones exist (Discord supports up to 2 buttons)
            if validated_buttons:
                presence_data["buttons"] = validated_buttons[:2]  # Limit to 2 buttons

            # Update the presence
            print("Updating Rich Presence...")
            print(f"  Details: {self.details}")
            print(f"  State: {self.state}")
            print(f"  Image: {self.image_name}")
            if validated_buttons:
                print(f"  Buttons: {len(validated_buttons)} button(s)")

            self.rpc.update(**presence_data)
            print("Rich Presence updated successfully!")
            return True

        except Exception as e:
            print(f"Error: Could not update Rich Presence.")
            print(f"Details: {e}")
            
            # Clean up connection on error
            if self.rpc:
                try:
                    self.rpc.close()
                except:
                    pass
                self.rpc = None
                self.connected = False
            return False

    def cleanup(self):
        """Clean up RPC connection"""
        if self.rpc and self.connected:
            try:
                print("Cleaning up Discord connection...")
                self.rpc.close()
                self.connected = False
                print("Connection closed.")
            except Exception as e:
                print(f"Warning: Error during cleanup: {e}")

    def run_continuous(self):
        """Run Rich Presence continuously"""
        print(f"Starting continuous Rich Presence mode (updates every {self.update_interval} seconds)...")
        print("Press Ctrl+C to stop")
        
        try:
            while True:
                if self.update_presence():
                    print(f"Rich Presence is active. Waiting {self.update_interval} seconds before next update...")
                    time.sleep(self.update_interval)
                else:
                    print("Failed to update Rich Presence. Retrying in 30 seconds...")
                    time.sleep(30)
                    
        except KeyboardInterrupt:
            print("\nStopping Rich Presence...")
        finally:
            self.cleanup()


def main():
    """Main function"""
    print("Hardcoded Discord Rich Presence")
    print("=" * 40)
    
    # Create Rich Presence instance
    rp = HardcodedRichPresence()
    
    # Show current configuration
    print("Configuration:")
    print(f"  Client ID: {rp.client_id}")
    print(f"  Details: {rp.details}")
    print(f"  State: {rp.state}")
    print(f"  Image: {rp.image_name}")
    print(f"  Buttons: {len(rp.buttons)} configured")
    print()
    
    # Ask user for mode
    print("Choose mode:")
    print("1. Update once and exit")
    print("2. Run continuously (updates every 15 seconds)")
    
    try:
        choice = input("Enter choice (1 or 2): ").strip()
        
        if choice == "1":
            print("\nUpdating Rich Presence once...")
            if rp.update_presence():
                print("Done! Rich Presence has been set.")
            else:
                print("Failed to set Rich Presence.")
                sys.exit(1)
                
        elif choice == "2":
            rp.run_continuous()
            
        else:
            print("Invalid choice. Exiting.")
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        rp.cleanup()


if __name__ == "__main__":
    main()