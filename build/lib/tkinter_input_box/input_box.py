from tkinter import ttk
from tkinter import StringVar


class InputBox(ttk.Entry):
    def __init__(self, container, text="", placeholder="", input_type="", show="*", font_color="",
                 placeholder_color="", background="grey", fieldbackground="white", **kw):
        self.__place_color = "#D3D3D3" if not placeholder_color else placeholder_color
        self.__foreground = font_color if font_color else "#000000"
        self.__show = show if input_type == "password" else ''
        self.__holder = StringVar(container)
        style = ttk.Style()
        style.configure(f"{id(self)}.TEntry", fieldbackground=fieldbackground, backgroun=background)
        self.__placeholder = placeholder
        super().__init__(container, textvariable=self.__holder, style=f"{id(self)}.TEntry", takefocus=0, **kw)
        self.configure(background="red")
        self.__text = self.__holder.get()

        # add action listener
        self.bind("<Key>", self.__on_key)
        self.bind("<KeyRelease>", self.__on_key_release, add="+")
        self.bind("<FocusIn>", self.__on_focus, add="+")
        # self.bind("<Tab>", self.__on_tab, add="+")

        # if there is placeholder add it
        if self.__placeholder:
            self.__add_placeholder(self.__placeholder)

        # if there is text add it to the textbox
        if text:
            self.__initial_text(text)

    def __add_placeholder(self, placeholder):
        self.__holder.set("")
        self.__text = self.__holder.get()
        self.__holder.set(placeholder)
        self.config(foreground=self.__place_color, show='')

    # add text to the textbox provided during creation
    def __initial_text(self, text):
        if not text:
            self.__add_placeholder(self.__placeholder)
            return
        self.__text = text
        self.__holder.set(self.__text)
        self.config(foreground=self.__foreground, show=self.__show)

    def __on_key(self, key):
        # check if there is placeholder or text
        if not self.__text:
            # remove placeholder and change the color
            self.__holder.set("")
            self.config(foreground=self.__foreground, show=self.__show)
            # temporarily hold a character, so when this event is called before the key
            # release event is called, the condition becomes false and this code do not execute
            self.__text = key.char

    def __on_key_release(self, key):
        # if the holder is empty add the placeholder again
        if not self.__holder.get():
            self.__add_placeholder(self.__placeholder)
            # empty the self.__text
            self.__text = ""
            return
        # if there is no placeholder then just update the __text with the __holder
        self.__text = self.__holder.get()

    # on focus, place the cursor at the beginning of the placeholder else if there is text return
    def __on_focus(self, _):
        if self.__text:
            return
        self.icursor(0)

    def __manage_special_keys(self, _):
        if not self.__text:
            return "break"

    def get_text(self):
        return self.__text

    def set_text(self, text):
        self.__initial_text(text)

    def get_placeholder(self):
        return self.__placeholder

    def set_placeholder(self, placeholder):
        self.__placeholder = placeholder
        self.__add_placeholder(self.__placeholder)
