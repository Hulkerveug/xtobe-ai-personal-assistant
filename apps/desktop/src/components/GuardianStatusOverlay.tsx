import React from 'react'
import { GuardianState } from '../App'

export default function GuardianStatusOverlay({ state }: { state: GuardianState }){
  const map: Record<string,string> = {
    idle: 'Awaiting Verified Input',
    activating: 'Activation Sequence Ready',
    listening_mock: 'Guardian Listening (Demo)',
    processing_mock: 'Processing Command (Demo)',
    verification_required: 'Secure Session Check Required',
    ready: 'Mission Control Ready',
    transitioning_to_dashboard: 'Transitioning to Mission Control',
    error: 'Error — returning to idle'
  }
  return (
    <div style={{position:'fixed',left:20,top:20,background:'rgba(4,6,12,0.6)',padding:'8px 12px',borderRadius:8}}>
      <small style={{color:'rgba(241,246,255,0.75)'}}>{map[state]}</small>
    </div>
  )
}
