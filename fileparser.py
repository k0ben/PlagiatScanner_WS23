import errno

class FileParser:

    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        try:
            with open(self.file_path, 'r') as f:
                content = f.read()
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
            tokens = []
            for token in content.split():
                if token.isdigit():
                    tokens.append(int(token))
                else:
                    tokens.append(token)
            print(f"Tokenized")
            return tokens
        except:
            print(f"Fehler beim Tokenisieren des Inhalts")
            return None

