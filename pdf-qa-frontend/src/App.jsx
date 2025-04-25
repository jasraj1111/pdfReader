import { useState } from 'react';
import Header from './components/Header';
import Chat from './components/Chat';
import MessageInput from './components/MessageInput';
import FileUpload from './components/FileUpload';
import './index.css';

function App() {
  const [messages, setMessages] = useState([]);
  const [pdfName, setPdfName] = useState(null);
  const [pdfId, setPdfId] = useState(null); // NEW: store pdf_id returned by backend

  const sendMessage = async (text) => {
    if (!pdfId) {
      alert('Please upload a PDF before asking a question.');
      return;
    }

    const newMessages = [...messages, { role: 'user', content: text }];
    setMessages(newMessages);

    const response = await fetch('http://localhost:8000/ask/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ question: text, pdf_id: pdfId }),
    });

    const data = await response.json();
    setMessages([...newMessages, { role: 'ai', content: data.answer }]);
  };

  // Callback to receive PDF name and ID from FileUpload component
  const handleUploadSuccess = ({ name, id }) => {
    setPdfName(name);
    setPdfId(id);
    setMessages([]); // Optionally reset chat when new file is uploaded
  };

  return (
    <div className="app" style={{ display: 'flex', flexDirection: 'column', height: '100vh' }}>
      <Header onUploadSuccess={handleUploadSuccess} pdfName={pdfName} />
      {/* <FileUpload onUploadSuccess={handleUploadSuccess} /> */}
      <Chat messages={messages} />
      <MessageInput onSend={sendMessage} />
    </div>
  );
}

export default App;
