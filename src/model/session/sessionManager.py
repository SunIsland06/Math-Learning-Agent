import uuid
from typing import Dict, Tuple

class SessionManager:
    def __init__(self, model_factory):
        # key: (user_id, session_id) -> Model instance
        self._sessions: Dict[Tuple[str, str], object] = {}
        self._model_factory = model_factory

    def new_session(self, user_id: str) -> str:
        session_id = str(uuid.uuid4())
        self._sessions[(user_id, session_id)] = self._model_factory()
        return session_id

    def get_session(self, user_id: str, session_id: str):
        return self._sessions.get((user_id, session_id))

    def reset_session(self, user_id: str, session_id: str) -> bool:
        key = (user_id, session_id)
        if key not in self._sessions:
            return False
        self._sessions[key].reset()
        return True

    def list_sessions(self, user_id: str):
        return [sid for (uid, sid) in self._sessions.keys() if uid == user_id]

    def remove_session(self, user_id: str, session_id: str) -> bool:
        return self._sessions.pop((user_id, session_id), None) is not None