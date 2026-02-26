import React, { useEffect, useState } from "react";
import axios from "axios";

function History() {

  const [history, setHistory] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/history/")
      .then(res => setHistory(res.data))
      .catch(err => console.log(err));
  }, []);

  return (
    <div>
      <h2>Analysis History</h2>
      {
        history.map((item, index) => (
          <div key={index}>
            <h4>Score: {item.readiness_score}%</h4>
            <p>Missing Skills: {item.missing_skills}</p>
          </div>
        ))
      }
    </div>
  );
}

export default History;