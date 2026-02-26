import React,{useState} from "react";
import axios from "../utils/axiosInstance";
import { setToken } from "../utils/auth";
import { useNavigate } from "react-router-dom";

function Login(){

const [username,setUsername]=useState("");
const [password,setPassword]=useState("");

const navigate=useNavigate();

const loginUser=async()=>{

try{

const res=await axios.post("login/",{
username,
password
});

setToken(res.data.access);
navigate("/home");

}catch(err){
alert("Invalid credentials");
}

};

return(

<div>

<input
placeholder="Username"
onChange={(e)=>setUsername(e.target.value)}
/>

<input
type="password"
placeholder="Password"
onChange={(e)=>setPassword(e.target.value)}
/>

<button onClick={loginUser}>
Login
</button>

</div>
);
}

export default Login;