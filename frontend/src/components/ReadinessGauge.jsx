import React from "react";
import { CircularProgressbar } from "react-circular-progressbar";
import "react-circular-progressbar/dist/styles.css";

export default function ReadinessGauge({score}) {

 return (
  <div style={{width:"200px",margin:"auto"}}>
   <CircularProgressbar
    value={score}
    text={`${score}%`}
   />
  </div>
 );
}