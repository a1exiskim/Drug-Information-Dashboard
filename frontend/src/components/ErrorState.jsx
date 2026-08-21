export default function ErrorState({ onRetry }) {
  return (
    <div className="state state--error">
      <div className="state__icon" aria-hidden="true">
        <svg viewBox="0 0 48 48" width="40" height="40">
          <path
            d="M24 8 L42 38 L6 38 Z"
            fill="none"
            stroke="currentColor"
            strokeWidth="1.5"
            strokeLinejoin="round"
          />
          <line x1="24" y1="20" x2="24" y2="29" stroke="currentColor" strokeWidth="1.5" />
          <circle cx="24" cy="33" r="1.4" fill="currentColor" />
        </svg>
      </div>
      <h2 className="state__title">The vault didn&rsquo;t respond</h2>
      <p className="state__text">
        Something went wrong retrieving this record. Try again in a moment.
      </p>
      <button className="state__retry" type="button" onClick={onRetry}>
        Try again
      </button>
    </div>
  )
}
