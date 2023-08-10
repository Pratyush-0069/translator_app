import tkinter as tk
from google.cloud import translate_v2 as translate

class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Translator App")

        self.label_source = tk.Label(root, text="Source Language:")
        self.label_source.pack()

        self.source_language = tk.StringVar()
        self.entry_source = tk.Entry(root, textvariable=self.source_language)
        self.entry_source.pack()

        self.label_target = tk.Label(root, text="Target Language:")
        self.label_target.pack()

        self.target_language = tk.StringVar()
        self.entry_target = tk.Entry(root, textvariable=self.target_language)
        self.entry_target.pack()

        self.label_text = tk.Label(root, text="Text to Translate:")
        self.label_text.pack()

        self.text_to_translate = tk.StringVar()
        self.entry_text = tk.Entry(root, textvariable=self.text_to_translate)
        self.entry_text.pack()

        self.translated_text = tk.StringVar()
        self.label_translation = tk.Label(root, textvariable=self.translated_text)
        self.label_translation.pack()

        self.translate_button = tk.Button(root, text="Translate", command=self.translate_text)
        self.translate_button.pack()

    def translate_text(self):
        source_lang = self.source_language.get()
        target_lang = self.target_language.get()
        text = self.text_to_translate.get()

        if not source_lang or not target_lang or not text:
            self.translated_text.set("Please fill in all fields.")
            return

        client = translate.Client()
        translation = client.translate(text, target_language=target_lang, source_language=source_lang)
        translated_text = translation['translatedText']
        self.translated_text.set(translated_text)

def main():
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
