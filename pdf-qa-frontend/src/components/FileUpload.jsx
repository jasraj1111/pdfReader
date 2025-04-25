import { useRef } from 'react';
import './FileUpload.css';

function FileUpload({ onUploadSuccess }) {
  const fileInputRef = useRef(null);

  const handleUploadClick = () => {
    fileInputRef.current.click();
  };

  const handleFileChange = async (event) => {
    const file = event.target.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch('http://localhost:8000/upload/', {
        method: 'POST',
        body: formData,
      });

      const data = await response.json();

      if (response.ok) {
        onUploadSuccess({ name: file.name, id: data.pdf_id });
      } else {
        alert(data.error || 'Upload failed');
      }
    } catch (error) {
      console.error('Upload error:', error);
      alert('Upload failed. See console for details.');
    }
  };

  return (
    <div className="file-upload">
      <button className="upload-button" onClick={handleUploadClick}>
        Upload PDF
      </button>
      <input
        type="file"
        ref={fileInputRef}
        style={{ display: 'none' }}
        accept="application/pdf"
        onChange={handleFileChange}
      />
    </div>
  );
}

export default FileUpload;
