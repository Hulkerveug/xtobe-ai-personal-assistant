import React from 'react'
import { GuardianState } from '../App'

export default function GuardianActivationScreen({ state, onStateChange }: { state: GuardianState; onStateChange: (s: GuardianState) => void }){
  return (
    <div className="guardian-screen">
      <div style={{textAlign:'center'}}>
        <h1 style={{margin:0}}>XTOBE FINAL GUARDIAN 2.0</h1>
        <p style={{marginTop:8,color:'rgba(241,246,255,0.7)'}}>INTELLIGENCE • INTEGRITY • HUMAN CONTROL</p>
      </div>

      <div className="guardian-hero" role="img" aria-label="XTOBE FINAL GUARDIAN 2.0">
        <div className="hero-core" aria-hidden>
          {/* mock core; animate via CSS in real app */}
        </div>
      </div>

      <div className="guardian-actions">
        <button className="btn primary" onClick={() => onStateChange('activating')}>ACTIVATE</button>
        <button className="btn" onClick={() => onStateChange('transitioning_to_dashboard')}>SKIP / ENTER COMMAND CENTER</button>
        <label style={{display:'inline-flex',alignItems:'center',gap:8}}>
          <input type="checkbox" /> SOUND
        </label>
      </div>
    </div>
  )
}
