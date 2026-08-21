export default function NotFoundState({ query }) {
  return (
    <div className="state state--notfound">
      <div className="state__icon" aria-hidden="true">
        <svg viewBox="0 0 48 48" width="40" height="40">
          <rect x="8" y="10" width="32" height="30" rx="2" fill="none" stroke="currentColor" strokeWidth="1.5" />
          <line x1="17" y1="21" x2="23" y2="27" stroke="currentColor" strokeWidth="1.5" />
          <line x1="23" y1="21" x2="17" y2="27" stroke="currentColor" strokeWidth="1.5" />
        </svg>
      </div>
      <h2 className="state__title">No record for &ldquo;{query}&rdquo;</h2>
      <p className="state__text">
        The vault doesn&rsquo;t have a label under that name. Check the spelling, or try the
        brand name rather than the generic name.
      </p>
    </div>
  )
}
