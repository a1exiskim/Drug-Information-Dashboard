import { useState, useRef } from 'react'
import Header from './components/Header.jsx'
import SearchBar from './components/SearchBar.jsx'
import EmptyState from './components/EmptyState.jsx'
import LoadingState from './components/LoadingState.jsx'
import NotFoundState from './components/NotFoundState.jsx'
import ErrorState from './components/ErrorState.jsx'
import DrugLabelCard from './components/DrugLabelCard.jsx'
import { fetchDrug } from './api.js'

// view: 'empty' | 'loading' | 'success' | 'notfound' | 'error'

export default function App() {
  const [view, setView] = useState('empty')
  const [drug, setDrug] = useState(null)
  const [query, setQuery] = useState('')
  const lastQuery = useRef('')

  async function runSearch(name) {
    lastQuery.current = name
    setQuery(name)
    setView('loading')

    const result = await fetchDrug(name)

    // Guard against a stale response landing after a newer search started.
    if (lastQuery.current !== name) return

    if (result.status === 'success') {
      setDrug(result.data)
      setView('success')
    } else if (result.status === 'notfound') {
      setDrug(null)
      setView('notfound')
    } else {
      setDrug(null)
      setView('error')
    }
  }

  function handleRetry() {
    if (query) runSearch(query)
  }

  return (
    <div className="page">
      <Header />

      <main className="content">
        <SearchBar onSearch={runSearch} isLoading={view === 'loading'} initialValue={query} />

        <section className="results" aria-live="polite">
          {view === 'empty' && <EmptyState />}
          {view === 'loading' && <LoadingState />}
          {view === 'success' && drug && <DrugLabelCard drug={drug} />}
          {view === 'notfound' && <NotFoundState query={query} />}
          {view === 'error' && <ErrorState onRetry={handleRetry} />}
        </section>
      </main>

      <footer className="site-footer">
        <span>Sourced from OpenFDA drug label data.</span>
      </footer>
    </div>
  )
}
