import tkinter as tk
morse = {'a': '.- ', 'b': '-... ', 'c': '-.-. ', 'd': '-.. ', 'e': '. ', 'f': '..-. ', 'g': '--. ', 'h': '.... ',
         'i': '.. ', 'j': '.--- ', 'k': '-.- ', 'l': '.-.. ', 'm': '-- ', 'n': '-. ', 'o': '--- ', 'p': '.--. ',
         'q': '--.- ', 'r': '.-. ', 's': '... ', 't': '- ', 'u': '..- ', 'v': '...- ', 'w': '.-- ', 'x': '-..- ',
         'y': '-.-- ', 'z': '--.. ', 'ą': '.-.- ', 'ć': '-.-.. ', 'ę': '..-.. ', 'ł': '.-..- ', 'ń': '--.-- ',
         'ó': '---. ', 'ś': '...-... ', 'ż': '--..-. ', 'ź': '--..- ', '1': '.---- ', '2': '..--- ', '3': '...-- ',
         '4': '....- ', '5': '..... ', '6': '-.... ', '7': '--... ', '8': '---.. ', '9': '----. ', '0': '----- ',
         ' ': '/ '}
alphabet = dict((v, k) for k, v in morse.items())


def translate():
    output_text.delete("1.0", tk.END)
    if ord(input_text.get("0.0")) != 45 and ord(input_text.get("0.0")) != 46:
        text = input_text.get("1.0", 'end-1c').lower()
        for letter in text:
            output_text.insert(tk.END, morse.get(letter, '/'))
    else:
        text = input_text.get("1.0", 'end-1c')
        words = text.split("/ ")
        for ind in range(0, len(words)):
            letters = words[ind].split()
            for one_letter in letters:
                output_text.insert(tk.END, alphabet.get(one_letter+" ", " "))
            output_text.insert(tk.END, " ")


def clear_text():
    input_text.delete("1.0", tk.END)

main_window = tk.Tk()
main_window.title("Morse alphabet converter")
input_label = tk.Label(main_window, text="Input text")
output_label = tk.Label(main_window, text="Translated text")
input_text = tk.Text(width=50, height=5, wrap='word')
output_text = tk.Text(width=50, height=5)
translate_button = tk.Button(text="Translate", command=translate)
clear_button = tk.Button(text="Clear input field", command=clear_text)
input_label.grid(row=0, columnspan=2)
input_text.grid(row=1, columnspan=2)
translate_button.grid(row=2, column=0)
clear_button.grid(row=2, column=1)
output_label.grid(row=3, columnspan=2)
output_text.grid(row=4, columnspan=2)
input_text.insert("end", 'Type your message here, either normal letters and numbers or Morse code using \'.\' for a dot'
                         ','' \'-\' for a dash, separating letters by spaces and words by \'/\' (with space)')
main_window.mainloop()
