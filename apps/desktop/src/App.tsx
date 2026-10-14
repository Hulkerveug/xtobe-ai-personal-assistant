import React, { useEffect, useState } from 'react'
import GuardianActivationScreen from './components/GuardianActivationScreen'
import GuardianVoicePanel from './components/GuardianVoicePanel'
import GuardianStatusOverlay from './components/GuardianStatusOverlay'

export type GuardianState =
  | 'idle'
  | 'activating'
  | 'listening_mock'
  | 'processing_mock'
  | 'verification_required'
  | 'ready'
  | 'transitioning_to_dashboard'
  | 'error'

export default function App() {
  const [state, setState] = useState<GuardianState>('idle')

  useEffect(() => {
    // example: if activating, auto-advance to listening_mock
    if (state === 'activating') {
      const t = setTimeout(() => setState('listening_mock'), 1400)
      return () => clearTimeout(t)
    }
    if (state === 'listening_mock') {
      const t = setTimeout(() => setState('processing_mock'), 3000)
      return () => clearTimeout(t)
    }
    if (state === 'processing_mock') {
      const t = setTimeout(() => setState('verification_required'), 2000)
      return () => clearTimeout(t)
    }
  }, [state])

  return (
    <div className="app-root">
      {state !== 'transitioning_to_dashboard' && (
        <GuardianActivationScreen state={state} onStateChange={setState} />
      )}

      {state === 'listening_mock' && (
        <GuardianVoicePanel onStateChange={setState} />
      )}

      <GuardianStatusOverlay state={state} />

      {state === 'ready' && (
        <div className="mission-control">
          <header>
            <h2>Mission Control</h2>
            <p>Mission Control Ready — demo</p>
          </header>
          <main>
            <p>Dashboard content placeholder. Transitioned from Guardian.</p>
          </main>
        </div>
      )}

      {state === 'verification_required' && (
        <div className="verification">
          <p className="verification-note">SECURE SESSION CHECK REQUIRED (DEMO VISUAL STATE)</p>
          <button onClick={() => setState('ready')}>Continue to Mission Control (Demo)</button>
        </div>
      )}
    </div>
  )
}
