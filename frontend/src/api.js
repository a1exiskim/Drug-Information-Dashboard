// The only place in the frontend that knows about the backend route.
// Everything else works with the { status, data } shape this returns.
//
// status is one of: 'success' | 'notfound' | 'error'

export async function fetchDrug(drugName) {
  let response
  try {
    response = await fetch(`/drugs/${encodeURIComponent(drugName)}`)
  } catch {
    return { status: 'error', data: null }
  }

  if (response.status === 404) {
    return { status: 'notfound', data: null }
  }

  if (!response.ok) {
    return { status: 'error', data: null }
  }

  try {
    const data = await response.json()
    return { status: 'success', data }
  } catch {
    return { status: 'error', data: null }
  }
}
