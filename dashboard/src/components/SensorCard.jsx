export default function SensorCard({ data }) {
  return (
    <div style={{ border: "1px solid #ccc", padding: 10 }}>
      <h3>{data.sensor_type}</h3>
      <p>Value: {data.value}</p>
      <p>Device: {data.device_id}</p>
    </div>
  );
}
