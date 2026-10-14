import React, { useRef, useEffect } from 'react'

export default function ParticleNetworkOverlay(){
  const canvasRef = useRef<HTMLCanvasElement | null>(null)

  useEffect(()=>{
    const c = canvasRef.current
    if(!c) return
    const ctx = c.getContext('2d')!
    let raf = 0
    let w = c.width = c.clientWidth
    let h = c.height = c.clientHeight
    const particles = Array.from({length:30}).map(()=>({x:Math.random()*w,y:Math.random()*h,vx:(Math.random()-0.5)*0.3,vy:(Math.random()-0.5)*0.3}))

    function tick(){
      ctx.clearRect(0,0,w,h)
      ctx.strokeStyle = 'rgba(255,138,26,0.6)'
      ctx.fillStyle = 'rgba(255,138,26,0.9)'
      particles.forEach(p=>{
        p.x += p.vx; p.y += p.vy
        if(p.x<0||p.x>w) p.vx *= -1
        if(p.y<0||p.y>h) p.vy *= -1
        ctx.beginPath(); ctx.arc(p.x,p.y,2,0,Math.PI*2); ctx.fill()
      })
      raf = requestAnimationFrame(tick)
    }
    tick()
    return ()=> cancelAnimationFrame(raf)
  },[])

  return <canvas ref={canvasRef} style={{position:'absolute',inset:0,pointerEvents:'none'}} />
}
