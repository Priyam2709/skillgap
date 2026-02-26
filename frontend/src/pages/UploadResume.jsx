import React, { useState } from "react";
import API from "../services/api";

function UploadResume() {

  const [resume, setResume] = useState(null);
  const [jd, setJd] = useState("");
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append("resume", resume);
    formData.append("job_description", jd);

    try {
      const response = await API.post("/analyze/", formData, {
        headers: {
          "Content-Type": "multipart/form-data"
        }
      });

      setResult(response.data);

    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div>
      <h2>Upload Resume</h2>

      <form onSubmit={handleSubmit}>
        <input
          type="file"
          onChange={(e) => setResume(e.target.files[0])}
        />

        <textarea
          placeholder="Paste Job Description"
          value={jd}
          onChange={(e) => setJd(e.target.value)}
        />

        <button type="submit">Analyze</button>
      </form>

      {result && (
        <div>
          <h3>Readiness Score: {result.readiness_score}</h3>

          <h4>Missing Skills:</h4>
          <ul>
            {result.missing_skills.map((s,i) => (
              <li key={i}>{s}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default UploadResume;