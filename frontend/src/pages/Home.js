import React,{useState} from "react";
import axios from "../utils/axiosInstance";
import { useNavigate } from "react-router-dom";

function HomePage(){

 const [file,setFile]=useState(null);
 const [jd,setJD]=useState("");

 const navigate = useNavigate();

 const handleAnalyze = async () => {

  try{

   const formData = new FormData();
   formData.append("resume",file);
   formData.append("job_description",jd);

   const token = localStorage.getItem("access");

   const res = await axios.post(
    "analyze/",
    formData,
    {
     headers:{
      "Content-Type":"multipart/form-data",
      "Authorization":`Bearer ${token}`
     }
    }
   );

   navigate("/dashboard",{state:res.data});

  }catch(err){
   alert("Analysis Failed");
  }
 };
const handleLogout = () => {
 localStorage.removeItem("access");
 localStorage.removeItem("refresh");
 navigate("/");
};
 return(

 <div className="min-h-screen bg-gray-100 p-10">

  <h1 className="text-3xl font-bold mb-8 text-gray-700">
   Resume Readiness Analyzer
  </h1>

  <div className="bg-white p-8 rounded-xl shadow max-w-xl">

   <label className="block mb-2 font-semibold">
    Upload Resume
   </label>

   <input
    type="file"
    className="mb-6"
    onChange={(e)=>setFile(e.target.files[0])}
   />

   <label className="block mb-2 font-semibold">
    Job Description
   </label>

   <textarea
    rows="6"
    className="border p-2 w-full mb-6 rounded"
    placeholder="Paste JD here"
    onChange={(e)=>setJD(e.target.value)}
   />

   <button
    onClick={handleAnalyze}
    className="bg-green-500 text-white px-6 py-2 rounded-lg"
   >
    Analyze
   </button>
  <div className="flex justify-end mb-4">



</div>
<button
 onClick={handleLogout}
 className="bg-red-500 text-white px-4 py-2 rounded-lg"
>
 Logout
</button>
  </div>

 </div>
 );
}

export default HomePage;