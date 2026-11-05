# Report format

Write detailed findings first and the summary table last, so the summary sits
right above where the reader looks next. Number every finding across both tiers.

- 🔴 **Must fix** (heading): accepted at must-fix severity.
- 🟡 **Recommendation** (heading): accepted at recommendation severity.
- 📄 File location, `path/to/file.rb:42`, RIGHT-side line numbers.
- 🔧 Fix.
- 🗳️ Council vote.

## Order

All 🔴 findings come before all 🟡 findings. Within a tier, rank by impact:

1. Broken build, data loss, or data corruption.
2. Wrong behaviour for users or callers.
3. Security exposure.
4. Broken downstream consumers: callers, services, events, dashboards.
5. Everything else.

## Part A: findings

Start with a one-sentence overview, then each accepted finding:

````
📋 **Overview**: [one sentence on what the PR does and the council's verdict]

---

### 🔴 1. Refund total ignores partial refunds

📄 `app/services/refund_calculator.rb:31-34`

```ruby
def refundable_amount
  order.total - order.refunds.first&.amount.to_i
end
```

Only the first refund is subtracted, so an order with two partial refunds can be
refunded past its total. `RefundsController#create` (app/controllers/refunds_controller.rb:18)
trusts this value as the upper bound.

🔧 **Fix**:
```ruby
def refundable_amount
  order.total - order.refunds.sum(:amount)
end
```

🗳️ **Council**: 8/8 agree · raised by Correctness, Testing · amended by Performance
````

Write the explanation as plain prose under the code: what is wrong and who pays for
it. Show the fix as code when it is five lines or fewer, and as prose otherwise.

## Part B: not agreed (chat only)

After the accepted findings, list each finding the council did not accept:

```
---

### ⚖️ Not agreed

- **Missing index on `refunds.order_id`** (`db/migrate/20261028_add_refunds.rb:5`):
  6 agree, 2 object. Architecture: "the index exists in the previous migration,
  db/migrate/20260901_create_refunds.rb:9." Performance: "agree with Architecture;
  the index is already there."
```

Give the vote split and each objector's reason in its own words. When every finding
was accepted, leave this part out.

## Part C: summary table (last)

```
---

## 📊 Summary

| #  | Sev | File                            | Finding                               | Raised by            |
|----|-----|---------------------------------|---------------------------------------|----------------------|
| 1  | 🔴 | refund_calculator.rb:31         | Refund total ignores partial refunds  | Correctness, Testing |
| 2  | 🟡 | refunds_controller.rb:18        | Refund failure is not reported        | Observability        |

Council: 8 members · 3 rounds · 5 proposed · 2 accepted · 1 not agreed
```

The table holds accepted findings only. Under the table, give the counts line, then
the offer to post from Step 5 of the skill.

## When nothing is accepted

Write the overview, then: "The council found no issues it agreed on." Add the
⚖️ Not agreed part if it has entries, and the counts line. The council does not
invent findings to fill the report.
