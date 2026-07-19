# How Do We Prepare Data for AI?

Data preparation is the work of turning raw information into reliable input for an AI model. It includes checking quality, cleaning errors, choosing useful features, creating labels when needed, splitting data correctly, and protecting sensitive information.

A powerful model cannot compensate for unclear, incorrect, or unsuitable data.

```text
Raw data → inspect → clean → represent → split → train and evaluate a model
```

## Why Data Preparation Matters

Imagine a model that predicts whether a customer may cancel a subscription. Its result depends on the examples it receives. If the data has missing values, duplicated records, inconsistent formats, or information unavailable in the real world, the prediction can be misleading.

| Data problem | Possible consequence |
|---|---|
| Missing or incorrect values | The model learns from incomplete or false information. |
| Inconsistent formats | The same value can be treated as different values. |
| Duplicated rows | Some examples receive unintended extra influence. |
| Unrepresentative data | The model may work poorly for groups or situations not included. |
| Data leakage | Evaluation looks excellent, but real-world performance fails. |
| Sensitive information | Privacy, legal, or fairness risks increase. |

## The Data-Preparation Workflow

```text
1. Define the prediction and available information
2. Collect and document data
3. Inspect quality and distribution
4. Clean errors, duplicates, and missing values
5. Create labels and useful features
6. Represent data in a model-friendly form
7. Split data into training, validation, and test sets
8. Apply transformations without leaking information
9. Review privacy, fairness, and security risks
```

## A Running Example: Predicting Customer Churn

Suppose a subscription service wants to estimate whether a customer is likely to cancel in the next 30 days. It has historical customer records:

| Customer | Days since last login | Support requests | Plan | Cancelled in next 30 days? |
|---|---:|---:|---|---|
| A-102 | 2 | 0 | Basic | No |
| A-103 | 45 | 4 | Premium | Yes |
| A-104 | — | 1 | basic | No |
| A-103 | 45 | 4 | Premium | Yes |

The table looks useful, but it has several problems:

- `—` means a value is missing.
- `Basic` and `basic` use inconsistent text.
- `A-103` appears twice.
- The final column is a label that is known only after the 30-day period ends, so it must not be used as an input feature.

The rest of this lesson prepares this data correctly.

## 1. Define the Problem Before Collecting Data

Start by stating exactly what the model should predict, when it will predict it, and which information is available at that time.

```text
Question: Which active customers are likely to cancel in the next 30 days?
Prediction time: Today
Allowed information: Activity and support history available today
Not allowed: Information that happens after today
```

This prevents accidental use of future information and makes the dataset easier to design.

### Example: A Clear Label

For every historical customer, the label could be:

```text
Cancelled within 30 days after the prediction date?
Yes → 1
No  → 0
```

The prediction date must be defined consistently. Otherwise, two rows may mean different things and the model cannot learn a reliable pattern.

## 2. Inspect the Data Before Changing It

Before cleaning data, look at its structure and ask practical questions:

- What does each row represent: a customer, an order, an email, or an event?
- What does each column mean, and where did it come from?
- Which values are missing or unusual?
- Are the units consistent?
- Does the data represent the people and situations where the model will be used?

### Example: Detecting an Impossible Value

```text
Days since last login: 2, 14, 45, -3
```

`-3` cannot be valid. It may be a data-entry or system error. A team should investigate the source rather than blindly treating it as a normal value.

## 3. Clean Inconsistent Values

Different systems and people often record the same idea in different ways. Cleaning makes values consistent.

### Example: Standardizing Plan Names

```text
Before: Basic, basic, BASIC, Basic plan
After:  basic
```

Without standardization, a model may treat each spelling as a separate category even though they mean the same plan.

### Example: Consistent Units

```text
Before: 1.5 GB, 800 MB, 2 GB
After:  1500 MB, 800 MB, 2000 MB
```

Choose one representation so the model can compare values correctly.

## 4. Handle Missing Values Carefully

Missing data does not always mean the same thing. A value can be missing because a customer skipped a field, a sensor failed, a system did not collect it, or the value is genuinely unknown.

### Example: Missing Login Activity

```text
Days since last login: —
```

Possible approaches include:

| Approach | When it may be appropriate | Example |
|---|---|---|
| **Investigate or correct** | A source-system error can be fixed. | Recover the value from a reliable event log. |
| **Remove the row** | Few records are missing a critical value. | Exclude a small number of unusable records. |
| **Impute a value** | A reasonable estimate is available. | Replace a missing numeric value with the training-set median. |
| **Use an “unknown” category** | Missingness itself may be meaningful. | Use `unknown` for a missing plan type. |
| **Add a missing-value indicator** | The fact that a value is missing may help. | Add `last_login_missing = yes`. |

There is no universal best choice. The correct method depends on why the value is missing and how the model will be used.

## 5. Find and Handle Duplicate Records

Duplicates can make a model give too much importance to repeated examples.

### Example: Duplicate Customer Row

```text
A-103 | 45 days | 4 requests | Premium | Yes
A-103 | 45 days | 4 requests | Premium | Yes
```

