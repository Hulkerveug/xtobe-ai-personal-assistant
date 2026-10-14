# SUBSCRIPTION_MODEL.md

# Subscription Model (Phase G — Mock)

Subscription object (fields)
- id
- provider
- plan_name
- currency
- monthly_cost
- billing_period
- data_allowance_bytes
- usage_bytes
- renewal_date
- contract_reference
- source_url
- last_verified
- status (active/inactive/manual)

Notes
- Third-party subscriptions (Starlink, carrier data) are recorded as manual references only in Phase G.
- Do not collect payment info or credentials in Phase G.
