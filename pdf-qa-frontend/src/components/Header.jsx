import FileUpload from './FileUpload';
// import './Header.css';

function Header({ onUploadSuccess }) {
  return (
    <header className="header">
      <div className="logo">Your Logo Here</div>
      <div className="upload-container">
        <FileUpload onUploadSuccess={onUploadSuccess} />
      </div>
    </header>
  );
}

export default Header;
