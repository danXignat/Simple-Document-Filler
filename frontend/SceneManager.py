import customtkinter as ctk

class SceneManager:
    def __init__(self, root, default_scene):
        self.root = root
        self.current_scene = None
        self.scene_stack = []
        self.shared_data = {}  # Shared data across scenes
        self.switch_scene(default_scene)

    def switch_scene(self, scene_class):
        """Switch scenes by destroying the current one and creating a new one."""
        if self.current_scene is not None:
            self.current_scene.save_state(self.shared_data)  # Save the state of the current scene
            self.current_scene.destroy()

        # Create the new scene
        self.current_scene = scene_class(self.root, self.switch_scene, self.shared_data)
        self.scene_stack.append(self.current_scene)
        self.current_scene.load_state(self.shared_data)  # Load the state for the new scene
        self.current_scene.pack(fill="both", expand=True)

    def go_back(self):
        """Go back to the previous scene."""
        if len(self.scene_stack) > 1:
            self.scene_stack.pop()  # Remove the current scene
            self.switch_scene(self.scene_stack[-1].__class__)  # Switch to the previous scene
