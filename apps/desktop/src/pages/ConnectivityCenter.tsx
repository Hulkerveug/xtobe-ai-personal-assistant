import React, { useEffect, useState } from 'react'

export default function ConnectivityCenter(){
  const [providers, setProviders] = useState<any[]>([])

  useEffect(()=>{
    // fetch mock provider list from local API if available
    fetch('/api/connectivity/providers').then(r=>r.json()).then(j=> setProviders(j.providers || [])).catch(()=> setProviders([]))
  },[])

  return (
    <div style={{padding:24}}>
      <h2>Connectivity Center (Demo)</h2>
      <p>Local-only mock of connectivity transports (Ethernet, Wi‑Fi, Cellular, Starlink).</p>
      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:12}}>
        {providers.length===0 && <div style={{gridColumn:'1 / -1'}}>No API available — showing client stub.</div>}
        <div style={{background:'rgba(255,255,255,0.02)',padding:12,borderRadius:8}}>
          <h3>Transport Status</h3>
          <ul>
            <li>Ethernet — Connected (mock)</li>
            <li>Wi‑Fi (Office‑WiFi) — Connected (mock)</li>
            <li>Cellular — Connected (mock)</li>
            <li>Starlink — Not present (mock)</li>
          </ul>
        </div>
        <div style={{background:'rgba(255,255,255,0.02)',padding:12,borderRadius:8}}>
          <h3>Actions</h3>
          <button className="btn" onClick={()=> alert('Simulate ethernet disconnect — client-only demo')}>Simulate Ethernet Disconnect</button>
          <button className="btn" onClick={()=> alert('Simulate Starlink present — client-only demo')}>Simulate Starlink Presence</button>
        </div>
      </div>
    </div>
  )
}
