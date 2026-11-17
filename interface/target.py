class Target:

    def __init__(self):
        self.target = None

    def set_target(self, target):
        self.target = target

    def get_target(self, target):
        return self.target

    def clear_target(self):
        self.target = None