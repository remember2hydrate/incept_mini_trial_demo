# incept_mini_trial_demo


Login → HTMX form, Django auth.
Dashboard → Shows:
  Patient table (HTMX polling updates every 10s).
  Chart.js trial allocation summary.
  “Add Patient” button → opens modal.
Add Patient modal → Input name → triggers search via HTMX.
  If patient exists → auto-fill form.
  If not → create new patient.
  On save → encrypt PII, assign random trial, return updated table row + update chart.
Encryption → EncryptedCharField / EncryptedTextField for PII, plus name_hash for searching.
Deployment →
  Local: docker-compose up (Django + Postgres).
  Render: push repo, attach Render Postgres, set env vars, deploy.
