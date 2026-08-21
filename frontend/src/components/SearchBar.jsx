import { useState } from 'react'

export default function SearchBar({ onSearch, isLoading, initialValue = '' }) {
  const [value, setValue] = useState(initialValue)

  function handleSubmit(event) {
    event.preventDefault()
    const trimmed = value.trim()
    if (!trimmed || isLoading) return
    onSearch(trimmed)
  }

  return (
    <form className="search" onSubmit={handleSubmit}>
      <label className="search__label" htmlFor="drug-search-input">
        Search records
      </label>
      <div className="search__row">
        <input
          id="drug-search-input"
          className="search__input"
          type="text"
          placeholder="Brand name — e.g. Tylenol, Advil, Zyrtec"
          value={value}
          onChange={(e) => setValue(e.target.value)}
          autoComplete="off"
          spellCheck="false"
          disabled={isLoading}
        />
        <button className="search__button" type="submit" disabled={isLoading}>
          {isLoading ? 'Pulling…' : 'Pull record'}
        </button>
      </div>
    </form>
  )
}
