// RiskChart.js

import React, { useEffect, useState } from "react";
import axios from "axios";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";

function RiskChart() {
  const [data, setData] = useState([]);

  useEffect(() => {
    // Fetch historical data from your backend
    axios
      .get("http://127.0.0.1:8000/historical-data")
      .then((response) => {
        setData(response.data);
      })
      .catch((error) => {
        console.error("Error fetching historical data", error);
      });
  }, []);

  return (
    <div>
      <h2>Price and Risk Over Time</h2>
      <ResponsiveContainer width="100%" height={400}>
        <LineChart
          data={data}
          margin={{ top: 30, right: 30, left: 30, bottom: 5 }}
        >
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis
            dataKey="date"
            tickFormatter={(dateStr) => {
              const date = new Date(dateStr);
              return `${date.getMonth() + 1}/${date.getDate()}`;
            }}
          />

          <YAxis
            yAxisId="left"
            domain={["auto", "auto"]}
            label={{ value: "Price", angle: -90, position: "insideLeft" }}
          />
          <YAxis
            yAxisId="right"
            orientation="right"
            domain={[0, 1]}
            label={{ value: "Risk Score", angle: 90, position: "insideRight" }}
          />
          <Tooltip />
          <Legend />
          <Line
            yAxisId="left"
            type="monotone"
            dataKey="price"
            stroke="#8884d8"
            dot={false}
            name="Price"
          />
          <Line
            yAxisId="right"
            type="stepAfter"
            dataKey="risk_score"
            stroke="#82ca9d"
            dot={false}
            name="Risk Score"
            strokeDasharray="5 5"
          />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}

export default RiskChart;
