function DialMark() {
  // A small combination-lock dial: the "vault" signature in miniature.
  return (
    <svg viewBox="0 0 40 40" width="30" height="30" aria-hidden="true">
      <circle cx="20" cy="20" r="17" fill="none" stroke="currentColor" strokeWidth="1.6" />
      <circle cx="20" cy="20" r="10.5" fill="none" stroke="currentColor" strokeWidth="1.2" />
      <circle cx="20" cy="20" r="2" fill="currentColor" />
      {Array.from({ length: 12 }).map((_, i) => {
        const angle = (i / 12) * Math.PI * 2
        const x1 = 20 + Math.cos(angle) * 15
        const y1 = 20 + Math.sin(angle) * 15
        const x2 = 20 + Math.cos(angle) * 17.6
        const y2 = 20 + Math.sin(angle) * 17.6
        return (
          <line key={i} x1={x1} y1={y1} x2={x2} y2={y2} stroke="currentColor" strokeWidth="1.2" />
        )
      })}
      <line x1="20" y1="20" x2="20" y2="7" stroke="currentColor" strokeWidth="1.6" />
    </svg>
  )
}

export default function Header() {
  return (
    <header className="site-header">
      <div className="wordmark">
        <span className="wordmark__mark"><DialMark /></span>
        <span className="wordmark__text">
          <span className="wordmark__title">Drug Vault</span>
          <span className="wordmark__subtitle">FDA label records, on request</span>
        </span>
      </div>
    </header>
  )
}
