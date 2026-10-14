import React from 'react'

export default function ConnectivityPanel({status}:{status?:any}){
  return (
    <div style={{padding:12,background:'rgba(255,255,255,0.02)',borderRadius:8}}>
      <h4>{status?.name||'Transport'}</h4>
      <div>State: {status?.state||'unknown'}</div>
      <div>Latency: {status?.latency_ms ?? 'n/a'} ms</div>
    </div>
  )
}
