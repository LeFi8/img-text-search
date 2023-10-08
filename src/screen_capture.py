import tkinter as tk


class ScreenCapture:
    def __init__(self, root):
        self.root = root
        self.root.attributes('-fullscreen', True)
        self.root.attributes('-alpha', 0.1)

        self.canvas = tk.Canvas(root, cursor="cross")
        self.canvas.pack(fill="both", expand=True)
        self.canvas.bind("<ButtonPress-1>", self._on_press)
        self.canvas.bind("<B1-Motion>", self._on_drag)
        self.canvas.bind("<ButtonRelease-1>", self._on_release)

        self.root.bind("<Escape>", self._exit)
        self.root.bind("<ButtonPress-3>", self._exit)

        self.start_x, self.start_y = None, None
        self.end_x, self.end_y = None, None
        self.rect = None

    def _on_press(self, event):
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)

        if self.rect:
            self.canvas.delete(self.rect)

        self.rect = self.canvas.create_rectangle(
            self.start_x, self.start_y, self.start_x, self.start_y, outline="red", width=3)

    def _on_drag(self, event):
        self.end_x = self.canvas.canvasx(event.x)
        self.end_y = self.canvas.canvasy(event.y)

        self.canvas.coords(self.rect, self.start_x,
                           self.start_y, self.end_x, self.end_y)

    def _on_release(self, event):
        self.end_x = self.canvas.canvasx(event.x)
        self.end_y = self.canvas.canvasy(event.y)

        selected_area = (self.start_x, self.start_y, self.end_x, self.end_y)

        self._capture_area(selected_area)
        self.canvas.delete(self.rect)
        self._exit()

    def _exit(self, event=None):
        self.root.destroy()

    def _capture_area(self, area):
        x1, y1, x2, y2 = area
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1

        self._set_capture_area(
            x1=x1,
            y1=y1,
            x2=x2 - x1,
            y2=y2 - y1
        )

    def _set_capture_area(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

    def get_capture_area(self):
        return self._x1, self._y1, self._x2, self._y2
