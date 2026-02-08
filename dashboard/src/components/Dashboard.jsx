import { useEffect, useState } from "react";
import { fetchSensors, fetchAlerts } from "../api";
import SensorCard from "./SensorCard";
import Alerts from "./Alerts";

export default function Dashboard() {
  const [sensors, setSensors] = useState([]);
  const [alerts, setAlerts] = useState([]);

  useEffect(() => {
    const interval = setInterval(async () => {
      setSensors(await fetchSensors());
      setAlerts(await fetchAlerts());
    }, 2000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div style={{ padding: 20 }}>
      <h1>Industrial IoT Security Dashboard</h1>
      <div style={{ display: "flex", gap: 20 }}>
        {sensors.map((s, i) => <SensorCard key={i} data={s} />)}
      </div>
      <Alerts alerts={alerts} />
    </div>
  );
}
