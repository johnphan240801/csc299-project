import json, builtins, runpy
from pathlib import Path

def test_add_task_via_cli(tmp_path, monkeypatch, capsys):
    # run in a temp folder so tasks.json is created there
    monkeypatch.chdir(tmp_path)

    # sequence of “user” inputs:
    #   2 = Add task, then title, description, 6 = Quit  (adjust numbers to your menu)
    inputs = iter(["2", "Buy milk", "groceries", "6"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    runpy.run_module("tasks3.__init__", run_name="__main__")

    out = capsys.readouterr().out
    assert "add" in out.lower()

    data = json.loads(Path("tasks.json").read_text(encoding="utf-8"))
    assert data[0]["title"] == "Buy milk"
    assert data[0]["completed"] is False
    
def test_mark_complete_via_cli(tmp_path, monkeypatch):
    # Work in an isolated temp dir
    monkeypatch.chdir(tmp_path)

    # Seed a tasks.json with two incomplete tasks
    Path("tasks.json").write_text(
        '[{"title":"A","description":"","completed":false},'
        ' {"title":"B","description":"","completed":false}]',
        encoding="utf-8",
    )

    # Inputs:
    #  3 -> "Mark task complete"
    #  2 -> choose task #2 ("B")
    #  6 -> Quit
    inputs = iter(["3", "2", "6"])
    monkeypatch.setattr(builtins, "input", lambda *_: next(inputs))

    # Run your CLI via the package entry (requires src/tasks3/__main__.py)
    runpy.run_module("tasks3.__init__", run_name="__main__")

    # Verify task #2 is now completed, task #1 remains not completed
    data = json.loads(Path("tasks.json").read_text(encoding="utf-8"))
    assert data[0]["completed"] is False
    assert data[1]["completed"] is True