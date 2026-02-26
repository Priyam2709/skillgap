import React from "react";
import { useLocation } from "react-router-dom";
import SkillRadar from "../components/SkillRadar";
import GapBarChart from "../components/GapBarChart";
import ReadinessGauge from "../components/ReadinessGauge";
import TrendGraph from "../components/TrendGraph";
import { useNavigate } from "react-router-dom";
function Dashboard() {

 const navigate = useNavigate();

const handleLogout = () => {
 localStorage.removeItem("access");
 localStorage.removeItem("refresh");
 navigate("/");
};


 const location = useLocation();
const data = location.state || {};

 if(!data) return <h2>No Data</h2>;

 const gapData = [
 {
  type:"Matched",
  count:data.matched_skills ? data.matched_skills.length : 0
 },
 {
  type:"Missing",
  count:data.missing_skills ? data.missing_skills.length : 0
 }
];

 return (

 <div className="min-h-screen bg-gray-100 p-8">

  <h1 className="text-3xl font-bold mb-8 text-gray-700">
   AI Role Readiness Dashboard
  </h1>
 <div className="flex gap-4 mb-6">



</div>
  {/* TOP ROW */}
  <div className="grid grid-cols-3 gap-6">

   <div className="bg-white p-6 rounded-xl shadow">
    <h2 className="text-lg font-semibold mb-4">
     Overall Readiness
    </h2>
    <ReadinessGauge score={data.readiness_score}/>
   </div>

   <div className="bg-white p-6 rounded-xl shadow col-span-2">
    <h2 className="text-lg font-semibold mb-4">
     Skill Gap Overview
    </h2>
    <GapBarChart data={gapData}/>
   </div>

  </div>

  {/* MIDDLE ROW */}
  <div className="grid grid-cols-2 gap-6 mt-8">

   <div className="bg-white p-6 rounded-xl shadow">
    <h2 className="text-lg font-semibold mb-4">
     Skill Competency Map
    </h2>
<SkillRadar data={data.skill_breakdown || {}}/>   </div>

   <div className="bg-white p-6 rounded-xl shadow">
    <h2 className="text-lg font-semibold mb-4">
     Readiness Trend
    </h2>
    <TrendGraph/>
   </div>

  </div>

  {/* BOTTOM */}
  <div className="bg-white p-6 rounded-xl shadow mt-8">
   <h2 className="text-lg font-semibold mb-4">
    Learning Roadmap
   </h2>
  

   <ul className="list-disc pl-6 text-gray-700">
    {data.learning_roadmap &&
    data.learning_roadmap.map((s,i)=>     <li key={i}>{s}</li>
    )}
   </ul>
  </div>

<button
 onClick={handleLogout}
 className="bg-red-500 text-white px-4 py-2 rounded-lg shadow"
>
 Logout
</button>

</div>
 );
}

export default Dashboard;