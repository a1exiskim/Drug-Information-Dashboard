export default function EmptyState() {
  return (
    <div className="state state--empty">
      <div className="state__icon" aria-hidden="true">
        <svg viewBox="0 0 48 48" width="40" height="40">
          <rect x="8" y="6" width="32" height="36" rx="2" fill="none" stroke="currentColor" strokeWidth="1.5" />
          <line x1="15" y1="16" x2="33" y2="16" stroke="currentColor" strokeWidth="1.5" />
          <line x1="15" y1="23" x2="33" y2="23" stroke="currentColor" strokeWidth="1.5" />
          <line x1="15" y1="30" x2="26" y2="30" stroke="currentColor" strokeWidth="1.5" />
        </svg>
      </div>
      <h2 className="state__title">No record open</h2>
      <p className="state__text">
        Search a brand name above to pull its label from the vault.
      </p>
    </div>
  )
}
