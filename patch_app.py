import os

app_code = '''import React from 'react';
import { DeviceManager } from './components/DeviceManager';
import { DispenserControl } from './components/DispenserControl';
import { CaregiverDashboard } from './components/CaregiverDashboard';

export function App() {
  return (
    <div style={{ maxWidth: '900px', margin: '0 auto', padding: '1rem', fontFamily: 'sans-serif' }}>
      <h1>DoseCompass Control Center</h1>
      <DeviceManager />
      <DispenserControl />
      <CaregiverDashboard />
    </div>
  );
}

export default App;
'''

target = "src/App.tsx" if os.path.exists("src/App.tsx") else "src/App.jsx"

with open(target, "w", encoding="utf-8") as f:
    f.write(app_code)

print(f"Successfully updated {target} to show your BLE controls!")