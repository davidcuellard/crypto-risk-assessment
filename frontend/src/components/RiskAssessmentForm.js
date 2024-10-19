import React, { useState } from "react";
import axios from "axios";

function RiskAssessmentForm() {
  const [formData, setFormData] = useState({
    volatility: "",
    liquidity: "",
    momentum: "",
    avg_sentiment: "",
  });

  const [result, setResult] = useState(null);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: parseFloat(e.target.value),
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    axios
      .post(`${process.env.REACT_APP_API_BASE_URL}/predict`, formData)
      .then((response) => {
        setResult(response.data.risk_level);
      })
      .catch((error) => {
        console.error("There was an error making the request", error);
      });
  };

  return (
    <div>
      <h2>Cryptocurrency Risk Assessment</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Volatility:</label>
          <input
            type="number"
            step="any"
            name="volatility"
            value={formData.volatility}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label>Liquidity:</label>
          <input
            type="number"
            step="any"
            name="liquidity"
            value={formData.liquidity}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label>Momentum:</label>
          <input
            type="number"
            step="any"
            name="momentum"
            value={formData.momentum}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label>Average Sentiment:</label>
          <input
            type="number"
            step="any"
            name="avg_sentiment"
            value={formData.avg_sentiment}
            onChange={handleChange}
            required
          />
        </div>
        <button type="submit">Assess Risk</button>
      </form>
      {result && <h3>Risk Level: {result}</h3>}
    </div>
  );
}

export default RiskAssessmentForm;
