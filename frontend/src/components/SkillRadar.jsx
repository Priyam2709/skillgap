import {
 Radar,
 RadarChart,
 PolarGrid,
 PolarAngleAxis,
 PolarRadiusAxis
} from "recharts";

export default function SkillRadar({data}) {

 if(!data) return null;

 const radarData = Object.keys(data).map(k=>({
  skill:k,
  score:data[k]
 }));

 return (
  <RadarChart
   outerRadius={120}
   width={400}
   height={300}
   data={radarData}
  >
   <PolarGrid />
   <PolarAngleAxis dataKey="skill" />
   <PolarRadiusAxis />
   <Radar dataKey="score"/>
  </RadarChart>
 );
}