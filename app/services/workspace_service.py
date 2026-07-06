import json
from pathlib import Path


class WorkspaceService:

    FILE = Path("data/workspace.json")

    @classmethod
    def load(cls):

        if not cls.FILE.exists():

            cls.FILE.parent.mkdir(
                parents=True,
                exist_ok=True
            )

            cls.FILE.write_text(
                json.dumps(
                    {
                        "summary": "",
                        "comparison": "",
                        "literature": "",
                        "chat": []
                    },
                    indent=4
                )
            )

        with open(cls.FILE, "r") as f:
            return json.load(f)

    @classmethod
    def save(cls, data):

        with open(cls.FILE, "w") as f:
            json.dump(
                data,
                f,
                indent=4
            )

    @classmethod
    def update(cls, key, value):

        workspace = cls.load()

        workspace[key] = value

        cls.save(workspace)

    
    @classmethod
    def add_chat(cls, question, answer):

        workspace = cls.load()

        workspace["chat"].append(
            {
                "question": question,
                "answer": answer
            }
        )

        cls.save(workspace)