import sqlite3

class Chat:
    @staticmethod
    def create_table():
        # Ensure the table exists before any operation
        conn = sqlite3.connect('chat.db')
        cursor = conn.cursor()
        
        # Create the conversations table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS conversations (
                id INTEGER PRIMARY KEY,
                session_id TEXT NOT NULL UNIQUE,
                conversation_text TEXT NOT NULL
            )
        ''')
        
        conn.commit()
        conn.close()

    @staticmethod
    def create(chat_id, text):
        Chat.create_table()  # Ensure the table is created
        
        conn = sqlite3.connect('chat.db')
        cursor = conn.cursor()
    
        # Insert a new conversation (ignore if it already exists due to UNIQUE constraint)
        cursor.execute('''
            INSERT OR IGNORE INTO conversations (session_id, conversation_text)
            VALUES (?, ?)
        ''', (chat_id, text))
    
        conn.commit()
        conn.close()
    
    @staticmethod
    def read(chat_id):
        Chat.create_table()  # Ensure the table is created
        
        conn = sqlite3.connect('chat.db')
        cursor = conn.cursor()
    
        # Fetch the conversation based on the session_id
        cursor.execute('''
            SELECT conversation_text FROM conversations WHERE session_id = ?
        ''', (chat_id,))
    
        result = cursor.fetchone()
        conn.close()
    
        return result[0] if result else None
    
    @staticmethod
    def write(chat_id, text):
        Chat.create_table()  # Ensure the table is created
        
        conn = sqlite3.connect('chat.db')
        cursor = conn.cursor()
    
        # Try to update the conversation text for the given session_id
        cursor.execute('''
            UPDATE conversations
            SET conversation_text = ?
            WHERE session_id = ?
        ''', (text, chat_id))
    
        # If no rows were affected (i.e., the session_id doesn't exist), insert a new conversation
        if cursor.rowcount == 0:
            cursor.execute('''
                INSERT INTO conversations (session_id, conversation_text)
                VALUES (?, ?)
            ''', (chat_id, text))
            print("Chat created.")
        else:
            print("Chat updated.")
    
        conn.commit()
        conn.close()