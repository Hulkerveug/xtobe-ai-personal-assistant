import React from 'react'
import { GuardianState } from '../App'

export default function GuardianVoicePanel({ onStateChange }: { onStateChange: (s: GuardianState) => void }){
  const langs = ['English','Tamil','Sinhala','Arabic','Hindi','Urdu','Malayalam']
  return (
    <div style={{position:'fixed',right:32,top:80,width:480,background:'rgba(12,18,32,0.6)',padding:16,borderRadius:12}}>
      <div style={{display:'flex',justifyContent:'space-between',alignItems:'center'}}>
        <div>
          <strong>Guardian Listening</strong>
          <div style={{fontSize:12,color:'rgba(241,246,255,0.7)'}}>Session state: Demo listening</div>
        </div>
        <select className="language-select" defaultValue="English">
          {langs.map(l=> <option key={l} value={l}>{l}</option>)}
        </select>
      </div>

      <div style={{marginTop:12,display:'flex',gap:12}}>
        <button className="btn" onClick={() => onStateChange('processing_mock')}>Stop</button>
        <button className="btn" onClick={() => onStateChange('processing_mock')}>Mock Microphone</button>
      </div>

      <div style={{marginTop:12}} className="transcript">
        <div><em>Transcript (demo):</em></div>
        <div style={{marginTop:6}}>“XTOBE, show today’s opportunities.”</div>
        <div style={{marginTop:6}}>“XTOBE, prepare my application plan.”</div>
        <div style={{marginTop:6}}>“XTOBE, open Mission Control.”</div>
      </div>
    </div>
  )
}
