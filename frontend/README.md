# Drug Vault — frontend

React + Vite frontend for the Drug Vault FastAPI backend. Pure UI layer: it
only ever talks to `GET /drugs/{drug_name}` on your backend, never to
PostgreSQL or OpenFDA directly.

## Setup

```bash
npm install
npm run dev
```

The dev server proxies `/drugs/*` requests to `http://localhost:8000`
(see `vite.config.js`), so run your FastAPI backend on that port, or edit
the `target` in `vite.config.js` to match wherever it's running.

## Build

```bash
npm run build
```

Outputs static files to `dist/`, which you can serve with any static host.
If you deploy the frontend separately from the backend, update the API
base URL in `src/api.js` (currently a relative path that relies on the
dev proxy or same-origin deployment) and set up CORS on the FastAPI side.

## Structure

```
src/
  api.js                       fetch(...) wrapper — the only file that
                                knows the backend route shape
  App.jsx                      owns search state, picks which view to show
  index.css                    design system (tokens + all component styles)
  components/
    Header.jsx                 wordmark
    SearchBar.jsx               drug name input + submit
    DrugLabelCard.jsx          the result — styled as a prescription label
    EmptyState.jsx             before any search
    LoadingState.jsx           skeleton while a request is in flight
    NotFoundState.jsx          backend returned 404
    ErrorState.jsx             backend returned a non-404 error, with retry
```

## Design notes

The result card is deliberately styled like a pulled prescription label —
eyebrow, bold name, italic generic name, a decorative barcode, and dashed
"perforation" rules separating sections — rather than a generic dashboard
panel, in keeping with the "vault of records" concept. Warnings get a
left-bordered tinted block instead of full alarm-red, per the design brief.
