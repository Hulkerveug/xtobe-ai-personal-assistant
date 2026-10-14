import React from 'react'

export default function GuardianEmblemBadge(){
  return (
    <div style={{width:40,height:40,background:'linear-gradient(180deg,#0b1222,#121c35)',borderRadius:8,display:'flex',alignItems:'center',justifyContent:'center',boxShadow:'0 6px 18px rgba(0,0,0,0.6)'}}>
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden>
        <path d="M12 2L3 6v5c0 5 3.7 9.5 9 11 5.3-1.5 9-6 9-11V6l-9-4z" fill="#121C35" />
        <circle cx="12" cy="11" r="3" fill="#27D8F5" />
      </svg>
    </div>
  )
}
