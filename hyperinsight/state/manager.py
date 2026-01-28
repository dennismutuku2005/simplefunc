import pandas as pd
import copy
from typing import Dict, List, Optional, Any

class StateManager:
    """
    Handles data versioning, checkpoints, and rollbacks.
    """
    def __init__(self, initial_df: pd.DataFrame):
        self._history: List[pd.DataFrame] = [initial_df.copy()]
        self._checkpoints: Dict[str, int] = {"initial": 0}
        self._current_index = 0
        self._rollback_allowed = True

    def commit(self, df: pd.DataFrame, message: str = "Update"):
        """Saves a new state of the data."""
        self._history = self._history[:self._current_index + 1]
        self._history.append(df.copy())
        self._current_index += 1
        print(f"State Committed: {message} (Version {self._current_index})")

    def create_checkpoint(self, name: str):
        """Creates a named pointer to the current state."""
        self._checkpoints[name] = self._current_index
        print(f"Checkpoint created: '{name}' at Version {self._current_index}")

    def rollback(self, to: Optional[str] = None) -> pd.DataFrame:
        """Rolls back the data to a previous state or checkpoint."""
        if not self._rollback_allowed:
            raise PermissionError("Rollback is currently disabled by administrative policy.")
        
        if to:
            if to in self._checkpoints:
                self._current_index = self._checkpoints[to]
                print(f"Rolled back to checkpoint: '{to}'")
            else:
                print(f"Checkpoint '{to}' not found. No action taken.")
        else:
            if self._current_index > 0:
                self._current_index -= 1
                print(f"Rolled back one step to Version {self._current_index}")
            else:
                print("Already at initial state. Cannot rollback further.")
        
        return self._history[self._current_index].copy()

    def set_lock(self, locked: bool):
        self._rollback_allowed = not locked
        status = "LOCKED" if locked else "UNLOCKED"
        print(f"Data Rollback system is now {status}")

    def get_status(self) -> Dict[str, Any]:
        return {
            "current_version": self._current_index,
            "total_history": len(self._history),
            "checkpoints": list(self._checkpoints.keys()),
            "rollback_allowed": self._rollback_allowed
        }
