export default function LoadingState() {
  return (
    <div className="state state--loading" role="status" aria-live="polite">
      <div className="skeleton-card">
        <div className="skeleton-line skeleton-line--title" />
        <div className="skeleton-line skeleton-line--sub" />
        <div className="skeleton-line skeleton-line--bar" />
        <div className="skeleton-line" />
        <div className="skeleton-line" />
        <div className="skeleton-line skeleton-line--short" />
      </div>
      <p className="state__text">Pulling the record…</p>
    </div>
  )
}
