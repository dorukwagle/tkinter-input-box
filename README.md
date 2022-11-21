**Installation**<br>
<pre>pip install tkinter-input-box</pre>
**Import in code<br>**
<pre>from tkinter_input_box.input_box import InputBox</pre><br>

**_Refer to the example.py file for example<br>_**
<br>
**Options:**
<li>container : container e.g. root, to hold the InputBox</li>
<li>text : default text to display</li>
<li>input_type : password or text</li>
<li>take_focus : whether to take focus or not, by default it is 0, i.e. it does not take focus by default</li>
<li>font_color : color of the text</li>
<li>placeholder_color : color of the placeholder</li>
<li>show: display the given character in the input box while entering password ( check the example )</li>
<li> And all the other options that usual ttk.Entry supports </li>

**<br><br>Methods**
<li>get_text(): returns the text in the InputBox</li>
<li>set_text(text): updates the InputBox text with given text</li>
<li>get_placeholder(): returns the current placeholder in the InputBox</li>
<li>set_placeholder(placeholder): updates the placeholder of the InputBox with given placeholder</li>

**_<br>More functionalities will be added soon..._**