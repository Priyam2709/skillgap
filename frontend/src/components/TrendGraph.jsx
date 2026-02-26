import React,{useEffect,useState} from "react";
import axios from "../utils/axiosInstance";
import { LineChart, Line, XAxis, YAxis } from "recharts";

export default function TrendGraph(){

 const [data,setData]=useState([]);

 useEffect(()=>{

  axios.get("/trend/")
  .then(res=>setData(res.data))
  .catch(err=>console.log(err));

 },[]);

 return(

  <LineChart width={500} height={300} data={data}>
   <XAxis dataKey="date"/>
   <YAxis/>
   <Line type="monotone" dataKey="score"/>
  </LineChart>

 );
}