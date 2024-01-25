import errno
import re

class FileParser:

    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        try:
            with open(self.file_path, 'r') as f:
                content = f.read()
                # Entferne alle Kommentare
                content = re.sub(r'%.*$', '', content, flags=re.MULTILINE)
                # Entferne Variablennamen vor einem '='
                content = re.sub(r'\b\w+(?=\s*=)', '', content)
                # Entferne Zeilenumbrüche
                content = re.sub(r'(\n)', '', content)
            print(f"Read: {self.file_path}")
            return content
        except IOError as e:
            if e.errno == errno.ENOENT:
                print(f"Datei nicht gefunden: {self.file_path}")
            elif e.errno == errno.EACCES:
                print(f"Keine Leseberechtigung für Datei: {self.file_path}")
            else:
                print(f"Unbekannter Fehler beim Öffnen der Datei: {e}")
            return None

    def tokenize(self, content):
        if content is None:
            return None
        try:
            #tokens = []
            #tokens = re.split(r'(\W+)', content)
            # Teile Inhalt in Tokens auf, wobei alle Nicht-Wort-Zeichen und Zeilenumbrüche als Trennzeichen verwendet werden
            tokens = re.split(r'(\W|\n)', content)
            # Entferne alle leeren Strings und Strings, die nur aus Leerzeichen oder Zeilenumbrüchen bestehen
            tokens = list(filter(lambda token: token.strip() and token != '\n', tokens))
            tokens_string = ' '.join(tokens)
            # for token in content.split():
            #    if token.isdigit():
            #        tokens.append(int(token))
            #    else:
            #        tokens.append(token)
            print(f"Tokenized")
            return tokens_string
        except Exception as e:
            print(f"Fehler beim Tokenisieren des Inhalts:{e}")
            return None

