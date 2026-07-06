from pathlib import Path
import json
import uuid


class NotesService:

    FILE = Path("data/notes.json")

    @classmethod
    def load(cls):

        if not cls.FILE.exists():

            cls.FILE.parent.mkdir(
                parents=True,
                exist_ok=True
            )

            cls.FILE.write_text("[]")

        with open(cls.FILE, "r") as f:

            return json.load(f)

    @classmethod
    def save(cls, notes):

        with open(cls.FILE, "w") as f:

            json.dump(
                notes,
                f,
                indent=4
            )

    @classmethod
    def add(cls, title, content):

        notes = cls.load()

        note = {

            "id": str(uuid.uuid4()),

            "title": title,

            "content": content
        }

        notes.append(note)

        cls.save(notes)

        return note

    @classmethod
    def list(cls):

        return cls.load()

    @classmethod
    def delete(cls, note_id):

        notes = cls.load()

        notes = [
            n
            for n in notes
            if n["id"] != note_id
        ]

        cls.save(notes)