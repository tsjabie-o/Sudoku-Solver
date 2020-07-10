import tkinter as tk


frame_width = 700
frame_height = 700

root = tk.Tk()
root.geometry("700x800")

# frame = tk.Frame(root, height=root_height, width=root_width)
# frame.pack(expand=True, fill='both')

board_frame = tk.Frame(root, height=frame_height, width=frame_width)
board_frame.pack()
canvas = tk.Canvas(board_frame, bg='gray',
                   width=frame_width, height=frame_height)

canvas.pack(expand=True, fill='both')

root.mainloop()
