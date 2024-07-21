from highrise import BaseBot, SessionMetadata

class Mybot(BaseBot): 
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("Bot started")
