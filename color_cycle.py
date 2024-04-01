from phue import Bridge
import time

# IP address of your Philips Hue bridge
HUE_BRIDGE_IP = '192.168.50.57'

# Connect to the Hue bridge
b = Bridge(HUE_BRIDGE_IP)

# If the app is not registered and the button is not pressed, press the button and call connect()
b.connect()

# Get all the lights connected to the bridge
lights = b.lights

# Function to fade through colors with faster transition time
def fade_through_colors(lights, transition_time=0.1):
    hue_range = range(0, 65535, 5000)  # Range of hues to fade through
    for hue in hue_range:
        for light in lights:
            light.transitiontime = transition_time * 10  # Convert seconds to 1/10 seconds
            light.hue = hue
            light.saturation = 254  # Set saturation to maximum for vivid colors
        time.sleep(transition_time)

# Main function to cycle indefinitely
def main():
    while True:
        fade_through_colors(lights)

# Start the main loop
if __name__ == "__main__":
    main()
