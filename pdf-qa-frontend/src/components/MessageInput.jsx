import { useState } from 'react';
import { FiSend } from 'react-icons/fi';

export default function MessageInput({ onSend }) {
  const [text, setText] = useState('');

  const handleSend = () => {
    if (!text.trim()) return;
    onSend(text.trim());
    setText('');
  };

  return (
    <div className="input-container">
      <input
        value={text}
        onChange={(e) => setText(e.target.value)}
        onKeyDown={(e) => e.key === 'Enter' && handleSend()}
        placeholder="Send a message..."
      />
      <button onClick={handleSend}>
        <FiSend />
      </button>
    </div>
  );
}