If both rows represent the same customer at the same point in time, keep one. If they represent different events, the dataset may need a different structure, such as one row per customer-month rather than one row per customer.

## 6. Create Features That Are Available at Prediction Time

Features are the inputs a model uses. They should be relevant, consistently computed, and available when a prediction is actually made.

| Possible churn feature | Use it? | Reason |
|---|---|---|
| Days since last login | Usually yes | It is known today and may show engagement. |
| Number of recent support requests | Usually yes | It may show an unresolved problem. |
| Current subscription plan | Often yes | It is available before cancellation. |
| Cancellation date | No | It is known only after the outcome. |
| Refund issued after cancellation | No | It happens after the prediction window. |

### Example: Creating a Feature

Raw event data can be turned into a useful summary feature:

```text
Login dates: 1 July, 6 July, 10 July
Prediction date: 20 July

days since last login = 10
```

The same definition must be used during training and when predicting for a new customer.

## 7. Represent Text and Categories as Numbers

Most machine-learning models require numeric input. Categories and text must therefore be represented in a suitable form.

### Example: One-Hot Encoding a Plan

```text
Plan       → [basic, premium, enterprise]
basic      → [1, 0, 0]
premium    → [0, 1, 0]
enterprise → [0, 0, 1]
```

This representation does not imply that `premium` is twice as large as `basic`. It simply indicates which category applies.

### Example: Text Features

For customer-support messages, an application can use:

```text
"I cannot log in" → text representation or embedding → model input vector
```

An embedding turns text into a list of numbers that captures patterns learned from language data. The model works with the vector, not the original sentence directly.

## 8. Scale Numerical Values When Needed

Some models work better when numerical features have comparable ranges. Scaling is especially common for distance-based models and many gradient-based models.

### Example: Different Ranges

```text
days since last login: 0 to 365
support requests:     0 to 10
monthly price:        5 to 500
```

Without scaling, a model may treat large-number features as more important merely because of their numeric range. A common approach is standardization, which centers values around a mean of `0` and a standard deviation of `1`.

Not every model requires scaling, so choose preprocessing based on the model and the data.

## 9. Split Data Before Learning Transformations

Use separate data for training, tuning, and final evaluation:

```text
Training set   → learn model weights and preprocessing values
Validation set → select settings and compare choices
Test set       → final evaluation on unseen data
```

### Example: A Simple Split

For 1,000 historical customer examples:

```text
700 examples → training
150 examples → validation
150 examples → test
```

The exact proportions vary, but the test set must stay separate until the final evaluation.

For time-based predictions, split by time when possible:

```text
January–October records → training
November records        → validation
December records        → test
```

This better matches the real situation: predicting the future from the past.

## 10. Avoid Data Leakage

**Data leakage** happens when a model receives information during training that would not be available when it makes a real prediction. Leakage produces overly optimistic results.

### Example: Leakage from a Future Column

```text
Goal: predict whether a customer will cancel next month

Wrong input: refund issued after cancellation
Why wrong: the refund is only known after the customer cancels
```

### Example: Leakage During Scaling

If you calculate the average and standard deviation using training, validation, and test data together, the training process has indirectly seen the evaluation data.

Correct order:

```text
1. Split the data
2. Learn the scaling values from training data only
3. Apply those same values to validation and test data
```

The same principle applies to filling missing values, selecting features, and any other learned preprocessing step.

## 11. Review Privacy, Fairness, and Security

Data preparation is also a responsible-AI task. Collect only information needed for the defined purpose, secure it, and consider how it may affect different groups.

### Example: Sensitive Customer Data

A churn model may not need a customer's full name, exact address, or government ID. Removing unnecessary personal data reduces privacy risk.

Some features can also act as proxies for sensitive characteristics. For example, location can sometimes correlate with income, ethnicity, or access to services. Teams should examine whether each feature is appropriate for the decision and test performance across relevant groups.

## A Preparation Checklist

- Define the prediction, timing, and allowed data.
- Document what each row and column means.
- Check missing values, duplicates, impossible values, formats, and units.
- Clean consistently without hiding important data issues.
- Create only features available at prediction time.
- Keep labels separate from input features.
- Encode categories and text appropriately.
- Split data before fitting preprocessing steps.
- Keep the test set separate for final evaluation.
- Protect personal data and review fairness risks.

## Key Takeaways

- Data preparation determines what a model can learn and how reliably it will work.
- Cleaning includes handling missing values, duplicates, inconsistent formats, and impossible values.
- Features must be available at prediction time; otherwise, the model has data leakage.
- Training, validation, and test data have different jobs and must stay separate.
- Transformations should be learned from training data and then applied consistently everywhere else.
- Privacy, fairness, and security should be considered before training begins.

## References

- [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course) — free lessons on numerical and categorical data, datasets, generalization, and overfitting.
- [scikit-learn: Common pitfalls and recommended practices](https://scikit-learn.org/stable/common_pitfalls.html) — practical guidance on consistent preprocessing and avoiding data leakage.
- [James, Witten, Hastie, Tibshirani, and Taylor, *An Introduction to Statistical Learning*](https://www.statlearning.com/) — freely downloadable introductory books with R and Python editions.
