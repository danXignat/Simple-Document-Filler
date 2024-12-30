class Signal:
    def __init__(self):
        self._slots = []

    def connect(self, slot):
        """Connect a slot to this signal."""
        self._slots.append(slot)

    def emit(self, *args, **kwargs):
        """Emit the signal and call all connected slots."""
        for slot in self._slots:
            slot(*args, **kwargs)
