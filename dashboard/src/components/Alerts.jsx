export default function Alerts({ alerts }) {
  return (
    <div>
      <h2>Alerts</h2>
      {alerts.map((a, i) => (
        <p key={i}>
          [{a.level}] {a.sensor} → {a.value}
        </p>
      ))}
    </div>
  );
}
