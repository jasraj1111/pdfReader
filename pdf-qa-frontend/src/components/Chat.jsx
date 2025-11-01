import './Chat.css'
import ChatBubble from './ChatBubble';

export default function Chat({ messages }) {
  return (
    <div className="chat">
      {messages.map((msg, index) => (
        <ChatBubble key={index} message={msg} />
      ))}
    </div>
  );
}
