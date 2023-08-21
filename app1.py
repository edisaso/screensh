import tkinter as tk
from tkinter import ttk
from PIL import ImageGrab, ImageTk
import datetime
from screeninfo import get_monitors

class ScreenshotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Screenshot")

        self.capture_button = tk.Button(root, text="Capture Screenshot", command=self.capture)
        self.capture_button.pack(pady=10)

        # Create a dropdown menu for screen selection
        self.screen_var = tk.StringVar()
        self.screen_label = tk.Label(root, text="Select Screen:")
        self.screen_label.pack()
        self.screen_dropdown = ttk.Combobox(root, textvariable=self.screen_var)
        self.screen_dropdown.pack(pady=5)

        # Fill the dropdown with available screen names
        screen_names = self.get_screen_names()
        self.screen_dropdown['values'] = screen_names
        self.screen_dropdown.current(0)  # Set the default value

    def get_screen_names(self):
        # Get a list of available screen names
        screen_names = [monitor.name for monitor in get_monitors()]
        return screen_names

    def capture(self):
        selected_screen = self.screen_var.get()
        if not selected_screen:
            return

        # Get the current timestamp for the image name
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"screenshot_{timestamp}.png"

        # Find the selected screen
        selected_screen_info = None
        for monitor in get_monitors():
            if monitor.name == selected_screen:
                selected_screen_info = monitor
                break

        if selected_screen_info:
            # Capture the selected screen
            screenshot = ImageGrab.grab(bbox=(
                selected_screen_info.x, selected_screen_info.y,
                selected_screen_info.x + selected_screen_info.width,
                selected_screen_info.y + selected_screen_info.height))
            screenshot.save(filename)

            # Display a success message
            success_label = tk.Label(root, text=f"Screenshot saved as {filename}")
            success_label.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = ScreenshotApp(root)
    root.mainloop()
