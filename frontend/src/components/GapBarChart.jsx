import { BarChart, Bar, XAxis } from "recharts";

export default function GapBarChart({data}) {

 return (
  <BarChart width={400} height={250} data={data}>
   <XAxis dataKey="type"/>
   <Bar dataKey="count"/>
  </BarChart>
 );
}