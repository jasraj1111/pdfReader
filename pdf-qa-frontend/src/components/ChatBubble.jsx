export default function ChatBubble({ message }) {
    const isUser = message.role === 'user';
    return (
      <div className={`chat-bubble ${isUser ? 'user' : 'ai'}`}>
        <div className="avatar">{isUser ? 'S' : 'ai'}</div>
        <div className="message">{message.content}</div>
      </div>
    );
  }
  