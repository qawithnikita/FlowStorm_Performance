class ChatSessions:
    sessions = {}

    @classmethod
    def create_session(cls, session_id, data):
        cls.sessions[session_id] = data

    @classmethod
    def get_session(cls, session_id):
        return cls.sessions.get(session_id)
