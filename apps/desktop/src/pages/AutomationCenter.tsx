import React from 'react'

export default function AutomationCenter(){
  return (
    <div style={{padding:24}}>
      <h2>Automation Center (Demo)</h2>
      <p>This is a local-only mock Automation Center showing registered workflows and execution history.</p>
      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:16}}>
        <section style={{background:'rgba(255,255,255,0.02)',padding:12,borderRadius:8}}>
          <h3>Registered Workflows</h3>
          <ul>
            <li>daily-expo-watch (Mock)</li>
            <li>application-prep (Mock)</li>
            <li>github-briefing (Mock)</li>
            <li>morning-briefing (Mock)</li>
            <li>reminder-planning (Mock)</li>
          </ul>
        </section>
        <section style={{background:'rgba(255,255,255,0.02)',padding:12,borderRadius:8}}>
          <h3>Recent Executions</h3>
          <p>Execution history is stored locally in a mock SQLite store.</p>
        </section>
      </div>
    </div>
  )
}
