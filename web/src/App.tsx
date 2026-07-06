import { useState } from "react";
import "./index.css";

export default function App() {
  return (
    <div className="page">
      <h1 className="title">M11 Frontend Dashboard 🚀</h1>

      <div className="grid">

        <div className="card">
          <h2>🔍 Extract</h2>
          <input placeholder="Enter text..." />
          <button>Run</button>
          <p className="result">Waiting for backend...</p>
        </div>

        <div className="card">
          <h2>🧠 KG Query</h2>
          <input placeholder="Ask question..." />
          <button>Run</button>
          <p className="result">Waiting for backend...</p>
        </div>

        <div className="card">
          <h2>📚 RAG</h2>
          <input placeholder="Ask question..." />
          <button>Run</button>
          <p className="result">Waiting for backend...</p>
        </div>

      </div>
    </div>
  );
}