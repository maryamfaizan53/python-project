from graphics import Canvas 
import time

# Canvas aur grid ka size set karo
canvas_width = 400
canvas_height = 400
cell_size = 40
eraser_size = 20

def erase_object(canvas, eraser):
    """Eraser ke neeche jo bhi object aaye usko white kar do."""
    mouse_x = canvas.get_mouse_x()
    mouse_y = canvas.get_mouse_y()

    # Eraser ka area define karo
    left_x = mouse_x
    top_y = mouse_y
    right_x = mouse_x + eraser_size
    bottom_y = mouse_y + eraser_size

    # Jo objects eraser ke neeche aa rahe hain unko find karo
    overlapping_objects = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)

    for obj in overlapping_objects:
        if obj != eraser:  # Eraser khud erase na ho
            canvas.set_color(obj, "white")

def main():
    """Main function: Grid draw karo, phir eraser ko enable karo."""
    canvas = Canvas(canvas_width, canvas_height)

    # Grid create karo
    num_rows = canvas_height // cell_size
    num_cols = canvas_width // cell_size
    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * cell_size
            top_y = row * cell_size
            right_x = left_x + cell_size
            bottom_y = top_y + cell_size
            canvas.create_rectangle(left_x, top_y, right_x, bottom_y)

    # Wait karo jab tak user first click nahi karta
    canvas.wait_for_click()
    last_click_x, last_click_y = canvas.get_mouse_click()

    # Eraser create karo jahan user ne click kiya
    eraser = canvas.create_rectangle(
        last_click_x, last_click_y, 
        last_click_x + eraser_size, last_click_y + eraser_size, 
        "pink"
    )

    # Eraser ko mouse ke sath move karna start karo
    while True:
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()

        # Eraser ko move karo
        canvas.moveto(eraser, mouse_x, mouse_y)

        # Jo eraser ke neeche aaye usko erase karo
        erase_object(canvas, eraser)

        time.sleep(0.05)  # Thoda delay taki CPU slow chale

if __name__ == '__main__':
    main()
