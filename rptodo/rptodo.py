''' This module provides the To-Do model-controller.'''
# rptodo/rptodo.py

from os import write
from pathlib import Path
import re
from typing import Any, Dict, List, NamedTuple

from rptodo import DB_READ_ERROR, ID_ERROR
from rptodo.database import DatbaseHandler

class CurrentToDo(NamedTuple):
    todo: Dict[str, Any]
    error: int

class Todoer:
    def __init__(self, db_path: Path) -> None:
        self._db_handler = DatbaseHandler(db_path)

    def add(self, description: List[str], priority: int = 2) -> CurrentToDo:
        '''Adds a new to-do to the datbase.'''
        description_text = " ".join(description)
        if not description_text.endswith("."):
            description_text += "."
        todo = {
            "Description": description_text,
            "Priority": priority,
            "Done": False,
        }
        read = self._db_handler.read_todos()
        if read.error == DB_READ_ERROR:
            return CurrentToDo(todo, read.error)
        read.todo_list.append(todo)
        write = self._db_handler.write_todos(read.todo_list)
        return CurrentToDo(todo, write.error)
    
    def get_todo_list(self) -> List[Dict[str, Any]]:
        """Return the current to-do list."""
        read = self._db_handler.read_todos()
        return read.todo_list
        
    def set_done(self, todo_id: int) -> CurrentToDo:
        """Set a todo as done."""
        read = self._db_handler.read_todos()
        if read.error:
            return CurrentToDo({}, read.error)
        try:
            todo = read.todo_list[todo_id - 1]
        except IndexError:
            return CurrentToDo({}, ID_ERROR)
        todo["Done"] = True
        write = self._db_handler.write_todos(read.todo_list)
        return CurrentToDo(todo, write.error)

    def remove(self, todo_id: int) -> CurrentToDo:
        """Remove a to-do from the database using its id of index."""
        read = self._db_handler.read_todos()
        if read.error:
            return CurrentToDo({}, read.error)
        try:
            todo = read.todo_list.pop(todo_id - 1)
        except IndexError:
            return CurrentToDo({}, ID_ERROR)
        write = self._db_handler.write_todos(read.todo_list)
        return CurrentToDo(todo, write.error)

    def remove_all(self) -> CurrentToDo:
        """Removes all to-do's from the database."""
        write = self._db_handler.write_todos([])
        return CurrentToDo({}, write.error)




 