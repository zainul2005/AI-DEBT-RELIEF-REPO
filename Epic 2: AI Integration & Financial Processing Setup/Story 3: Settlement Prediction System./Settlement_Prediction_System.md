# Settlement Prediction System

## Objective

The Settlement Prediction System analyzes borrower financial information and loan details to recommend an optimal settlement percentage and classify the loan into a risk category.

## Features

- Calculates settlement percentage.
- Evaluates borrower financial health.
- Analyzes overdue loans.
- Considers EMI burden.
- Calculates loan risk score.
- Classifies loans into Low, Medium, or High risk.

## Settlement Logic

The prediction engine considers:

- Outstanding loan amount
- Interest rate
- EMI ratio
- Debt-to-income ratio
- Overdue months

The system adjusts the settlement percentage based on these factors.

## Risk Categories

| Risk Score | Category |
|------------|----------|
| 0–19 | Low |
| 20–39 | Medium |
| 40+ | High |

## Output

The module generates:

- Loan ID
- Lender Name
- Suggested Settlement Percentage
- Risk Score
- Risk Category

## Conclusion

The Settlement Prediction System provides intelligent settlement recommendations based on borrower financial conditions and loan portfolio analysis. These predictions support AI-powered debt negotiation and financial recovery planning.
