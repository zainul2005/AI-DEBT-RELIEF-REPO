# Loan & Settlement Processing Functionality

## Objective

The Loan & Settlement Processing module manages borrower loan information and generates intelligent settlement recommendations.

## Features

- Loan record processing
- Settlement percentage calculation
- Loan priority classification
- Negotiation letter generation

## Settlement Logic

The settlement percentage is determined based on the number of overdue months.

| Overdue Months | Settlement |
|---------------|------------|
| 0 | 50% |
| 1–3 | 55% |
| 4–6 | 60% |
| More than 6 | 65–75% |

## Loan Priority

- High
- Medium
- Low

## Output

The module generates:

- Settlement Percentage
- Loan Priority
- Negotiation Letter

## Conclusion

The Loan & Settlement Processing module analyzes borrower loan details and provides settlement recommendations together with lender-specific negotiation letters.
