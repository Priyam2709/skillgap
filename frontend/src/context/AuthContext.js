import { createContext,useState,useEffect } from "react";

export const AuthContext=createContext();

export const AuthProvider=({children})=>{

const [isAuth,setIsAuth]=useState(false);

useEffect(()=>{
const token=localStorage.getItem("token");
if(token){
setIsAuth(true);
}
},[]);

return(
<AuthContext.Provider value={{isAuth,setIsAuth}}>
{children}
</AuthContext.Provider>
);
};