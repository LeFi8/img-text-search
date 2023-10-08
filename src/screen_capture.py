import tkinter as tk


class ScreenCapture:
    def __init__(self, root):
        self._root = root
        self._root.attributes('-fullscreen', True)
        self._root.attributes('-alpha', 0.1)

        self._canvas = tk.Canvas(root, cursor="cross")
        self._canvas.pack(fill="both", expand=True)
        self._canvas.bind("<ButtonPress-1>", self._on_press)
        self._canvas.bind("<B1-Motion>", self._on_drag)
        self._canvas.bind("<ButtonRelease-1>", self._on_release)

        self._root.bind("<Escape>", self._exit)
        self._root.bind("<ButtonPress-3>", self._exit)

        self._start_x, self._start_y = None, None
        self._end_x, self._end_y = None, None
        self._rect = None

    def _on_press(self, event):
        self._start_x = self._canvas.canvasx(event.x)
        self._start_y = self._canvas.canvasy(event.y)

        if self._rect:
            self._canvas.delete(self._rect)

        self._rect = self._canvas.create_rectangle(
            self._start_x, self._start_y, self._start_x, self._start_y, outline="red", width=3)

    def _on_drag(self, event):
        self._end_x = self._canvas.canvasx(event.x)
        self._end_y = self._canvas.canvasy(event.y)

        self._canvas.coords(self._rect, self._start_x,
                            self._start_y, self._end_x, self._end_y)

    def _on_release(self, event):
        self._end_x = self._canvas.canvasx(event.x)
        self._end_y = self._canvas.canvasy(event.y)

        selected_area = (self._start_x, self._start_y,
                         self._end_x, self._end_y)

        self._capture_area(selected_area)
        self._canvas.delete(self._rect)
        self._exit()

    def _exit(self):
        self._root.destroy()

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
