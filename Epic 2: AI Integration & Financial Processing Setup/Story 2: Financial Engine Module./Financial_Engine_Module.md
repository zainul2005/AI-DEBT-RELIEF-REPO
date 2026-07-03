# Financial Engine Module

## Objective

The Financial Engine Module performs real-time financial analysis for borrowers by calculating financial health metrics using borrower income, expenses, and loan portfolio information.

## Features

- EMI-to-Income Ratio Calculation
- Debt-to-Income Ratio Calculation
- Monthly Surplus Calculation
- Outstanding Debt Analysis
- Financial Stress Level Classification

## Financial Metrics

### EMI Ratio

EMI Ratio = (Total EMI / Monthly Income) × 100

### Debt-to-Income Ratio

Debt-to-Income Ratio = (Outstanding Loan Amount / Monthly Income) × 100

### Monthly Surplus

Monthly Surplus = Monthly Income − Monthly Expenses − Total EMI

## Stress Level

| EMI Ratio | Stress Level |
|-----------|--------------|
| Below 30% | Low |
| 30–50% | Medium |
| Above 50% | High |

## Output

The module returns:

- Total EMI
- Outstanding Loan Amount
- Monthly Surplus
- EMI Ratio
- Debt-to-Income Ratio
- Financial Stress Level

## Conclusion

The Financial Engine Module provides the financial foundation for the FinRelief AI platform by evaluating borrower repayment capacity and financial health. These metrics are later used by the Settlement Prediction and AI Negotiation modules.
