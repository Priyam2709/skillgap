import React,{useState} from "react";
import axios from "../utils/axiosInstance";
import { useNavigate } from "react-router-dom";

function AuthPage(){

 const [isLogin,setIsLogin]=useState(true);
 const [username,setUsername]=useState("");
 const [password,setPassword]=useState("");

 const navigate = useNavigate();

 const handleAuth = async () => {

  try{

   if(isLogin){

    const res = await axios.post("login/",{
     username,
     password
    });

    localStorage.setItem("access",res.data.access);
    localStorage.setItem("refresh",res.data.refresh);

    navigate("/home");

   }else{

    await axios.post("register/",{
     username,
     password
    });

    alert("Registered Successfully! Now Login.");
    setIsLogin(true);

   }

  }catch(err){
   alert("Error Occurred");
  }
 };

 return(

 <div className="min-h-screen flex items-center justify-center bg-gray-100">

  <div className="bg-white p-10 rounded-xl shadow w-96">

   <h2 className="text-2xl font-bold mb-6 text-center">
    Skill Gap Analyzer
   </h2>

   <input
    className="border p-2 w-full mb-4 rounded"
    placeholder="Username"
    onChange={(e)=>setUsername(e.target.value)}
   />

   <input
    type="password"
    className="border p-2 w-full mb-6 rounded"
    placeholder="Password"
    onChange={(e)=>setPassword(e.target.value)}
   />

   <button
    onClick={handleAuth}
    className="bg-blue-500 text-white w-full py-2 rounded-lg"
   >
    {isLogin ? "Login" : "Register"}
   </button>

   <p
    className="mt-4 text-center text-blue-500 cursor-pointer"
    onClick={()=>setIsLogin(!isLogin)}
   >
    {isLogin ?
     "Don't have an account? Register" :
     "Already have an account? Login"}
   </p>

  </div>

 </div>
 );
}

export default AuthPage;