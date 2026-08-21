function Barcode() {
  // Decorative barcode built from a deterministic-looking bar pattern.
  // Purely visual — no data is encoded.
  const widths = [2, 1, 3, 1, 1, 2, 1, 4, 2, 1, 1, 3, 2, 1, 2, 1, 1, 3, 1, 2, 1, 4, 1, 1, 2]
  let x = 0
  return (
    <svg className="barcode" viewBox="0 0 220 28" preserveAspectRatio="none" aria-hidden="true">
      {widths.map((w, i) => {
        const bar = (
          <rect
            key={i}
            x={x}
            y="0"
            width={w}
            height="28"
            fill={i % 2 === 0 ? 'currentColor' : 'transparent'}
          />
        )
        x += w + 1.4
        return bar
      })}
    </svg>
  )
}

function Field({ label, children, mono = false }) {
  return (
    <div className="field">
      <div className="field__label">{label}</div>
      <div className={mono ? 'field__value field__value--mono' : 'field__value'}>{children}</div>
    </div>
  )
}

export default function DrugLabelCard({ drug }) {
  return (
    <article className="label-card">
      <div className="label-card__header">
        <div className="label-card__eyebrow">Vault record</div>
        <h2 className="label-card__name">{drug.drug_name}</h2>
        <div className="label-card__subline">
          <span className="label-card__generic">{drug.generic_name}</span>
        </div>
      </div>

      <div className="label-card__meta">
        <Field label="Manufacturer" mono>
          {drug.manufacturer}
        </Field>
      </div>

      <div className="label-card__barcode">
        <Barcode />
      </div>

      <div className="perforation" role="presentation" />

      <div className="label-card__body">
        <Field label="Purpose">{drug.purpose}</Field>
        <Field label="Active ingredient">{drug.active_ingredient}</Field>
        <Field label="Dosage and administration">{drug.dosage_and_administration}</Field>
      </div>

      <div className="perforation" role="presentation" />

      <div className="label-card__warnings">
        <div className="field__label field__label--warn">Warnings</div>
        <p className="label-card__warnings-text">{drug.warnings}</p>
      </div>
    </article>
  )
}
