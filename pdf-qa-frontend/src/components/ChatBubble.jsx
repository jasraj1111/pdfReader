import './ChatBubble.css';
export default function ChatBubble({ message }) {
    const isUser = message.role === 'user';
    return (
      <div className={`chat-bubble ${isUser ? 'user' : 'ai'}`}>
        <div className="avatar">{isUser ? 'J' : 'AI'}</div>
        <div className="message">{message.content}</div>
      </div>
    );
  }
  