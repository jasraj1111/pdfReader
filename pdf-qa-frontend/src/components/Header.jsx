import './Header.css';
import FileUpload from './FileUpload';

function Header({ onUploadSuccess }) {
  return (
    <header className="header">
      <div className="logo">PDF Chatbot</div>
      <div className="upload-container">
        <FileUpload onUploadSuccess={onUploadSuccess} />
      </div>
    </header>
  );
}

export default Header;
